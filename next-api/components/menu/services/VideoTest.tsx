import { useState } from 'react';
import axios from 'axios';

export default function VideoPlayer() {
  const [videoSrc, setVideoSrc] = useState<string>('');
  const [error, setError] = useState<string>('');

  const fetchVideo = async () => {
    const file_name = "kimgoeun.jpg"; // 클라이언트가 원하는 파일 이름
    try {
      const response = await axios.post('http://api.choiminho.co.kr/test', { file_name });
      const base64Data = response.data.data;
      const blob = await fetch(`data:video/mp4;base64,${base64Data}`).then(res => res.blob());
      setVideoSrc(URL.createObjectURL(blob));
      setError('');
    } catch (error) {
      console.error(error);
      setError('비디오를 불러오는 중에 오류가 발생했습니다.');
    }
  };

  return (
    <div>
      <button onClick={fetchVideo}>Fetch Video</button>
      {error && <div style={{ color: 'red' }}>{error}</div>}
      {videoSrc && (
        <video controls>
          <source src={videoSrc} type="video/mp4" />
        </video>
      )}
    </div>
  );
}