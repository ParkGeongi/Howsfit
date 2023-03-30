import { useState } from "react";
import axios from "axios";

const GanVideo = () => {
  const [file, setFile] = useState<File | null>(null);
  const [progress, setProgress] = useState<number>(0);
  const [isUploading, setIsUploading] = useState<boolean>(false);
  const [isCompleted, setIsCompleted] = useState<boolean>(false);
  const [filename, setFilename] = useState<string>("");
  const [imageSrc, setImageSrc] = useState<string>("");

  const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    if (event.target.files && event.target.files.length > 0) {
      const selectedFile = event.target.files[0];
      setFile(selectedFile);
      setFilename(selectedFile.name);
      setProgress(0);
      setIsCompleted(false);

      
      // 파일을 읽어서 이미지 미리보기를 생성합니다.
      const reader = new FileReader();
      reader.readAsDataURL(selectedFile);
      reader.onload = () => {
        setImageSrc(reader.result as string);
      };
    }
  };

  const handleUpload = async () => {
    if (file) {
      setIsUploading(true);
      const formData = new FormData();
      formData.append("image", file, filename);
      const startTime = Date.now();
      const interval = setInterval(() => {
        const elapsedTime = Date.now() - startTime;
        if (elapsedTime >= 300) {
          clearInterval(interval);
          setProgress(100);
          setIsCompleted(true);
        } else {
          setProgress(Math.floor((elapsedTime / 300) * 100));
        }
      }, 100);
      try {
        const response = await axios.post("http://api.choiminho.co.kr/video", formData, {
          headers: {
            "Content-Type": "multipart/form-data"
          }
        });
        setIsUploading(false);
        clearInterval(interval);
        setIsCompleted(true);
      } catch (error) {
        console.log(error);
      }
    }
  };

  const [videoSrc, setVideoSrc] = useState<string>("");
  const [error, setError] = useState<string>("");

  const fetchVideo = async () => {
    const file_name = filename; // 클라이언트가 원하는 파일 이름
    try {
      const response = await axios.post("http://api.choiminho.co.kr/test", { file_name });
      const base64Data = response.data.data;
      const blob = await fetch(`data:video/mp4;base64,${base64Data}`).then((res) => res.blob());
      setVideoSrc(URL.createObjectURL(blob));
      setError("");
    } catch (error) {
      console.error(error);
      setError("비디오를 불러오는 중에 오류가 발생했습니다.");
    }
  };


  return (
    <div style={{ display: "flex", alignItems: "center", justifyContent: "center", height: 800, boxShadow: '0 0 5px 5px rgba(0, 50, 200, 0.3)'}}>
      <table>
        <tbody>
          <tr>
            <td style={{ textAlign: "center", width: 400, height: 400, border: '5px solid pink'}}>
            <h2>원본 이미지</h2>
              {imageSrc && (
                <div>
                  <img src={imageSrc} alt="uploaded file" style={{maxWidth: "100%", maxHeight: 550 }} />
                </div>
              )}
            </td>


            <td style={{ textAlign: "center", width: 400, height: 400, border: '1px solid blue'}}>
            <h1>만화 사진 만들기</h1>
              <p style={{fontSize: '20px', color: "rgba(140, 210, 100, 1)", fontWeight: "bold"}}>이미지 업로드 가이드</p>
              <p>얼굴만 추출하지 않고 사진 전체를 만화로 변환합니다</p>
              <p>너무 큰 이미지는 900픽셀로 축소된 결과를 제공합니다</p>
              <br/><br/><br/>
              {error && <div style={{color: 'red'}}>{error}</div>}
              <div>
              <input style={{
                      backgroundColor: "rgba(0, 50, 200, 0.3)",
                      color: "white",
                      padding: "10px 15px",
                      borderRadius: "5px",
                      border: "none",
                      fontSize: "16px",
                      fontWeight: "bold",
                      cursor: "pointer",
                      boxShadow: "2px 2px 5px rgba(0, 0, 0, 0.5)",
                      textDecoration: "none",
                    }}type="file" accept="image/*" onChange={handleFileChange} />
              </div>
              <br/><br/>

              <div>
              <button style={{
                      backgroundColor: "rgba(0, 50, 200, 0.3)",
                      color: "white",
                      padding: "10px 15px",
                      borderRadius: "5px",
                      border: "none",
                      fontSize: "16px",
                      fontWeight: "bold",
                      cursor: "pointer",
                      boxShadow: "2px 2px 5px rgba(0, 0, 0, 0.5)",
                      textDecoration: "none",
                    }}onClick={handleUpload} disabled={isUploading}>
                    변환하기
              </button>
              </div>

              <div style={{border: '1px solid green'}}>
                {isUploading && <progress value={progress} max={100} />}
                {isCompleted && (
                  <span  style={{border: '1px solid black'}}>
                    <button onClick={fetchVideo}>페이크 영상 보기</button>
                  </span>
                )}
              </div>
            </td>


            <td style={{ textAlign: "center", width: 400, height: 400, border: '1px solid green'}}>
            <h2>만화 이미지</h2>
            {videoSrc && (
                  <video style={{width:400}} controls>
                    <source src={videoSrc} type="video/mp4" />
                  </video>
                )}
            </td>
  

    

          
          </tr>
        </tbody>
      </table>
    </div>
  );
};

export default GanVideo;
