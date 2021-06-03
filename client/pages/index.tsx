import styled from "styled-components";
import Navbar from "../src/components/Navbar";
import Content from "../src/components/Content";
import Footer from "../src/components/Footer";


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
      <Navbar/>
      <Footer/>
    </Content>
  </main>
);

//#262b31 navbar/ content color
//#d8d8da secondary

// be able to view different bundles (bundle component)
// search bar 
// account system
// Save Results (NEW)

export default Home;
