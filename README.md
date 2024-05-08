# Facial Insight: Augmented Object Detection  Using OpenCV
  This Python script integrates computer vision for skin condition assessment with PDF report generation, providing personalized skincare prescriptions. It uses OpenCV for face detection, analyzes skin conditions, and exports reports using ReportLab. This system offers a convenient and automated approach to skincare analysis and prescription.



Here's a step-by-step breakdown of the code:

Import Required Libraries:
Imports necessary libraries like OpenCV (cv2), NumPy (np), datetime, and modules from ReportLab.

Load Haar Cascade Classifier:
Loads the pre-trained Haar Cascade classifier for face detection.

Define Functions:
generate_prescription: Generates a personalized skin care prescription based on skin condition percentages.
assess_skin_condition: Performs skin condition analysis on the provided face region of interest (ROI) using a placeholder implementation.

export_report: Exports a PDF report containing skin condition details and personalized skin care prescription.

Open Webcam:
Initializes the webcam (or video file) using OpenCV's VideoCapture.
Webcam Loop:

Enters a loop to continuously capture frames from the webcam.

Converts each frame to grayscale for face detection.

Detects faces in the grayscale frame using the Haar Cascade classifier.

For each detected face:
Extracts the face region of interest.
Assesses the skin condition of the face using assess_skin_condition.
Generates a personalized skin care prescription using generate_prescription.

Exports a PDF report using export_report.

Draws text annotations for skin condition percentages and a rectangle around the detected face on the frame.

Displays the annotated frame.

-->Breaks the loop if the 'q' key is pressed.

Release Resources:
Releases the webcam and closes all OpenCV windows.
Each frame from the webcam is processed in real-time, assessing the skin condition of detected faces and providing personalized skin care recommendations, while also displaying the annotated frame for visualization.
![Screenshot (1560)](https://github.com/SATYAMSINGH0707/Facial-Insight--Augmented-Object-Detection--Using-OpenCV/assets/97894680/78d4cd92-3ff3-4259-9b7e-1b84e8bf2613)



To run this project, you'll need to install the following libraries:

OpenCV (cv2): This library is used for image and video processing, including face detection. You can install it via pip:
Copy code
pip install opencv-python
NumPy (np): NumPy is a fundamental package for numerical computing with Python. It's used extensively for numerical operations and array manipulation. Install it with:
Copy code
pip install numpy
ReportLab: ReportLab is a library used for creating PDF documents programmatically. You can install it with:
Copy code
pip install reportlab
Once you have these libraries installed, you should be able to run the project successfully. If you encounter any issues, ensure that your Python environment is properly set up and that you have the necessary permissions to install packages.



[report_20240422133127.pdf](https://github.com/SATYAMSINGH0707/Facial-Insight--Augmented-Object-Detection--Using-OpenCV/files/15253383/report_20240422133127.pdf)%PDF-1.4
%���� ReportLab Generated PDF document http://www.reportlab.com
1 0 obj
<<
/F1 2 0 R /F2 3 0 R
>>
endobj
2 0 obj
<<
/BaseFont /Helvetica /Encoding /WinAnsiEncoding /Name /F1 /Subtype /Type1 /Type /Font
>>
endobj
3 0 obj
<<
/BaseFont /Helvetica-Bold /Encoding /WinAnsiEncoding /Name /F2 /Subtype /Type1 /Type /Font
>>
endobj
4 0 obj
<<
/Contents 8 0 R /MediaBox [ 0 0 612 792 ] /Parent 7 0 R /Resources <<
/Font 1 0 R /ProcSet [ /PDF /Text /ImageB /ImageC /ImageI ]
>> /Rotate 0 /Trans <<

>> 
  /Type /Page
>>
endobj
5 0 obj
<<
/PageMode /UseNone /Pages 7 0 R /Type /Catalog
>>
endobj
6 0 obj
<<
/Author (\(anonymous\)) /CreationDate (D:20240422133127-05'00') /Creator (\(unspecified\)) /Keywords () /ModDate (D:20240422133127-05'00') /Producer (ReportLab PDF Library - www.reportlab.com) 
  /Subject (\(unspecified\)) /Title (\(anonymous\)) /Trapped /False
>>
endobj
7 0 obj
<<
/Count 1 /Kids [ 4 0 R ] /Type /Pages
>>
endobj
8 0 obj
<<
/Filter [ /ASCII85Decode /FlateDecode ] /Length 1046
>>
stream
GatU1gN(as&:Ml+ljGVr+\%X`]Tkf$(l%9$%*udk&lDjgZI9H#Ss:ldDFt(B-Bm(gn)`o`faS+:+56`128G[r]K2rU)6DCSUEG0=-[<+(r)ceYR:_QA%%Yd8HCNS=0T=k$_O)7J0VFiY_O/R[7mS3Ypi]ZSoBR?pi(U1LG#Bj#&redi/:eBKObb_1L6SMf@.bO@-a9,\,*kn"*:V<7JN1aV5XEE<.&Ls27>T*4dhG,8@*);#!nJ`W+AYOs7<!b$&fWP0jCIc#lek"p\8RN%6nq3\KSLf[;Z"1@j/D"CZ\K-OK`T$DA'BW\KhrfILl).!!7V)nbCYDcOJ[H3dmAm=b(`8dkD3Q"4SuI#7Y31M+jPG\Y=>O]9!nT)c8c9):7K6(*_8\Ga1'jZ^icEa^Z9P*H0U*AH!/c]?AVR:p+K".Djkpd;A:@aFZ@s;pt>%nLYXM*m[pndGr9TK1B**en*XGahW)N0]iOH*IJ0gqleY7(NBFF=I>54l,P0<M+(A*?K+2`g>9#XBhMelsEAkHID)g=R8EOa4<G%H;QUfM^gEV_W406J'QN#W6M0cjJ<psq+30*-T&T(reA#JYcK]'o$8a`XsL,ok.lM7tK^i=n;RA8Ql_4NM:iCb\O_Zg@Z&l;PZX&`Uc<C3BZ.nfa>8ulNsCJehgPQfQ?[\u4^9:3MQ.?!@sqOe14E$t8&@dA+\$XQ,3"Rg(.C6<XD.]G>Qnk'[Er$"G4oRf`QH.:`^7H::1TlXC#D454#9hlOZ45"IZ]B@_iB]V9B(=6%SP]U+1/P=@HD)=UnUE$ucc-'\QLnZ];)VU`KFUOlIB\+'`3-g%uCuo8eJ4hMq]cTs.6_'J>d]VW]Y%']nCmNGn7Z$S;.jbb)II+H3&e.<p'(sgB-#WqAb)Y(si,.XLii+>R/qq&[3^\"a/.T>Qkr2)e>4Je?VR*'WEaslUgQgfS5\;FnEc6]I/2-O%2G7Xp>HN7K4jnbZFgnc6nVI3SbA1BV>Z5ed<Z4b%)")6(9`KGe^4`oQ)oGZ!Q>8U@_kA&OL;e)54I`G~>endstream
endobj
xref
0 9
0000000000 65535 f 
0000000073 00000 n 
0000000114 00000 n 
0000000221 00000 n 
0000000333 00000 n 
0000000526 00000 n 
0000000594 00000 n 
0000000877 00000 n 
0000000936 00000 n 
trailer
<<
/ID 
[<ce9055a2c81980674da985be1a7e0b15><ce9055a2c81980674da985be1a7e0b15>]
% ReportLab generated PDF document -- digest (http://www.reportlab.com)

/Info 6 0 R
/Root 5 0 R
/Size 9
>>
startxref
2073
%%EOF




