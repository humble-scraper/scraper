import styled from "styled-components";
import Navbar from "../src/components/Navbar";
import Content from "../src/components/Content";


// const Content = styled.div`
//   justify-content: center;
//   flex-direction: column;
//   justify-items: center;
//   display: flex;

//   & > * {
//     margin-top: 7rem;
//   }
// `;

const Home = () => (
  <main>
    <Content>
      <Navbar>
        <img src="../assets/logo.png" />
      </Navbar>
    </Content>
  </main>
);

//#262b31 navbar/ content color
//#d8d8da secondary

// be able to view different bundles (bundle component)
// search bar 
// account system

export default Home;
