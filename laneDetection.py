import cv2
import numpy as np

def canny_edge_detection(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(src=gray, ksize=(3, 5), sigmaX=0.5)
    edges = cv2.Canny(blurred, 200, 235)
    return edges

def detect_lanes(edges):
    # Mask the region of interest // only the bottom half of the frame
    height, width = edges.shape
    mask = np.zeros_like(edges)
    polygon = np.array([[
        (0, height),
        (width, height),
        (width, height//2),
        (0, height//2),
    ]], np.int32)
    # Fill the polygon with white color in order to mask the region of interest
    cv2.fillPoly(mask, polygon, 255)
    # Apply the mask to the edges in order to get the region of interest
    masked_edges = cv2.bitwise_and(edges, mask)
    
    # Detect lines using Hough Transform
    lines = cv2.HoughLinesP(masked_edges, 1, np.pi/180, 60, maxLineGap=150)
    return lines

def draw_lane_boxes(frame, lines):
    if lines is None:
        return frame, 'N/A', 'N/A'
    
    height, width = frame.shape[:2]
    center_x = width // 2


    left_lines = []
    right_lines = []
    for line in lines:
        # Extract the coordinates of the line
        x1, y1, x2, y2 = line[0]

        # Fit a linear equation to the line

        if x1 == x2:
            continue  # Ignore vertical lines
        slope = (y2 - y1) / (x2 - x1)
        # Filter lines based on slope
        # Left lane lines will have a negative slope
        if slope < 0:
            left_lines.append(line)

        # Right lane lines will have a positive slope
        else:
            right_lines.append(line)

    #Draw center line
    cv2.line(frame, (center_x, height), (center_x, height//2), (0, 255, 255), 2)

    #Initialize distance variables
    left_dist = right_dist = 'N/A'

    # Draw bounding boxes for left and right lanes
    if left_lines:
        left_x = int(min(min(line[0][0], line[0][2]) for line in left_lines))
        right_x = int(max(max(line[0][0], line[0][2]) for line in left_lines))
        top_y = int(min(min(line[0][1], line[0][3]) for line in left_lines))
        bottom_y = int(max(max(line[0][1], line[0][3]) for line in left_lines))
        cv2.rectangle(frame, (left_x, top_y), (right_x, bottom_y), (0, 255, 0), 2)
        cv2.putText(frame, "Left Lane", (left_x, top_y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Calculate the distance of the left lane from the center
        left_dist = center_x - right_x

    if right_lines:
        left_x = int(min(min(line[0][0], line[0][2]) for line in right_lines))
        right_x = int(max(max(line[0][0], line[0][2]) for line in right_lines))
        top_y = int(min(min(line[0][1], line[0][3]) for line in right_lines))
        bottom_y = int(max(max(line[0][1], line[0][3]) for line in right_lines))
        cv2.rectangle(frame, (left_x, top_y), (right_x, bottom_y), (0, 0, 255), 2)
        cv2.putText(frame, "Right Lane", (left_x, top_y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

        # Calculate the distance of the right lane from the center
        right_dist = left_x - center_x

    

    cv2.putText(frame, f"Left Distance: {left_dist}", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    cv2.putText(frame, f"Right Distance: {right_dist}", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    return frame, left_dist, right_dist

# Initialize the camera
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # Use 0 for Raspberry Pi
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 576)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not capture frame.")
        break

    edges = canny_edge_detection(frame)
    lines = detect_lanes(edges)
    frame_with_boxes, left_dist, right_dist = draw_lane_boxes(frame.copy(), lines)

    cv2.imshow('Lane Detection', frame_with_boxes)
    cv2.imshow('Edges', edges)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()