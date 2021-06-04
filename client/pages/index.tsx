import Navbar from "../src/components/Navbar";
import Root from "../src/components/Root";
import Footer from "../src/components/Footer";
import Content from "../src/components/Content";

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
