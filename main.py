from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField
from wtforms.validators import DataRequired, InputRequired

from model import Model

app = Flask(__name__)

# Flask-WTF requires an encryption key - the string can be anything
app.config['SECRET_KEY'] = 'C2HWGVoMGfNTBsrYQg8EcMrdTimkZfAb'

# Flask-Bootstrap requires this line
Bootstrap(app)

class DadosPaciente(FlaskForm):

    # definindo os campos do formulário
    pregnant    = IntegerField('Pregnant', validators=[InputRequired()])
    glucose     = IntegerField('glucose', validators=[DataRequired()])
    bp          = IntegerField('bp', validators=[DataRequired()])
    skin        = IntegerField('skin', validators=[DataRequired()])
    insulin     = IntegerField('insulin', validators=[InputRequired()])
    bmi         = FloatField('bmi', validators=[DataRequired()])
    pedigree    = FloatField('pedigree', validators=[DataRequired()])
    age         = IntegerField('age', validators=[DataRequired()])
    
    submit = SubmitField('Consultar')
    
@app.route('/', methods=['GET', 'POST'])
def index():
    
    # criando uma instância do formário DadosPaciente
    form = DadosPaciente()
    message = ""
    
    if form.validate_on_submit():

        # capturando o valor de cada feature preenchida no formulário
        x_pregnant  = form.pregnant.data
        x_glucose   = form.glucose.data
        x_bp        = form.bp.data
        x_skin      = form.skin.data
        x_insulin   = form.insulin.data
        x_bmi       = form.bmi.data
        x_pedigree  = form.pedigree.data
        x_age       = form.age.data
        
        try:
            # Cria uma instância do modelo salvo
            modelo = Model("ml/models/modelo_salvo.sav")
            
            # Obtém a predição do modelo passando a lista de features
            response = modelo.get_predict([[x_pregnant, x_glucose, x_bp, x_skin, x_insulin, x_bmi, x_pedigree, x_age]])
            response_prob = modelo.get_predict_prob([[x_pregnant, x_glucose, x_bp, x_skin, x_insulin, x_bmi, x_pedigree, x_age]])

            if (response[0] == 1):
                message = "O paciente TEM diabetes ({})".format(round(response_prob[0][response[0]],2))
            else:
                message = "O paciente NÃO TEM diabetes ({})".format(round(response_prob[0][response[0]],2))
                
        except Exception as e:
            message = "Tivemos um problema: " + str(e)

    return render_template('diagnostico.html', form=form, message=message)

if __name__ == '__main__':
    app.run(debug=True, port=8001)
