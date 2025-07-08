import numpy as np
import cv2

# Set frame size
width, height = 640, 480

while True:
    # Generate random noise frame
    noise_frame = np.random.randint(0, 256, (height, width), dtype=np.uint8)

    # Display the noise frame
    cv2.imshow('Static TV Effect', noise_frame)

    # Exit when 'q' is pressed
    if cv2.waitKey(50) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
