import { useState } from "react";
import axios from "axios";

const loadingStyle = {
  fontSize: "24px",
  fontWeight: "bold",
  marginBottom: "32px",
  color: "#787878",
};

const resultStyle = {
  maxWidth: "80%",
  maxHeight: "500px",
  margin: "16px auto",
  border: "none",
  borderRadius: "10px",
};

const buttonStyle = {
  backgroundColor: "#FBB6CE",
  color: "white",
  padding: "12px 20px",
  borderRadius: "5px",
  border: "none",
  fontSize: "16px",
  fontWeight: "bold",
  cursor: "pointer",
  boxShadow: "2px 2px 5px rgba(0, 0, 0, 0.5)",
  textDecoration: "none",
  margin: "32px auto",
  display: "block",
};

const linkStyle = {
  backgroundColor: "#FBB6CE",
  color: "white",
  padding: "12px 15px",
  borderRadius: "5px",
  border: "none",
  fontSize: "16px",
  fontWeight: "bold",
  cursor: "pointer",
  boxShadow: "2px 2px 5px rgba(0, 0, 0, 0.5)",
  textDecoration: "none",
};

const Viton = () => {
  const [isLoading, setIsLoading] = useState(false);
  const [imageSrc, setImageSrc] = useState("");
  const [url, setUrl] = useState<string>("https://bucket-aiacademy.s3.ap-northeast-2.amazonaws.com/howsfit/");

  const handleClick = async () => {
    setIsLoading(true);
    try {
      const response = await axios.post("http://howsfit.shop/try-on");
      const imageBase64 = response.data.data;
      setImageSrc(`data:image/jpeg;base64,${imageBase64}`);
    } catch (error) {
      console.error(error);
    } finally {
      setIsLoading(false);
    }
  };

  const handleDownload = () => {
    const link = document.createElement("a");
    link.href = imageSrc;
    link.download = "viton-image.jpeg";
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  };

  return (
    <div
      style={{
        textAlign: "center",
        padding: "64px",
        borderRadius: "10px",
        boxShadow: "2px 2px 5px rgba(0, 0, 0, 0.5)",
        maxWidth: "600px",
        margin: "0 auto"
      }}
    >
      {isLoading ? (
        <div
          style={{
            display: "flex",
            flexDirection: "column",
            alignItems: "center"
          }}
        >
          <p style={{ fontSize: "24px" }}>로딩중입니다...</p>
          <img style={{ width: 50 }} src={`${url}walk.gif`} alt="loading" />
        </div>
      ) : (
        <>
          <button style={buttonStyle} onClick={handleClick}>
            결과 확인
          </button>
          {imageSrc && (
            <div style={{ display: "flex", flexDirection: "column", alignItems: "center" }}>
              <img src={imageSrc} alt="image" style={resultStyle} />
              <a
                href={imageSrc}
                download
                style={linkStyle}
                onClick={handleDownload}
              >
                다운로드
              </a>
            </div>
          )}
        </>
      )}
    </div>
  );
};

export default Viton;