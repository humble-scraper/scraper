import styled from "styled-components";
import HelloWorld from "../src/components/HelloWorld";

const Content = styled.div`
  justify-content: center;
  flex-direction: column;
  justify-items: center;
  display: flex;

  & > * {
    margin-top: 7rem;
  }
`;

const Home = () => (
  <main>
    <Content>
      <HelloWorld />
    </Content>
  </main>
);

export default Home;
