import { Button, Loader } from "@mantine/core";
import { useEffect, useState } from "react";
import { Microphone, PlayerStop, Tex } from "tabler-icons-react";
import useRecorder from "../../hooks/useRecorder";
import { FormAnswer, Form, DefaultApi, FieldSubmit } from "../../../../generated";
import { ApiConfiguration } from "../../../../api/ApiConfiguration";

type RecorderProps = {
    form: Form;
    setAnswers: (answers: FormAnswer) => void;
    answers: FormAnswer;
}

const RecorderInput = ( { form }: RecorderProps ) => {
    const { isRecording, audioUrl, startRecording, stopRecording } = useRecorder();

    const [error, setError] = useState<string | undefined>(undefined);
    const [sending, setSending] = useState<boolean>(false);

    const onSubmit = async () => {
        const api = new DefaultApi(ApiConfiguration);
        setSending(true);
        const audioFile = new File([audioUrl!], "audio.wav");
        const audioFileBytes = await convertAudioToBytes(audioFile);
        console.log('Audio bytes:', audioFileBytes);
        for (const field of form.fields) {
            console.log(audioFile instanceof File)
            api.convertSpeechToTextSpeechPost({
                audioFile: audioFile,
                field: field,
                formName: form.name }).then((response) => {
                console.log(response);
            }
            ).catch((error) => {
                setError(error.message);
            }
            );
        }
        setSending(false);
      };

      function convertAudioToBytes(file: File): Promise<Uint8Array> {
        return new Promise<Uint8Array>((resolve, reject) => {
          const reader = new FileReader();
      
          reader.onload = () => {
            const buffer = reader.result as ArrayBuffer;
            const bytes = new Uint8Array(buffer);
      
            resolve(bytes);
          };
      
          reader.onerror = () => {
            reject(new Error('Failed to convert audio to bytes.'));
          };
      
          reader.readAsArrayBuffer(file);
        });
      }
      
    useEffect(() => {
        if (audioUrl) {
            onSubmit();
        }
    }
    , [audioUrl]);

    return (
        <div style={{display: "grid", placeItems: "center", height: "330px", border: "1px solid #ccc", borderRadius: "5px", padding: "10px"}}>
            <div style={{display: "flex", flexDirection: "column", alignItems: "center"}}>
            {sending ? <Loader size={50}/> : 
            <Button onClick={isRecording ? stopRecording : startRecording} style={{borderRadius: "50%", height: "50px", width: "50px", border: `3px solid ${error ? "red" : "black"}`, background: "transparent"}} p={0}>
  
                {isRecording ? <Loader variant="bars" color="red" size={24}/> : <Microphone color="black" size={24} /> }
            </Button>
            }
            {error && <p style={{color: "red"}}>{error}</p>}
            </div>
        </div>
    );
};

export default RecorderInput;
