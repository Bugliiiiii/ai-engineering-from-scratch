import "dotenv/config";
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
    apiKey: process.env.ANTHROPIC_API_KEY,
    baseURL: "https://api.deepseek.com/anthropic"
});

const response = await client.messages.create({
    model: "deepseek-v4-flash",
    max_tokens: 10000,
    messages: [
        {
            role: "user",
            content: "What is the capital of France?"
        }
    ]
});

// 只打印 text 类型的块的内容
response.content.forEach(block => {
    if (block.type === 'text') console.log(block.text);
});