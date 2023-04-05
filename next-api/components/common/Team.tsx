import Image from 'next/image';
import React, { useState } from 'react';

interface TeamMemberProps {
  name: string;
  email: string;
  kakao: string;
  imageSrc: string;
  gitHubUrl: string;
  blogUrl: string;

}

const TeamMember: React.FC<TeamMemberProps> = ({
  name,
  email,
  kakao,
  imageSrc,
  gitHubUrl,
  blogUrl,

}) => {
  const [url, setUrl] = useState<string>(
    'https://bucket-aiacademy.s3.ap-northeast-2.amazonaws.com/howsfit/',
  );

  const handleClickGitHub = () => {
    window.location.href = gitHubUrl;
  };

  const handleClickBlog = () => {
    window.location.href = blogUrl;
  };

  return (
    <div style={{ textAlign: 'center', width: 230 }}>
      <img style={{ width: 200 }} src={`${url}${imageSrc}`} alt={name} />
      <p style={{ margin: 0, fontWeight: 600, fontSize: 18 }}>{name}</p>
      <p style={{ margin: '5px 0' }}>{email}</p>
      <p style={{ margin: '5px 0' }}>{kakao}</p>
      <div style={{ margin: '10px 0' }}>
        <p style={{ margin: 0, fontWeight: 600 }}>Click to view profile:</p>
        <img onClick={handleClickGitHub} style={{ width: 30, margin: '0 5px', cursor: 'pointer' }} src={`${url}github.png`} alt="git button image" />
        <img onClick={handleClickBlog} style={{ width: 30, margin: '0 5px', cursor: 'pointer' }} src={`${url}velog.png`} alt="blog button image" />
      </div>

    </div>
  );
};

const Team: React.FC = () => {
  return (
    <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', height: '100vh' }}>
      <table style={{ borderSpacing: '30px' }}>
        <tbody>
          <tr>
            <td>
              <TeamMember
                name="박 건 기"
                email="이메일 : pgg11357@gmail.com"
                kakao="카카오톡 : pgg113579@naver.com"
                imageSrc="geongi.jpg"
                gitHubUrl="https://github.com/ParkGeongi"
                blogUrl="https://velog.io/@pgg113579/Howsfit-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EA%B0%9C%EC%9A%94"

              />
            </td>
            <td>
              <TeamMember
                name="조 용 훈"
                email="이메일 : "
                kakao="카카오톡 : "
                imageSrc="이미지"
                gitHubUrl="https://github.com/Johyonghoon"
                blogUrl="https://velog.io/@johyonghoon"

              />
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  );
};

export default Team;