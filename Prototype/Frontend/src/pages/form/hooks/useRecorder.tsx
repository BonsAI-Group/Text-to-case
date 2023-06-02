import { Button } from "@mantine/core";
import { useEffect, useState } from "react";
import { Microphone, PlayerStop } from "tabler-icons-react";

type UseRecorderProps = {
    isRecording: boolean;
    audioUrl: string | undefined;
    startRecording: () => void;
    stopRecording: () => void;
}

const useRecorder = (): UseRecorderProps => {
    const [isRecording, setIsRecording] = useState<boolean>(false);
    const [audioChunks, setAudioChunks] = useState<Blob[]>([]);
    const [mediaRecorder, setMediaRecorder] = useState<MediaRecorder | undefined>(undefined);
    const [audioUrl, setAudioUrl] = useState<string | undefined>(undefined);

    useEffect(() => {
        navigator.mediaDevices.getUserMedia({ audio: true }).then((stream) => {
            const mediaRecorder = new MediaRecorder(stream, { mimeType: "audio/webm", audioBitsPerSecond: 44100 });
            setMediaRecorder(mediaRecorder);
            mediaRecorder.ondataavailable = (e) => {
                setAudioChunks((chunks) => [...chunks, e.data]);
            };
            mediaRecorder.onerror = (e) => {
                console.log(e);
            }
        });
    }
        , []);

    const startRecording = () => {
        if (mediaRecorder) {
            mediaRecorder.start();
            setIsRecording(true);
        }
    };

    const stopRecording = () => {
        if (mediaRecorder) {
            mediaRecorder.stop();
            setIsRecording(false);
        }
    };

    useEffect(() => {
        if (audioChunks.length === 0) {
            return;
        }
        const audioBlob = new Blob(audioChunks, { type: "audio/webm" });
        const audioUrl = URL.createObjectURL(audioBlob);
        setAudioUrl(audioUrl);
    }
        , [audioChunks, mediaRecorder]);

    return {
        isRecording,
        audioUrl,
        startRecording,
        stopRecording
    } as UseRecorderProps;
};

export default useRecorder;
