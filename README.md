# POLLY Pipeline

This project uses Amazon Polly's generative engine to convert text from speech.txt into an .mp3 file and uploads it to an S3 bucket using GitHub Actions. It includes both beta and production workflows triggered on pull requests and pushes to the main branch respectively.

---

Prerequisites 

* ﻿﻿AWS account
* ﻿﻿An S3 bucket for each environment (e.g., beta and prod)
* ﻿AWS access/secret keys with polly:SynthesizeSpeech and s3:Putobject permissions
* ﻿﻿GitHub repository secrets configured

---

AWS Credentials & S3 Setup

1. ﻿﻿﻿Create an S3 bucket (or two: one for beta, one for prod).
2. In your GitHub repository, go to Settings Secrets and variables → Actions and add the following repository secrets:
* AWS_ACCESS_KEY_ID
* ﻿AWS_SECRET_ACCESS_KEY
* ﻿﻿53_BUCKET_BETA - e.g., my-tts-bucket-beta
* ﻿﻿S3_PATH_BETA - e.g., audio/beta/example.mp3
* ﻿﻿S3_BUCKET_PROD - e.g., my-tts-bucket-prod
* ﻿﻿S3_PATH_PROD - e.g., audio/prod/example* mp3

---

How to Modify the Text


Update the contents of the speech.txt file with the text you'd like Polly to convert to speech. For example:
Welcome to the Polly generative voice demo.
Save the file and commit the change to trigger the appropriate workflow.

---


Triggering the Workflows


• Beta Environment
Triggered on any pull request (pul1_request)
This converts the text and uploads example.mp3
to the beta S3 bucket.
• Production Environment
Triggered on push to the main branch (push → main)
This converts the text and uploads example. mp3 to the production S3 bucket.

---

Verifying the Uploaded • mp3 Files

1. ﻿﻿﻿Go to the AWS S3 Console.
2. ﻿﻿﻿Navigate to your bucket and folder (e.g.,
audio/beta/
audio/prod/
1. ﻿﻿﻿Download example.mp3 and play it locally.
2. ﻿﻿﻿Confirm that the audio matches your updated speech.txt.

---

File Structure

.
├── .github/
│   └── workflows/
│       ├── beta.yml
│       └── prod.yml
├── speech.txt
├── synthesize.py
└── README.md



