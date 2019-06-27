import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run2_2016_cff import *
era = Run2_2016

def SetLevel1(process):
  process.ctppsBeamParametersESSource.vtxStddevX = 0E-4
  process.ctppsBeamParametersESSource.vtxStddevZ = 0

  process.ctppsBeamParametersESSource.beamDivX45 = 0E-6
  process.ctppsBeamParametersESSource.beamDivX56 = 0E-6
  process.ctppsBeamParametersESSource.beamDivY45 = 0E-6
  process.ctppsBeamParametersESSource.beamDivY56 = 0E-6

  process.ctppsDirectProtonSimulation.roundToPitch = False


def SetLevel2(process):
  process.ctppsBeamParametersESSource.beamDivX45 = 0E-6
  process.ctppsBeamParametersESSource.beamDivX56 = 0E-6
  process.ctppsBeamParametersESSource.beamDivY45 = 0E-6
  process.ctppsBeamParametersESSource.beamDivY56 = 0E-6

  process.ctppsDirectProtonSimulation.roundToPitch = False


def SetLevel3(process):
  process.ctppsDirectProtonSimulation.roundToPitch = False


def SetLevel4(process):
  pass


def SetLowTheta(process):
  process.generator.theta_x_sigma = 0E-6
  process.generator.theta_y_sigma = 0E-6


def SetLargeTheta(process):
  pass


# xangle in murad
def UseCrossingAngle(xangle, process):
  pass

def SetDefaults(process):
  UseCrossingAngle(185, process)
