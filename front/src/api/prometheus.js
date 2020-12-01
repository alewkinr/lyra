import Axios from "axios"
const qurl = "http://178.154.232.207:9090/api/v1/query_range?query=lyra_metrics_counter_total&start=1604413230&end=1606413251&step=1000"

export default {
    data: async () => {
        return Axios.get(qurl)
    }
}