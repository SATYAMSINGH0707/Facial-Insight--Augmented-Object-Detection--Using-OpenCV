import cv2
import numpy as np
from datetime import datetime
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

# Load the pre-trained Haar Cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Function to generate personalized skin care prescription
def generate_prescription(acne_percentage, wrinkle_percentage, dark_spot_percentage, redness_percentage):
    prescription = []

    if acne_percentage > 20:
        prescription.append("For acne:")
        prescription.append("- Use a gentle cleanser and consider a non-comedogenic moisturizer.")
        prescription.append("- Incorporate a topical treatment containing salicylic acid.")

    if wrinkle_percentage > 15:
        prescription.append("For wrinkles:")
        prescription.append("- Apply a moisturizer with hyaluronic acid to hydrate the skin.")
        prescription.append("- Use a broad-spectrum sunscreen with SPF 30 or higher daily.")

    if dark_spot_percentage > 10:
        prescription.append("For dark spots:")
        prescription.append("- Consider using a serum with ingredients like vitamin C or niacinamide.")
        prescription.append("- Apply sunscreen to prevent further pigmentation.")

    if redness_percentage > 15:
        prescription.append("For redness:")
        prescription.append("- Choose a moisturizer with soothing ingredients like chamomile or aloe vera.")
        prescription.append("- Use a gentle, fragrance-free sunscreen.")

    return prescription

# Function to perform skin condition analysis
def assess_skin_condition(face_roi):
    # Placeholder implementation
    # Add your code to analyze skin conditions based on the provided face_roi
    # Return the relevant skin condition percentages and other information
    acne_percentage = np.random.randint(0, 100)  # Random value for demonstration
    wrinkle_percentage = np.random.randint(0, 100)
    dark_spot_percentage = np.random.randint(0, 100)
    redness_percentage = np.random.randint(0, 100)
    skin_texture = "Normal"

    return acne_percentage, wrinkle_percentage, dark_spot_percentage, redness_percentage, skin_texture

# Function to export a PDF report
def export_report(acne_percentage, wrinkle_percentage, dark_spot_percentage, redness_percentage, skin_texture, prescription):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    path = "C:/Users/satya/OneDrive/Documents/Zoom"  # Custom path
    filename = f'{path}/report_{timestamp}.pdf'

    doc = SimpleDocTemplate(filename, pagesize=letter)
    styles = getSampleStyleSheet()
    report = []

    report.append(Paragraph(f'Skin Condition Report - {timestamp}', styles['Title']))

    # Skin condition details
    data = [
        ["Skin Condition", "Percentage"],
        ["Acne", f"{acne_percentage:.2f}%"],
        ["Wrinkles", f"{wrinkle_percentage:.2f}%"],
        ["Dark Spots", f"{dark_spot_percentage:.2f}%"],
        ["Redness", f"{redness_percentage:.2f}%"],
        ["Skin Texture", skin_texture]
    ]

    table = Table(data, colWidths=[200, 100])
    table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
                               ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
                               ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                               ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                               ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                               ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                               ('GRID', (0, 0), (-1, -1), 1, colors.black)]))
    report.append(table)

    report.append(Spacer(1, 12))

    # Skin care prescription
    report.append(Paragraph("Skin Care Prescription:", styles['Heading2']))
    for line in prescription:
        report.append(Paragraph(line, styles['Normal']))

    doc.build(report)

    print(f'Report exported to {filename}')
    return filename  # Return the filename

# Open the webcam (you can also use a video file or image)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()
    
    if not ret:
        print("Error: Could not read frame from webcam.")
        break
    
    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Perform face detection
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    
    # Process each detected face
    for (x, y, w, h) in faces:
        # Extract the face region
        face_roi = frame[y:y+h, x:x+w]
        
        # Assess skin condition
        acne_percentage, wrinkle_percentage, dark_spot_percentage, redness_percentage, skin_texture = assess_skin_condition(face_roi)
        
        # Generate personalized skin care prescription
        prescription = generate_prescription(acne_percentage, wrinkle_percentage, dark_spot_percentage, redness_percentage)
        
        # Export a PDF report
        report_filename = export_report(acne_percentage, wrinkle_percentage, dark_spot_percentage, redness_percentage, skin_texture, prescription)
        
        # Draw text annotations for skin condition percentages
        cv2.putText(frame, f'Acne: {acne_percentage:.2f}%', (x, y-30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        cv2.putText(frame, f'Wrinkles: {wrinkle_percentage:.2f}%', (x, y-20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        cv2.putText(frame, f'Dark Spots: {dark_spot_percentage:.2f}%', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        cv2.putText(frame, f'Redness: {redness_percentage:.2f}%', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        
        # Draw a rectangle around the face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    # Display the frame
    cv2.imshow('Skin Condition Assessment', frame)
    
    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()
