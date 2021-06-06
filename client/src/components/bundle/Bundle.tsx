import { useState } from "react";
import styled from "styled-components";
import Collapsed from "./Collapsed";
import Expanded from "./Expanded";



function Bundle() {
  const [showExpanded, setExpanded] = useState(true);

  const open = () => {
    setExpanded((prev) => !prev);
  }

  return (
    <>
      {showExpanded? (
        <Collapsed showExpanded={showExpanded} setExpanded={setExpanded} open={open}/>
      ) : (
       <Expanded showExpanded={showExpanded} setExpanded={setExpanded} open={open}/>
      )}
    </>
  );
}

export default Bundle;
