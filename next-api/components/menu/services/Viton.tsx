import { useState } from "react";
import axios from "axios";

function Viton() {
  const [url, setUrl] = useState<string>('https://bucket-4cr3lx.s3.ap-northeast-2.amazonaws.com/');
  const [image, setImage] = useState<File | null>(null);
  const [previewImage, setPreviewImage] = useState<string | null>(null);
  const [resizedImage, setResizedImage] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [errorMessage, setErrorMessage] = useState<string | null>(null);
 
  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    if (!image) return;

    setIsLoading(true);
    setErrorMessage(null); // 에러 메시지 초기화

    const formData = new FormData();
    formData.append("image", image);

    try {
      const response = await axios.post<{ data: string }>(
        "http://127.0.0.1:8000/cloth",
        formData,
        {
          headers: { "Content-Type": "multipart/form-data" },
        }
      );

      const imageData = response.data.data;
      setResizedImage(`data:image/jpeg;base64,${imageData}`);
    } catch (error) {
      console.log(error);
      setErrorMessage("변환 실패 다시 업로드해 주세요.\n이미지 업로드 가이드를 참고 해주세요"); // 실패 메시지 설정
    } finally {
      setIsLoading(false);
    }
  };

  const handleImageChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (file) {
      setImage(file);

      const reader = new FileReader();
      reader.onload = () => {
        setPreviewImage(reader.result as string);
      };
      reader.readAsDataURL(file);
    } else {
      setImage(null);
      setPreviewImage(null);
    }
  };

  return (
    <div style={{ display: "flex", alignItems: "center", justifyContent: "center", height: 800, boxShadow: '0 0 5px 5px pink'}}>
      <table>
        <tbody>
          <tr>
            <td style={{ textAlign: "center", width: 400, height: 400}}>
              <h2>원본 이미지</h2>
              {previewImage && !isLoading && !errorMessage && (
                <div>
                  <img style={{ width: 400 }} src={previewImage} alt="Preview" />
                </div>
              )}
           
              {isLoading && (
                <div>
                  <img style={{ width: 300 }} src={`${url}ai_logo.gif`} alt="logo" />
                  <h3>변환 중입니다!</h3>
                </div>
              )}
              {errorMessage && (
                <div>
                  <p>{errorMessage}</p>
                  <button onClick={() => window.location.reload()}>새로고침</button>
                </div>
              )}
            </td>


            <td style={{ textAlign: "center", width: 400, height: 400}}>
              
              <p style={{fontSize: '20px', color: "hotpink", fontWeight: "bold"}}>이미지 업로드 가이드</p>
              <p>옷 사진을 업로드 해주세요</p>
              <br/><br/><br/><br/><br/><br/>
              <form onSubmit={handleSubmit}>
                <input  style={{
                      backgroundColor: "pink",
                      color: "white",
                      padding: "10px 15px",
                      borderRadius: "5px",
                      border: "none",
                      fontSize: "16px",
                      fontWeight: "bold",
                      cursor: "pointer",
                      boxShadow: "2px 2px 5px rgba(0, 0, 0, 0.5)",
                      textDecoration: "none",
                    }} type="file" accept="image/*" onChange={handleImageChange} />
                    <br/><br/><br/>
                <button style={{
                      backgroundColor: "pink",
                      color: "white",
                      padding: "10px 15px",
                      borderRadius: "5px",
                      border: "none",
                      fontSize: "16px",
                      fontWeight: "bold",
                      cursor: "pointer",
                      boxShadow: "2px 2px 5px rgba(0, 0, 0, 0.5)",
                      textDecoration: "none",
                    }} type="submit">변환하기</button>
              </form>
            </td>
            <td style={{ textAlign: "center", width: 400, height: 400}}>
              <h2>전처리 이미지</h2>
              {resizedImage && (
                <div>
                  <img style={{ width: 400 }} src={resizedImage} alt="Resized" />
                  <br /><br />
                  <a
                    href={resizedImage}
                    download
                    style={{
                      backgroundColor: "pink",
                      color: "white",
                      padding: "10px 15px",
                      borderRadius: "5px",
                      border: "none",
                      fontSize: "16px",
                      fontWeight: "bold",
                      cursor: "pointer",
                      boxShadow: "2px 2px 5px rgba(0, 0, 0, 0.5)",
                      textDecoration: "none",
                    }}
                  >
                    다운로드
                  </a>
                </div>
              )}
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  );
}

export default Viton;



