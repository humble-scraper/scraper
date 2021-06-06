import styled from "styled-components";
import Navbar from "../src/components/navbar";
import Footer from "../src/components/Footer";
import Content from "../src/components/Content";


const Root = styled.div`
  background-color: #494f5c;
  border-bottom: 1px #373c46 solid;
  box-shadow: 1px 2px 3px rgb(0 0 0 / 45%);
  height: 1000px;
  width: 100%;
  display: "flex";
  position: relative;
`;

const Home = () => (
  <main>
    <Root>
      <Navbar/>
      <Content/>
      <Footer/>
    </Root>
  </main>
);

export default Home;
