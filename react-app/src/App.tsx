import React, { useState } from "react";
import axios from "axios";

function App() {
	const [count, setCount] = useState(0);
	const [data, setData] = useState<SystemHealthcheckRes | null>(null);
	const url = "http://127.0.0.1:8000/system/healthcheck";

	type SystemHealthcheckRes = {
		status: string;
	};

	const GetData = () => {
		axios.get(url).then((res) => {
			setData(res.data);
		});
	};
	return (
		<div>
			<div>ここに処理を書いてください</div>
			<p> You clicked {count} </p>
			<button onClick={() => setCount(count+1)}>Click!</button>
			{data ? <div>{data.status}</div> : <button onClick={GetData}>データを取得</button>}
		</div>
	);
}

export default App;
