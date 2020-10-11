# (c) stonatm@gmail.com
class analog:

  import machine

  T_OFFEST = 0

  def set_t_offest(offest):
    analog.T_OFFEST = offest

  def lm35_read(pin):
    adc0 = machine.ADC(pin)
    adc0.width(machine.ADC.WIDTH_9BIT)
    adc0.atten(machine.ADC.ATTN_0DB)
    temp = adc0.read() / 10
    return temp + analog.T_OFFEST

  def tmp36_read(pin):
    adc0 = machine.ADC(pin)
    adc0.width(machine.ADC.WIDTH_9BIT)
    adc0.atten(machine.ADC.ATTN_0DB)
    temp = (adc0.read()-500) / 10
    return temp + analog.T_OFFEST
