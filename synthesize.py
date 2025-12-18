import boto3 # Import the AWS SDK for pyython to interact with AWS services

with open('speech.txt','r') as file:
    text = file.read()
    print(text)

# Create a Polly client to interact with the amazon Polly service 
pollly = boto3.client('polly')

# Request Polly to synthesize speech using the generative engine
response = polly.synthesize_speech(
    Engine='generation',     # Use the new generative engine for more natural speech 
    OutputFormat='mp3',      # Request the audio output in MP3 format
    text=text,# the text that Polly will convert to speech 
    VoiceId='Stephen'        # Use the 'Stephen' voice for the synthesized speech 
)

# Extract the audio stream from the reponse 
audioStream = response ['AudioStream']

# Save the audio stream to file named 'exaple.mp3'
with open("exemple.mp3","wb") as f:
    f.write(audioStream.read()) # Read and write the binary MP3 content to file
    print("Polly output saved.") 