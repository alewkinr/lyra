// import request from "./client"
const prefix = '/api'

export default {
    login: async (login, password) => {
        return {
            token: `${prefix}${login}${password}`
        }
        // return request({
        //     'url': `${prefix}/`
        // })
    }
}