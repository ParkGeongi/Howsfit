import React, { useState } from 'react'
import Link from 'next/link';



const Home: React.FC = () => {
 const [url, setUrl] = useState<string>("https://bucket-aiacademy.s3.ap-northeast-2.amazonaws.com/howsfit/")
  return (
    <div style={{display: 'flex', alignItems: 'center', justifyContent: 'center', height: "auto"}} >
    <table>
      <tbody>
        <tr>
          <td style={{textAlign: 'center'}}>
            <h5>원본 이미지</h5>
            <img style={{ width: 300 }} src={`${url}person_1.jpg`} alt="person_1" />
          </td>
          <td style={{textAlign: 'center'}}>
            <h5>옷 이미지</h5>
            <img style={{ width: 300 }} src={`${url}cloth_1.jpg`} alt="logo" />
          </td>
          <td style={{textAlign: 'center'}}>
            <h5>가상피팅 이미지</h5>
            <img style={{ width: 300 }} src={`${url}output_1.png`} alt="logo" />
          </td>
        </tr>

       
        <tr>
          <td style={{textAlign: 'center'}}>
          </td>
          <td style={{textAlign: 'center'}}>
            <h3>가상피팅 체험하기</h3>
            <p style={{
                backgroundColor: "rgb(255, 160, 122)",
                color: "white",
                padding: "10px 15px",
                borderRadius: "5px",
                border: "none",
                fontSize: "16px",
                fontWeight: "bold",
                cursor: "pointer",
                boxShadow: "0 3px 5px rgba(0, 0, 0, 0.2)",
                textDecoration: "none",
                display: "inline-block",
                transition: "background-color 0.2s ease-in-out",
                width: 400
              }}>
                <Link href="../menu/service">서비스 페이지로 &raquo;</Link>
            </p>
          </td>
        </tr>

      </tbody>
    </table>
  </div>
  );
}
export default Home