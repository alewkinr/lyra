import ModelList from '../components/models/ModelsList'
import ModelCard from '../components/models/ModelCard'

export default [
    {
        path: '/models',
        component: ModelList,
        name: 'Model List'
    },
    {
        path: '/models/:id',
        component: ModelCard,
        name: 'Model Card'
    }
]