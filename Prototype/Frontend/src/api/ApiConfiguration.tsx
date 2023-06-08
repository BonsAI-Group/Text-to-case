import { Configuration } from "../generated"

export const ApiConfiguration = new Configuration({
  basePath: process.env.REACT_APP_API_URL,
})