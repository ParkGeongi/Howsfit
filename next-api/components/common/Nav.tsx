import React from 'react';
import Link from 'next/link';
import styles from '@/styles/Nav.module.css';
import Image from 'next/image';
import { Button } from '@mui/material';

export default function Nav() {
  return (
    <div className={styles.container}>
      <div className={styles.header} style={{ justifyContent: 'center' }}>
        <div className={styles.logo} style={{ width: 600 }}>
          <Link href="/">
            <img
              style={{ width: 200 }}
              src="https://bucket-aiacademy.s3.ap-northeast-2.amazonaws.com/howsfit/howsfit_logo.png"
              alt="logo"
            />
          </Link>
        </div>
        <div className={styles.menus}>
          <div className={styles.mainMenu}>

            <Button style={{ fontSize: '20px', color: 'black' }}>
              <Link href="/menu/team">팀원</Link>
            </Button>
            <Button style={{ fontSize: '20px', color: 'black' }}>
              <Link href="/menu/service">서비스</Link>
            </Button>
          </div>
        </div>
      </div>
    </div>
  );
}