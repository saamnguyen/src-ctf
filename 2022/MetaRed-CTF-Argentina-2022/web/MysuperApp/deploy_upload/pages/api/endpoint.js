import vars from '../../utils/vars'

export default function handler(req, res) {
  // res.status(200).json({ name: vars.FLAG })
  res.status(200).json({ name: vars.SECRET })
}
