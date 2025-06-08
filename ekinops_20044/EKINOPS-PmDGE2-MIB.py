# SNMP MIB module (EKINOPS-PmDGE2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ekinops_20044/EKINOPS-PmDGE2-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 12:01:48 2025
# On host e-ws1-mac.muc.elastiflow.net platform Darwin version 24.3.0 by user rob
# Using Python version 3.13.3 (main, Apr  8 2025, 13:54:08) [Clang 16.0.0 (clang-1600.0.26.6)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(EkiApiState,
 EkiMeasureType,
 EkiMode,
 EkiOnOff,
 EkiProtocol,
 EkiState,
 EkiSynchroMode,
 ekinops) = mibBuilder.importSymbols(
    "EKINOPS-MIB",
    "EkiApiState",
    "EkiMeasureType",
    "EkiMode",
    "EkiOnOff",
    "EkiProtocol",
    "EkiState",
    "EkiSynchroMode",
    "ekinops")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

modulepmdge2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 65)
)
if mibBuilder.loadTexts:
    modulepmdge2.setRevisions(
        ("2012-10-16 00:00",
         "2014-07-02 00:00",
         "2014-10-16 00:00",
         "2015-02-23 00:00",
         "2015-09-01 00:00",
         "2016-04-19 00:00",
         "2016-05-23 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Pmdge2Grid(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(50,
              100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("dge2grid50", 50),
          ("dge2grid100", 100),
          ("dge2grid200", 200))
    )



class Pmdge2EqualizerMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dge2off", 0),
          ("dge2auto", 1),
          ("dge2manual", 2))
    )



class Pmdge2EqualizerReference(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dge2refvalue", 0),
          ("dge2reflowest", 1))
    )



class Pmdge2Channel(TextualConvention, Integer32):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_Pmdge2alarms_ObjectIdentity = ObjectIdentity
pmdge2alarms = _Pmdge2alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 65, 2)
)
_Pmdge2AlmOther_ObjectIdentity = ObjectIdentity
pmdge2AlmOther = _Pmdge2AlmOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 65, 2, 1)
)
_Pmdge2AlmOtherNurg_ObjectIdentity = ObjectIdentity
pmdge2AlmOtherNurg = _Pmdge2AlmOtherNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 65, 2, 1, 1)
)
_Pmdge2AlmswitchDegrade_ObjectIdentity = ObjectIdentity
pmdge2AlmswitchDegrade = _Pmdge2AlmswitchDegrade_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 65, 2, 1, 1, 17)
)
_Pmdge2AlmSwitchTempHighDeg_Type = EkiOnOff
_Pmdge2AlmSwitchTempHighDeg_Object = MibScalar
pmdge2AlmSwitchTempHighDeg = _Pmdge2AlmSwitchTempHighDeg_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 2, 1, 1, 17, 2),
    _Pmdge2AlmSwitchTempHighDeg_Type()
)
pmdge2AlmSwitchTempHighDeg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2AlmSwitchTempHighDeg.setStatus("current")
_Pmdge2AlmequalizationStatus_ObjectIdentity = ObjectIdentity
pmdge2AlmequalizationStatus = _Pmdge2AlmequalizationStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 65, 2, 1, 1, 18)
)
_Pmdge2AlmEqualizationFail_Type = EkiOnOff
_Pmdge2AlmEqualizationFail_Object = MibScalar
pmdge2AlmEqualizationFail = _Pmdge2AlmEqualizationFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 2, 1, 1, 18, 1),
    _Pmdge2AlmEqualizationFail_Type()
)
pmdge2AlmEqualizationFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2AlmEqualizationFail.setStatus("current")
_Pmdge2AlmEqualizationInprogress_Type = EkiOnOff
_Pmdge2AlmEqualizationInprogress_Object = MibScalar
pmdge2AlmEqualizationInprogress = _Pmdge2AlmEqualizationInprogress_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 2, 1, 1, 18, 2),
    _Pmdge2AlmEqualizationInprogress_Type()
)
pmdge2AlmEqualizationInprogress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2AlmEqualizationInprogress.setStatus("current")
_Pmdge2AlmEqualizationComplete_Type = EkiOnOff
_Pmdge2AlmEqualizationComplete_Object = MibScalar
pmdge2AlmEqualizationComplete = _Pmdge2AlmEqualizationComplete_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 2, 1, 1, 18, 3),
    _Pmdge2AlmEqualizationComplete_Type()
)
pmdge2AlmEqualizationComplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2AlmEqualizationComplete.setStatus("current")
_Pmdge2AlmEqualizationOff_Type = EkiOnOff
_Pmdge2AlmEqualizationOff_Object = MibScalar
pmdge2AlmEqualizationOff = _Pmdge2AlmEqualizationOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 2, 1, 1, 18, 4),
    _Pmdge2AlmEqualizationOff_Type()
)
pmdge2AlmEqualizationOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2AlmEqualizationOff.setStatus("current")
_Pmdge2AlmPowerOverRange_Type = EkiOnOff
_Pmdge2AlmPowerOverRange_Object = MibScalar
pmdge2AlmPowerOverRange = _Pmdge2AlmPowerOverRange_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 2, 1, 1, 18, 5),
    _Pmdge2AlmPowerOverRange_Type()
)
pmdge2AlmPowerOverRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2AlmPowerOverRange.setStatus("current")
_Pmdge2AlmAttenuationOverRange_Type = EkiOnOff
_Pmdge2AlmAttenuationOverRange_Object = MibScalar
pmdge2AlmAttenuationOverRange = _Pmdge2AlmAttenuationOverRange_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 2, 1, 1, 18, 6),
    _Pmdge2AlmAttenuationOverRange_Type()
)
pmdge2AlmAttenuationOverRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2AlmAttenuationOverRange.setStatus("current")
_Pmdge2AlmLossOfSpectrum_Type = EkiOnOff
_Pmdge2AlmLossOfSpectrum_Object = MibScalar
pmdge2AlmLossOfSpectrum = _Pmdge2AlmLossOfSpectrum_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 2, 1, 1, 18, 7),
    _Pmdge2AlmLossOfSpectrum_Type()
)
pmdge2AlmLossOfSpectrum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2AlmLossOfSpectrum.setStatus("current")
_Pmdge2AlmOtherUrg_ObjectIdentity = ObjectIdentity
pmdge2AlmOtherUrg = _Pmdge2AlmOtherUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 65, 2, 1, 2)
)
_Pmdge2AlmswitchAlarms_ObjectIdentity = ObjectIdentity
pmdge2AlmswitchAlarms = _Pmdge2AlmswitchAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 65, 2, 1, 2, 16)
)
_Pmdge2AlmSwitchTempHighAla_Type = EkiOnOff
_Pmdge2AlmSwitchTempHighAla_Object = MibScalar
pmdge2AlmSwitchTempHighAla = _Pmdge2AlmSwitchTempHighAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 2, 1, 2, 16, 2),
    _Pmdge2AlmSwitchTempHighAla_Type()
)
pmdge2AlmSwitchTempHighAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2AlmSwitchTempHighAla.setStatus("current")
_Pmdge2AlmmoduleStatus_ObjectIdentity = ObjectIdentity
pmdge2AlmmoduleStatus = _Pmdge2AlmmoduleStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 65, 2, 1, 2, 66)
)
_Pmdge2AlmSwitchNotReady_Type = EkiOnOff
_Pmdge2AlmSwitchNotReady_Object = MibScalar
pmdge2AlmSwitchNotReady = _Pmdge2AlmSwitchNotReady_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 2, 1, 2, 66, 5),
    _Pmdge2AlmSwitchNotReady_Type()
)
pmdge2AlmSwitchNotReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2AlmSwitchNotReady.setStatus("current")
_Pmdge2AlmmoduleAlarms_ObjectIdentity = ObjectIdentity
pmdge2AlmmoduleAlarms = _Pmdge2AlmmoduleAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 65, 2, 1, 2, 67)
)
_Pmdge2AlmModuleTempHighAla_Type = EkiOnOff
_Pmdge2AlmModuleTempHighAla_Object = MibScalar
pmdge2AlmModuleTempHighAla = _Pmdge2AlmModuleTempHighAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 2, 1, 2, 67, 2),
    _Pmdge2AlmModuleTempHighAla_Type()
)
pmdge2AlmModuleTempHighAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2AlmModuleTempHighAla.setStatus("current")
_Pmdge2AlmCaseTempHighAla_Type = EkiOnOff
_Pmdge2AlmCaseTempHighAla_Object = MibScalar
pmdge2AlmCaseTempHighAla = _Pmdge2AlmCaseTempHighAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 2, 1, 2, 67, 4),
    _Pmdge2AlmCaseTempHighAla_Type()
)
pmdge2AlmCaseTempHighAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2AlmCaseTempHighAla.setStatus("current")
_Pmdge2AlmmoduleDegrad_ObjectIdentity = ObjectIdentity
pmdge2AlmmoduleDegrad = _Pmdge2AlmmoduleDegrad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 65, 2, 1, 2, 68)
)
_Pmdge2AlmModuleTempHighDeg_Type = EkiOnOff
_Pmdge2AlmModuleTempHighDeg_Object = MibScalar
pmdge2AlmModuleTempHighDeg = _Pmdge2AlmModuleTempHighDeg_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 2, 1, 2, 68, 2),
    _Pmdge2AlmModuleTempHighDeg_Type()
)
pmdge2AlmModuleTempHighDeg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2AlmModuleTempHighDeg.setStatus("current")
_Pmdge2AlmCaseTempHighDeg_Type = EkiOnOff
_Pmdge2AlmCaseTempHighDeg_Object = MibScalar
pmdge2AlmCaseTempHighDeg = _Pmdge2AlmCaseTempHighDeg_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 2, 1, 2, 68, 4),
    _Pmdge2AlmCaseTempHighDeg_Type()
)
pmdge2AlmCaseTempHighDeg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2AlmCaseTempHighDeg.setStatus("current")
_Pmdge2AlmOtherCrit_ObjectIdentity = ObjectIdentity
pmdge2AlmOtherCrit = _Pmdge2AlmOtherCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 65, 2, 1, 3)
)
_Pmdge2AlmsynthAlm0_ObjectIdentity = ObjectIdentity
pmdge2AlmsynthAlm0 = _Pmdge2AlmsynthAlm0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 65, 2, 1, 3, 0)
)
_Pmdge2AlmModuleGlobFailure_Type = EkiOnOff
_Pmdge2AlmModuleGlobFailure_Object = MibScalar
pmdge2AlmModuleGlobFailure = _Pmdge2AlmModuleGlobFailure_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 2, 1, 3, 0, 9),
    _Pmdge2AlmModuleGlobFailure_Type()
)
pmdge2AlmModuleGlobFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2AlmModuleGlobFailure.setStatus("current")
_Pmdge2AlmDefFuseA_Type = EkiOnOff
_Pmdge2AlmDefFuseA_Object = MibScalar
pmdge2AlmDefFuseA = _Pmdge2AlmDefFuseA_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 2, 1, 3, 0, 15),
    _Pmdge2AlmDefFuseA_Type()
)
pmdge2AlmDefFuseA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2AlmDefFuseA.setStatus("current")
_Pmdge2AlmDefFuseB_Type = EkiOnOff
_Pmdge2AlmDefFuseB_Object = MibScalar
pmdge2AlmDefFuseB = _Pmdge2AlmDefFuseB_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 2, 1, 3, 0, 16),
    _Pmdge2AlmDefFuseB_Type()
)
pmdge2AlmDefFuseB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2AlmDefFuseB.setStatus("current")
_Pmdge2AlmsynthAlm7_ObjectIdentity = ObjectIdentity
pmdge2AlmsynthAlm7 = _Pmdge2AlmsynthAlm7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 65, 2, 1, 3, 7)
)
_Pmdge2AlmInitNotCompl_Type = EkiOnOff
_Pmdge2AlmInitNotCompl_Object = MibScalar
pmdge2AlmInitNotCompl = _Pmdge2AlmInitNotCompl_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 2, 1, 3, 7, 2),
    _Pmdge2AlmInitNotCompl_Type()
)
pmdge2AlmInitNotCompl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2AlmInitNotCompl.setStatus("current")
_Pmdge2AlmSwitchDegrade_Type = EkiOnOff
_Pmdge2AlmSwitchDegrade_Object = MibScalar
pmdge2AlmSwitchDegrade = _Pmdge2AlmSwitchDegrade_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 2, 1, 3, 7, 9),
    _Pmdge2AlmSwitchDegrade_Type()
)
pmdge2AlmSwitchDegrade.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2AlmSwitchDegrade.setStatus("current")
_Pmdge2AlmSwitchAlm_Type = EkiOnOff
_Pmdge2AlmSwitchAlm_Object = MibScalar
pmdge2AlmSwitchAlm = _Pmdge2AlmSwitchAlm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 2, 1, 3, 7, 10),
    _Pmdge2AlmSwitchAlm_Type()
)
pmdge2AlmSwitchAlm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2AlmSwitchAlm.setStatus("current")
_Pmdge2measures_ObjectIdentity = ObjectIdentity
pmdge2measures = _Pmdge2measures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3)
)
_Pmdge2MesrOther_ObjectIdentity = ObjectIdentity
pmdge2MesrOther = _Pmdge2MesrOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1)
)


class _Pmdge2MesrswitchTemp_Type(Unsigned32):
    """Custom type pmdge2MesrswitchTemp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2MesrswitchTemp_Type.__name__ = "Unsigned32"
_Pmdge2MesrswitchTemp_Object = MibScalar
pmdge2MesrswitchTemp = _Pmdge2MesrswitchTemp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 16),
    _Pmdge2MesrswitchTemp_Type()
)
pmdge2MesrswitchTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2MesrswitchTemp.setStatus("current")


class _Pmdge2MesrchannelLowestPowerValue_Type(Unsigned32):
    """Custom type pmdge2MesrchannelLowestPowerValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2MesrchannelLowestPowerValue_Type.__name__ = "Unsigned32"
_Pmdge2MesrchannelLowestPowerValue_Object = MibScalar
pmdge2MesrchannelLowestPowerValue = _Pmdge2MesrchannelLowestPowerValue_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 17),
    _Pmdge2MesrchannelLowestPowerValue_Type()
)
pmdge2MesrchannelLowestPowerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2MesrchannelLowestPowerValue.setStatus("current")


class _Pmdge2MesrchannelNumber_Type(Unsigned32):
    """Custom type pmdge2MesrchannelNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2MesrchannelNumber_Type.__name__ = "Unsigned32"
_Pmdge2MesrchannelNumber_Object = MibScalar
pmdge2MesrchannelNumber = _Pmdge2MesrchannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 18),
    _Pmdge2MesrchannelNumber_Type()
)
pmdge2MesrchannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2MesrchannelNumber.setStatus("current")


class _Pmdge2MesrmoduleTemp_Type(Unsigned32):
    """Custom type pmdge2MesrmoduleTemp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2MesrmoduleTemp_Type.__name__ = "Unsigned32"
_Pmdge2MesrmoduleTemp_Object = MibScalar
pmdge2MesrmoduleTemp = _Pmdge2MesrmoduleTemp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 64),
    _Pmdge2MesrmoduleTemp_Type()
)
pmdge2MesrmoduleTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2MesrmoduleTemp.setStatus("current")


class _Pmdge2MesrtargetRequest_Type(Unsigned32):
    """Custom type pmdge2MesrtargetRequest based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2MesrtargetRequest_Type.__name__ = "Unsigned32"
_Pmdge2MesrtargetRequest_Object = MibScalar
pmdge2MesrtargetRequest = _Pmdge2MesrtargetRequest_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 65),
    _Pmdge2MesrtargetRequest_Type()
)
pmdge2MesrtargetRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2MesrtargetRequest.setStatus("current")


class _Pmdge2MesrchannelPresenceThreshold_Type(Unsigned32):
    """Custom type pmdge2MesrchannelPresenceThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2MesrchannelPresenceThreshold_Type.__name__ = "Unsigned32"
_Pmdge2MesrchannelPresenceThreshold_Object = MibScalar
pmdge2MesrchannelPresenceThreshold = _Pmdge2MesrchannelPresenceThreshold_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 66),
    _Pmdge2MesrchannelPresenceThreshold_Type()
)
pmdge2MesrchannelPresenceThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2MesrchannelPresenceThreshold.setStatus("current")


class _Pmdge2Mesrchannel1InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel1InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel1InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel1InputPwr_Object = MibScalar
pmdge2Mesrchannel1InputPwr = _Pmdge2Mesrchannel1InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 72),
    _Pmdge2Mesrchannel1InputPwr_Type()
)
pmdge2Mesrchannel1InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel1InputPwr.setStatus("current")


class _Pmdge2Mesrchannel2InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel2InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel2InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel2InputPwr_Object = MibScalar
pmdge2Mesrchannel2InputPwr = _Pmdge2Mesrchannel2InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 73),
    _Pmdge2Mesrchannel2InputPwr_Type()
)
pmdge2Mesrchannel2InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel2InputPwr.setStatus("current")


class _Pmdge2Mesrchannel3InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel3InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel3InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel3InputPwr_Object = MibScalar
pmdge2Mesrchannel3InputPwr = _Pmdge2Mesrchannel3InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 74),
    _Pmdge2Mesrchannel3InputPwr_Type()
)
pmdge2Mesrchannel3InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel3InputPwr.setStatus("current")


class _Pmdge2Mesrchannel4InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel4InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel4InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel4InputPwr_Object = MibScalar
pmdge2Mesrchannel4InputPwr = _Pmdge2Mesrchannel4InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 75),
    _Pmdge2Mesrchannel4InputPwr_Type()
)
pmdge2Mesrchannel4InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel4InputPwr.setStatus("current")


class _Pmdge2Mesrchannel5InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel5InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel5InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel5InputPwr_Object = MibScalar
pmdge2Mesrchannel5InputPwr = _Pmdge2Mesrchannel5InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 76),
    _Pmdge2Mesrchannel5InputPwr_Type()
)
pmdge2Mesrchannel5InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel5InputPwr.setStatus("current")


class _Pmdge2Mesrchannel6InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel6InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel6InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel6InputPwr_Object = MibScalar
pmdge2Mesrchannel6InputPwr = _Pmdge2Mesrchannel6InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 77),
    _Pmdge2Mesrchannel6InputPwr_Type()
)
pmdge2Mesrchannel6InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel6InputPwr.setStatus("current")


class _Pmdge2Mesrchannel7InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel7InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel7InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel7InputPwr_Object = MibScalar
pmdge2Mesrchannel7InputPwr = _Pmdge2Mesrchannel7InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 78),
    _Pmdge2Mesrchannel7InputPwr_Type()
)
pmdge2Mesrchannel7InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel7InputPwr.setStatus("current")


class _Pmdge2Mesrchannel8InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel8InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel8InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel8InputPwr_Object = MibScalar
pmdge2Mesrchannel8InputPwr = _Pmdge2Mesrchannel8InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 79),
    _Pmdge2Mesrchannel8InputPwr_Type()
)
pmdge2Mesrchannel8InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel8InputPwr.setStatus("current")


class _Pmdge2Mesrchannel9InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel9InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel9InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel9InputPwr_Object = MibScalar
pmdge2Mesrchannel9InputPwr = _Pmdge2Mesrchannel9InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 80),
    _Pmdge2Mesrchannel9InputPwr_Type()
)
pmdge2Mesrchannel9InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel9InputPwr.setStatus("current")


class _Pmdge2Mesrchannel10InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel10InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel10InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel10InputPwr_Object = MibScalar
pmdge2Mesrchannel10InputPwr = _Pmdge2Mesrchannel10InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 81),
    _Pmdge2Mesrchannel10InputPwr_Type()
)
pmdge2Mesrchannel10InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel10InputPwr.setStatus("current")


class _Pmdge2Mesrchannel11InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel11InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel11InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel11InputPwr_Object = MibScalar
pmdge2Mesrchannel11InputPwr = _Pmdge2Mesrchannel11InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 82),
    _Pmdge2Mesrchannel11InputPwr_Type()
)
pmdge2Mesrchannel11InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel11InputPwr.setStatus("current")


class _Pmdge2Mesrchannel12InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel12InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel12InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel12InputPwr_Object = MibScalar
pmdge2Mesrchannel12InputPwr = _Pmdge2Mesrchannel12InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 83),
    _Pmdge2Mesrchannel12InputPwr_Type()
)
pmdge2Mesrchannel12InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel12InputPwr.setStatus("current")


class _Pmdge2Mesrchannel13InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel13InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel13InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel13InputPwr_Object = MibScalar
pmdge2Mesrchannel13InputPwr = _Pmdge2Mesrchannel13InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 84),
    _Pmdge2Mesrchannel13InputPwr_Type()
)
pmdge2Mesrchannel13InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel13InputPwr.setStatus("current")


class _Pmdge2Mesrchannel14InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel14InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel14InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel14InputPwr_Object = MibScalar
pmdge2Mesrchannel14InputPwr = _Pmdge2Mesrchannel14InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 85),
    _Pmdge2Mesrchannel14InputPwr_Type()
)
pmdge2Mesrchannel14InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel14InputPwr.setStatus("current")


class _Pmdge2Mesrchannel15InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel15InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel15InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel15InputPwr_Object = MibScalar
pmdge2Mesrchannel15InputPwr = _Pmdge2Mesrchannel15InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 86),
    _Pmdge2Mesrchannel15InputPwr_Type()
)
pmdge2Mesrchannel15InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel15InputPwr.setStatus("current")


class _Pmdge2Mesrchannel16InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel16InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel16InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel16InputPwr_Object = MibScalar
pmdge2Mesrchannel16InputPwr = _Pmdge2Mesrchannel16InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 87),
    _Pmdge2Mesrchannel16InputPwr_Type()
)
pmdge2Mesrchannel16InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel16InputPwr.setStatus("current")


class _Pmdge2Mesrchannel17InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel17InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel17InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel17InputPwr_Object = MibScalar
pmdge2Mesrchannel17InputPwr = _Pmdge2Mesrchannel17InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 88),
    _Pmdge2Mesrchannel17InputPwr_Type()
)
pmdge2Mesrchannel17InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel17InputPwr.setStatus("current")


class _Pmdge2Mesrchannel18InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel18InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel18InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel18InputPwr_Object = MibScalar
pmdge2Mesrchannel18InputPwr = _Pmdge2Mesrchannel18InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 89),
    _Pmdge2Mesrchannel18InputPwr_Type()
)
pmdge2Mesrchannel18InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel18InputPwr.setStatus("current")


class _Pmdge2Mesrchannel19InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel19InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel19InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel19InputPwr_Object = MibScalar
pmdge2Mesrchannel19InputPwr = _Pmdge2Mesrchannel19InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 90),
    _Pmdge2Mesrchannel19InputPwr_Type()
)
pmdge2Mesrchannel19InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel19InputPwr.setStatus("current")


class _Pmdge2Mesrchannel20InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel20InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel20InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel20InputPwr_Object = MibScalar
pmdge2Mesrchannel20InputPwr = _Pmdge2Mesrchannel20InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 91),
    _Pmdge2Mesrchannel20InputPwr_Type()
)
pmdge2Mesrchannel20InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel20InputPwr.setStatus("current")


class _Pmdge2Mesrchannel21InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel21InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel21InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel21InputPwr_Object = MibScalar
pmdge2Mesrchannel21InputPwr = _Pmdge2Mesrchannel21InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 92),
    _Pmdge2Mesrchannel21InputPwr_Type()
)
pmdge2Mesrchannel21InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel21InputPwr.setStatus("current")


class _Pmdge2Mesrchannel22InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel22InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel22InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel22InputPwr_Object = MibScalar
pmdge2Mesrchannel22InputPwr = _Pmdge2Mesrchannel22InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 93),
    _Pmdge2Mesrchannel22InputPwr_Type()
)
pmdge2Mesrchannel22InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel22InputPwr.setStatus("current")


class _Pmdge2Mesrchannel23InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel23InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel23InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel23InputPwr_Object = MibScalar
pmdge2Mesrchannel23InputPwr = _Pmdge2Mesrchannel23InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 94),
    _Pmdge2Mesrchannel23InputPwr_Type()
)
pmdge2Mesrchannel23InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel23InputPwr.setStatus("current")


class _Pmdge2Mesrchannel24InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel24InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel24InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel24InputPwr_Object = MibScalar
pmdge2Mesrchannel24InputPwr = _Pmdge2Mesrchannel24InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 95),
    _Pmdge2Mesrchannel24InputPwr_Type()
)
pmdge2Mesrchannel24InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel24InputPwr.setStatus("current")


class _Pmdge2Mesrchannel25InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel25InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel25InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel25InputPwr_Object = MibScalar
pmdge2Mesrchannel25InputPwr = _Pmdge2Mesrchannel25InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 96),
    _Pmdge2Mesrchannel25InputPwr_Type()
)
pmdge2Mesrchannel25InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel25InputPwr.setStatus("current")


class _Pmdge2Mesrchannel26InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel26InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel26InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel26InputPwr_Object = MibScalar
pmdge2Mesrchannel26InputPwr = _Pmdge2Mesrchannel26InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 97),
    _Pmdge2Mesrchannel26InputPwr_Type()
)
pmdge2Mesrchannel26InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel26InputPwr.setStatus("current")


class _Pmdge2Mesrchannel27InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel27InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel27InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel27InputPwr_Object = MibScalar
pmdge2Mesrchannel27InputPwr = _Pmdge2Mesrchannel27InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 98),
    _Pmdge2Mesrchannel27InputPwr_Type()
)
pmdge2Mesrchannel27InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel27InputPwr.setStatus("current")


class _Pmdge2Mesrchannel28InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel28InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel28InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel28InputPwr_Object = MibScalar
pmdge2Mesrchannel28InputPwr = _Pmdge2Mesrchannel28InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 99),
    _Pmdge2Mesrchannel28InputPwr_Type()
)
pmdge2Mesrchannel28InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel28InputPwr.setStatus("current")


class _Pmdge2Mesrchannel29InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel29InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel29InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel29InputPwr_Object = MibScalar
pmdge2Mesrchannel29InputPwr = _Pmdge2Mesrchannel29InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 100),
    _Pmdge2Mesrchannel29InputPwr_Type()
)
pmdge2Mesrchannel29InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel29InputPwr.setStatus("current")


class _Pmdge2Mesrchannel30InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel30InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel30InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel30InputPwr_Object = MibScalar
pmdge2Mesrchannel30InputPwr = _Pmdge2Mesrchannel30InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 101),
    _Pmdge2Mesrchannel30InputPwr_Type()
)
pmdge2Mesrchannel30InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel30InputPwr.setStatus("current")


class _Pmdge2Mesrchannel31InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel31InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel31InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel31InputPwr_Object = MibScalar
pmdge2Mesrchannel31InputPwr = _Pmdge2Mesrchannel31InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 102),
    _Pmdge2Mesrchannel31InputPwr_Type()
)
pmdge2Mesrchannel31InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel31InputPwr.setStatus("current")


class _Pmdge2Mesrchannel32InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel32InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel32InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel32InputPwr_Object = MibScalar
pmdge2Mesrchannel32InputPwr = _Pmdge2Mesrchannel32InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 103),
    _Pmdge2Mesrchannel32InputPwr_Type()
)
pmdge2Mesrchannel32InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel32InputPwr.setStatus("current")


class _Pmdge2Mesrchannel33InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel33InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel33InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel33InputPwr_Object = MibScalar
pmdge2Mesrchannel33InputPwr = _Pmdge2Mesrchannel33InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 104),
    _Pmdge2Mesrchannel33InputPwr_Type()
)
pmdge2Mesrchannel33InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel33InputPwr.setStatus("current")


class _Pmdge2Mesrchannel34InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel34InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel34InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel34InputPwr_Object = MibScalar
pmdge2Mesrchannel34InputPwr = _Pmdge2Mesrchannel34InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 105),
    _Pmdge2Mesrchannel34InputPwr_Type()
)
pmdge2Mesrchannel34InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel34InputPwr.setStatus("current")


class _Pmdge2Mesrchannel35InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel35InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel35InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel35InputPwr_Object = MibScalar
pmdge2Mesrchannel35InputPwr = _Pmdge2Mesrchannel35InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 106),
    _Pmdge2Mesrchannel35InputPwr_Type()
)
pmdge2Mesrchannel35InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel35InputPwr.setStatus("current")


class _Pmdge2Mesrchannel36InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel36InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel36InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel36InputPwr_Object = MibScalar
pmdge2Mesrchannel36InputPwr = _Pmdge2Mesrchannel36InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 107),
    _Pmdge2Mesrchannel36InputPwr_Type()
)
pmdge2Mesrchannel36InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel36InputPwr.setStatus("current")


class _Pmdge2Mesrchannel37InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel37InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel37InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel37InputPwr_Object = MibScalar
pmdge2Mesrchannel37InputPwr = _Pmdge2Mesrchannel37InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 108),
    _Pmdge2Mesrchannel37InputPwr_Type()
)
pmdge2Mesrchannel37InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel37InputPwr.setStatus("current")


class _Pmdge2Mesrchannel38InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel38InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel38InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel38InputPwr_Object = MibScalar
pmdge2Mesrchannel38InputPwr = _Pmdge2Mesrchannel38InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 109),
    _Pmdge2Mesrchannel38InputPwr_Type()
)
pmdge2Mesrchannel38InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel38InputPwr.setStatus("current")


class _Pmdge2Mesrchannel39InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel39InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel39InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel39InputPwr_Object = MibScalar
pmdge2Mesrchannel39InputPwr = _Pmdge2Mesrchannel39InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 110),
    _Pmdge2Mesrchannel39InputPwr_Type()
)
pmdge2Mesrchannel39InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel39InputPwr.setStatus("current")


class _Pmdge2Mesrchannel40InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel40InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel40InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel40InputPwr_Object = MibScalar
pmdge2Mesrchannel40InputPwr = _Pmdge2Mesrchannel40InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 111),
    _Pmdge2Mesrchannel40InputPwr_Type()
)
pmdge2Mesrchannel40InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel40InputPwr.setStatus("current")


class _Pmdge2Mesrchannel41InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel41InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel41InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel41InputPwr_Object = MibScalar
pmdge2Mesrchannel41InputPwr = _Pmdge2Mesrchannel41InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 112),
    _Pmdge2Mesrchannel41InputPwr_Type()
)
pmdge2Mesrchannel41InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel41InputPwr.setStatus("current")


class _Pmdge2Mesrchannel42InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel42InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel42InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel42InputPwr_Object = MibScalar
pmdge2Mesrchannel42InputPwr = _Pmdge2Mesrchannel42InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 113),
    _Pmdge2Mesrchannel42InputPwr_Type()
)
pmdge2Mesrchannel42InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel42InputPwr.setStatus("current")


class _Pmdge2Mesrchannel43InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel43InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel43InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel43InputPwr_Object = MibScalar
pmdge2Mesrchannel43InputPwr = _Pmdge2Mesrchannel43InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 114),
    _Pmdge2Mesrchannel43InputPwr_Type()
)
pmdge2Mesrchannel43InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel43InputPwr.setStatus("current")


class _Pmdge2Mesrchannel44InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel44InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel44InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel44InputPwr_Object = MibScalar
pmdge2Mesrchannel44InputPwr = _Pmdge2Mesrchannel44InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 115),
    _Pmdge2Mesrchannel44InputPwr_Type()
)
pmdge2Mesrchannel44InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel44InputPwr.setStatus("current")


class _Pmdge2Mesrchannel45InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel45InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel45InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel45InputPwr_Object = MibScalar
pmdge2Mesrchannel45InputPwr = _Pmdge2Mesrchannel45InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 116),
    _Pmdge2Mesrchannel45InputPwr_Type()
)
pmdge2Mesrchannel45InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel45InputPwr.setStatus("current")


class _Pmdge2Mesrchannel46InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel46InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel46InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel46InputPwr_Object = MibScalar
pmdge2Mesrchannel46InputPwr = _Pmdge2Mesrchannel46InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 117),
    _Pmdge2Mesrchannel46InputPwr_Type()
)
pmdge2Mesrchannel46InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel46InputPwr.setStatus("current")


class _Pmdge2Mesrchannel47InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel47InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel47InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel47InputPwr_Object = MibScalar
pmdge2Mesrchannel47InputPwr = _Pmdge2Mesrchannel47InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 118),
    _Pmdge2Mesrchannel47InputPwr_Type()
)
pmdge2Mesrchannel47InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel47InputPwr.setStatus("current")


class _Pmdge2Mesrchannel48InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel48InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel48InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel48InputPwr_Object = MibScalar
pmdge2Mesrchannel48InputPwr = _Pmdge2Mesrchannel48InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 119),
    _Pmdge2Mesrchannel48InputPwr_Type()
)
pmdge2Mesrchannel48InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel48InputPwr.setStatus("current")


class _Pmdge2Mesrchannel49InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel49InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel49InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel49InputPwr_Object = MibScalar
pmdge2Mesrchannel49InputPwr = _Pmdge2Mesrchannel49InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 120),
    _Pmdge2Mesrchannel49InputPwr_Type()
)
pmdge2Mesrchannel49InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel49InputPwr.setStatus("current")


class _Pmdge2Mesrchannel50InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel50InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel50InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel50InputPwr_Object = MibScalar
pmdge2Mesrchannel50InputPwr = _Pmdge2Mesrchannel50InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 121),
    _Pmdge2Mesrchannel50InputPwr_Type()
)
pmdge2Mesrchannel50InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel50InputPwr.setStatus("current")


class _Pmdge2Mesrchannel51InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel51InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel51InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel51InputPwr_Object = MibScalar
pmdge2Mesrchannel51InputPwr = _Pmdge2Mesrchannel51InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 122),
    _Pmdge2Mesrchannel51InputPwr_Type()
)
pmdge2Mesrchannel51InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel51InputPwr.setStatus("current")


class _Pmdge2Mesrchannel52InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel52InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel52InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel52InputPwr_Object = MibScalar
pmdge2Mesrchannel52InputPwr = _Pmdge2Mesrchannel52InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 123),
    _Pmdge2Mesrchannel52InputPwr_Type()
)
pmdge2Mesrchannel52InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel52InputPwr.setStatus("current")


class _Pmdge2Mesrchannel53InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel53InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel53InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel53InputPwr_Object = MibScalar
pmdge2Mesrchannel53InputPwr = _Pmdge2Mesrchannel53InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 124),
    _Pmdge2Mesrchannel53InputPwr_Type()
)
pmdge2Mesrchannel53InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel53InputPwr.setStatus("current")


class _Pmdge2Mesrchannel54InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel54InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel54InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel54InputPwr_Object = MibScalar
pmdge2Mesrchannel54InputPwr = _Pmdge2Mesrchannel54InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 125),
    _Pmdge2Mesrchannel54InputPwr_Type()
)
pmdge2Mesrchannel54InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel54InputPwr.setStatus("current")


class _Pmdge2Mesrchannel55InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel55InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel55InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel55InputPwr_Object = MibScalar
pmdge2Mesrchannel55InputPwr = _Pmdge2Mesrchannel55InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 126),
    _Pmdge2Mesrchannel55InputPwr_Type()
)
pmdge2Mesrchannel55InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel55InputPwr.setStatus("current")


class _Pmdge2Mesrchannel56InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel56InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel56InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel56InputPwr_Object = MibScalar
pmdge2Mesrchannel56InputPwr = _Pmdge2Mesrchannel56InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 127),
    _Pmdge2Mesrchannel56InputPwr_Type()
)
pmdge2Mesrchannel56InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel56InputPwr.setStatus("current")


class _Pmdge2Mesrchannel57InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel57InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel57InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel57InputPwr_Object = MibScalar
pmdge2Mesrchannel57InputPwr = _Pmdge2Mesrchannel57InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 128),
    _Pmdge2Mesrchannel57InputPwr_Type()
)
pmdge2Mesrchannel57InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel57InputPwr.setStatus("current")


class _Pmdge2Mesrchannel58InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel58InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel58InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel58InputPwr_Object = MibScalar
pmdge2Mesrchannel58InputPwr = _Pmdge2Mesrchannel58InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 129),
    _Pmdge2Mesrchannel58InputPwr_Type()
)
pmdge2Mesrchannel58InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel58InputPwr.setStatus("current")


class _Pmdge2Mesrchannel59InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel59InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel59InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel59InputPwr_Object = MibScalar
pmdge2Mesrchannel59InputPwr = _Pmdge2Mesrchannel59InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 130),
    _Pmdge2Mesrchannel59InputPwr_Type()
)
pmdge2Mesrchannel59InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel59InputPwr.setStatus("current")


class _Pmdge2Mesrchannel60InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel60InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel60InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel60InputPwr_Object = MibScalar
pmdge2Mesrchannel60InputPwr = _Pmdge2Mesrchannel60InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 131),
    _Pmdge2Mesrchannel60InputPwr_Type()
)
pmdge2Mesrchannel60InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel60InputPwr.setStatus("current")


class _Pmdge2Mesrchannel61InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel61InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel61InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel61InputPwr_Object = MibScalar
pmdge2Mesrchannel61InputPwr = _Pmdge2Mesrchannel61InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 132),
    _Pmdge2Mesrchannel61InputPwr_Type()
)
pmdge2Mesrchannel61InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel61InputPwr.setStatus("current")


class _Pmdge2Mesrchannel62InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel62InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel62InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel62InputPwr_Object = MibScalar
pmdge2Mesrchannel62InputPwr = _Pmdge2Mesrchannel62InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 133),
    _Pmdge2Mesrchannel62InputPwr_Type()
)
pmdge2Mesrchannel62InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel62InputPwr.setStatus("current")


class _Pmdge2Mesrchannel63InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel63InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel63InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel63InputPwr_Object = MibScalar
pmdge2Mesrchannel63InputPwr = _Pmdge2Mesrchannel63InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 134),
    _Pmdge2Mesrchannel63InputPwr_Type()
)
pmdge2Mesrchannel63InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel63InputPwr.setStatus("current")


class _Pmdge2Mesrchannel64InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel64InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel64InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel64InputPwr_Object = MibScalar
pmdge2Mesrchannel64InputPwr = _Pmdge2Mesrchannel64InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 135),
    _Pmdge2Mesrchannel64InputPwr_Type()
)
pmdge2Mesrchannel64InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel64InputPwr.setStatus("current")


class _Pmdge2Mesrchannel65InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel65InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel65InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel65InputPwr_Object = MibScalar
pmdge2Mesrchannel65InputPwr = _Pmdge2Mesrchannel65InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 136),
    _Pmdge2Mesrchannel65InputPwr_Type()
)
pmdge2Mesrchannel65InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel65InputPwr.setStatus("current")


class _Pmdge2Mesrchannel66InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel66InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel66InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel66InputPwr_Object = MibScalar
pmdge2Mesrchannel66InputPwr = _Pmdge2Mesrchannel66InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 137),
    _Pmdge2Mesrchannel66InputPwr_Type()
)
pmdge2Mesrchannel66InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel66InputPwr.setStatus("current")


class _Pmdge2Mesrchannel67InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel67InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel67InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel67InputPwr_Object = MibScalar
pmdge2Mesrchannel67InputPwr = _Pmdge2Mesrchannel67InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 138),
    _Pmdge2Mesrchannel67InputPwr_Type()
)
pmdge2Mesrchannel67InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel67InputPwr.setStatus("current")


class _Pmdge2Mesrchannel68InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel68InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel68InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel68InputPwr_Object = MibScalar
pmdge2Mesrchannel68InputPwr = _Pmdge2Mesrchannel68InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 139),
    _Pmdge2Mesrchannel68InputPwr_Type()
)
pmdge2Mesrchannel68InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel68InputPwr.setStatus("current")


class _Pmdge2Mesrchannel69InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel69InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel69InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel69InputPwr_Object = MibScalar
pmdge2Mesrchannel69InputPwr = _Pmdge2Mesrchannel69InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 140),
    _Pmdge2Mesrchannel69InputPwr_Type()
)
pmdge2Mesrchannel69InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel69InputPwr.setStatus("current")


class _Pmdge2Mesrchannel70InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel70InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel70InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel70InputPwr_Object = MibScalar
pmdge2Mesrchannel70InputPwr = _Pmdge2Mesrchannel70InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 141),
    _Pmdge2Mesrchannel70InputPwr_Type()
)
pmdge2Mesrchannel70InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel70InputPwr.setStatus("current")


class _Pmdge2Mesrchannel71InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel71InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel71InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel71InputPwr_Object = MibScalar
pmdge2Mesrchannel71InputPwr = _Pmdge2Mesrchannel71InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 142),
    _Pmdge2Mesrchannel71InputPwr_Type()
)
pmdge2Mesrchannel71InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel71InputPwr.setStatus("current")


class _Pmdge2Mesrchannel72InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel72InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel72InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel72InputPwr_Object = MibScalar
pmdge2Mesrchannel72InputPwr = _Pmdge2Mesrchannel72InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 143),
    _Pmdge2Mesrchannel72InputPwr_Type()
)
pmdge2Mesrchannel72InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel72InputPwr.setStatus("current")


class _Pmdge2Mesrchannel73InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel73InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel73InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel73InputPwr_Object = MibScalar
pmdge2Mesrchannel73InputPwr = _Pmdge2Mesrchannel73InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 144),
    _Pmdge2Mesrchannel73InputPwr_Type()
)
pmdge2Mesrchannel73InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel73InputPwr.setStatus("current")


class _Pmdge2Mesrchannel74InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel74InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel74InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel74InputPwr_Object = MibScalar
pmdge2Mesrchannel74InputPwr = _Pmdge2Mesrchannel74InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 145),
    _Pmdge2Mesrchannel74InputPwr_Type()
)
pmdge2Mesrchannel74InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel74InputPwr.setStatus("current")


class _Pmdge2Mesrchannel75InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel75InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel75InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel75InputPwr_Object = MibScalar
pmdge2Mesrchannel75InputPwr = _Pmdge2Mesrchannel75InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 146),
    _Pmdge2Mesrchannel75InputPwr_Type()
)
pmdge2Mesrchannel75InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel75InputPwr.setStatus("current")


class _Pmdge2Mesrchannel76InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel76InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel76InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel76InputPwr_Object = MibScalar
pmdge2Mesrchannel76InputPwr = _Pmdge2Mesrchannel76InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 147),
    _Pmdge2Mesrchannel76InputPwr_Type()
)
pmdge2Mesrchannel76InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel76InputPwr.setStatus("current")


class _Pmdge2Mesrchannel77InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel77InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel77InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel77InputPwr_Object = MibScalar
pmdge2Mesrchannel77InputPwr = _Pmdge2Mesrchannel77InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 148),
    _Pmdge2Mesrchannel77InputPwr_Type()
)
pmdge2Mesrchannel77InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel77InputPwr.setStatus("current")


class _Pmdge2Mesrchannel78InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel78InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel78InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel78InputPwr_Object = MibScalar
pmdge2Mesrchannel78InputPwr = _Pmdge2Mesrchannel78InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 149),
    _Pmdge2Mesrchannel78InputPwr_Type()
)
pmdge2Mesrchannel78InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel78InputPwr.setStatus("current")


class _Pmdge2Mesrchannel79InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel79InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel79InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel79InputPwr_Object = MibScalar
pmdge2Mesrchannel79InputPwr = _Pmdge2Mesrchannel79InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 150),
    _Pmdge2Mesrchannel79InputPwr_Type()
)
pmdge2Mesrchannel79InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel79InputPwr.setStatus("current")


class _Pmdge2Mesrchannel80InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel80InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel80InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel80InputPwr_Object = MibScalar
pmdge2Mesrchannel80InputPwr = _Pmdge2Mesrchannel80InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 151),
    _Pmdge2Mesrchannel80InputPwr_Type()
)
pmdge2Mesrchannel80InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel80InputPwr.setStatus("current")


class _Pmdge2Mesrchannel81InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel81InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel81InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel81InputPwr_Object = MibScalar
pmdge2Mesrchannel81InputPwr = _Pmdge2Mesrchannel81InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 152),
    _Pmdge2Mesrchannel81InputPwr_Type()
)
pmdge2Mesrchannel81InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel81InputPwr.setStatus("current")


class _Pmdge2Mesrchannel82InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel82InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel82InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel82InputPwr_Object = MibScalar
pmdge2Mesrchannel82InputPwr = _Pmdge2Mesrchannel82InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 153),
    _Pmdge2Mesrchannel82InputPwr_Type()
)
pmdge2Mesrchannel82InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel82InputPwr.setStatus("current")


class _Pmdge2Mesrchannel83InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel83InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel83InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel83InputPwr_Object = MibScalar
pmdge2Mesrchannel83InputPwr = _Pmdge2Mesrchannel83InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 154),
    _Pmdge2Mesrchannel83InputPwr_Type()
)
pmdge2Mesrchannel83InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel83InputPwr.setStatus("current")


class _Pmdge2Mesrchannel84InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel84InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel84InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel84InputPwr_Object = MibScalar
pmdge2Mesrchannel84InputPwr = _Pmdge2Mesrchannel84InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 155),
    _Pmdge2Mesrchannel84InputPwr_Type()
)
pmdge2Mesrchannel84InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel84InputPwr.setStatus("current")


class _Pmdge2Mesrchannel85InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel85InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel85InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel85InputPwr_Object = MibScalar
pmdge2Mesrchannel85InputPwr = _Pmdge2Mesrchannel85InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 156),
    _Pmdge2Mesrchannel85InputPwr_Type()
)
pmdge2Mesrchannel85InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel85InputPwr.setStatus("current")


class _Pmdge2Mesrchannel86InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel86InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel86InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel86InputPwr_Object = MibScalar
pmdge2Mesrchannel86InputPwr = _Pmdge2Mesrchannel86InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 157),
    _Pmdge2Mesrchannel86InputPwr_Type()
)
pmdge2Mesrchannel86InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel86InputPwr.setStatus("current")


class _Pmdge2Mesrchannel87InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel87InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel87InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel87InputPwr_Object = MibScalar
pmdge2Mesrchannel87InputPwr = _Pmdge2Mesrchannel87InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 158),
    _Pmdge2Mesrchannel87InputPwr_Type()
)
pmdge2Mesrchannel87InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel87InputPwr.setStatus("current")


class _Pmdge2Mesrchannel88InputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel88InputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel88InputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel88InputPwr_Object = MibScalar
pmdge2Mesrchannel88InputPwr = _Pmdge2Mesrchannel88InputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 159),
    _Pmdge2Mesrchannel88InputPwr_Type()
)
pmdge2Mesrchannel88InputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel88InputPwr.setStatus("current")


class _Pmdge2Mesrchannel1OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel1OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel1OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel1OutputPwr_Object = MibScalar
pmdge2Mesrchannel1OutputPwr = _Pmdge2Mesrchannel1OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 164),
    _Pmdge2Mesrchannel1OutputPwr_Type()
)
pmdge2Mesrchannel1OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel1OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel2OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel2OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel2OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel2OutputPwr_Object = MibScalar
pmdge2Mesrchannel2OutputPwr = _Pmdge2Mesrchannel2OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 165),
    _Pmdge2Mesrchannel2OutputPwr_Type()
)
pmdge2Mesrchannel2OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel2OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel3OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel3OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel3OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel3OutputPwr_Object = MibScalar
pmdge2Mesrchannel3OutputPwr = _Pmdge2Mesrchannel3OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 166),
    _Pmdge2Mesrchannel3OutputPwr_Type()
)
pmdge2Mesrchannel3OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel3OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel4OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel4OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel4OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel4OutputPwr_Object = MibScalar
pmdge2Mesrchannel4OutputPwr = _Pmdge2Mesrchannel4OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 167),
    _Pmdge2Mesrchannel4OutputPwr_Type()
)
pmdge2Mesrchannel4OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel4OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel5OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel5OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel5OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel5OutputPwr_Object = MibScalar
pmdge2Mesrchannel5OutputPwr = _Pmdge2Mesrchannel5OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 168),
    _Pmdge2Mesrchannel5OutputPwr_Type()
)
pmdge2Mesrchannel5OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel5OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel6OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel6OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel6OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel6OutputPwr_Object = MibScalar
pmdge2Mesrchannel6OutputPwr = _Pmdge2Mesrchannel6OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 169),
    _Pmdge2Mesrchannel6OutputPwr_Type()
)
pmdge2Mesrchannel6OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel6OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel7OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel7OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel7OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel7OutputPwr_Object = MibScalar
pmdge2Mesrchannel7OutputPwr = _Pmdge2Mesrchannel7OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 170),
    _Pmdge2Mesrchannel7OutputPwr_Type()
)
pmdge2Mesrchannel7OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel7OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel8OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel8OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel8OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel8OutputPwr_Object = MibScalar
pmdge2Mesrchannel8OutputPwr = _Pmdge2Mesrchannel8OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 171),
    _Pmdge2Mesrchannel8OutputPwr_Type()
)
pmdge2Mesrchannel8OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel8OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel9OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel9OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel9OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel9OutputPwr_Object = MibScalar
pmdge2Mesrchannel9OutputPwr = _Pmdge2Mesrchannel9OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 172),
    _Pmdge2Mesrchannel9OutputPwr_Type()
)
pmdge2Mesrchannel9OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel9OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel10OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel10OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel10OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel10OutputPwr_Object = MibScalar
pmdge2Mesrchannel10OutputPwr = _Pmdge2Mesrchannel10OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 173),
    _Pmdge2Mesrchannel10OutputPwr_Type()
)
pmdge2Mesrchannel10OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel10OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel11OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel11OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel11OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel11OutputPwr_Object = MibScalar
pmdge2Mesrchannel11OutputPwr = _Pmdge2Mesrchannel11OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 174),
    _Pmdge2Mesrchannel11OutputPwr_Type()
)
pmdge2Mesrchannel11OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel11OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel12OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel12OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel12OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel12OutputPwr_Object = MibScalar
pmdge2Mesrchannel12OutputPwr = _Pmdge2Mesrchannel12OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 175),
    _Pmdge2Mesrchannel12OutputPwr_Type()
)
pmdge2Mesrchannel12OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel12OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel13OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel13OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel13OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel13OutputPwr_Object = MibScalar
pmdge2Mesrchannel13OutputPwr = _Pmdge2Mesrchannel13OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 176),
    _Pmdge2Mesrchannel13OutputPwr_Type()
)
pmdge2Mesrchannel13OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel13OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel14OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel14OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel14OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel14OutputPwr_Object = MibScalar
pmdge2Mesrchannel14OutputPwr = _Pmdge2Mesrchannel14OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 177),
    _Pmdge2Mesrchannel14OutputPwr_Type()
)
pmdge2Mesrchannel14OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel14OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel15OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel15OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel15OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel15OutputPwr_Object = MibScalar
pmdge2Mesrchannel15OutputPwr = _Pmdge2Mesrchannel15OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 178),
    _Pmdge2Mesrchannel15OutputPwr_Type()
)
pmdge2Mesrchannel15OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel15OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel16OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel16OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel16OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel16OutputPwr_Object = MibScalar
pmdge2Mesrchannel16OutputPwr = _Pmdge2Mesrchannel16OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 179),
    _Pmdge2Mesrchannel16OutputPwr_Type()
)
pmdge2Mesrchannel16OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel16OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel17OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel17OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel17OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel17OutputPwr_Object = MibScalar
pmdge2Mesrchannel17OutputPwr = _Pmdge2Mesrchannel17OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 180),
    _Pmdge2Mesrchannel17OutputPwr_Type()
)
pmdge2Mesrchannel17OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel17OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel18OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel18OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel18OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel18OutputPwr_Object = MibScalar
pmdge2Mesrchannel18OutputPwr = _Pmdge2Mesrchannel18OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 181),
    _Pmdge2Mesrchannel18OutputPwr_Type()
)
pmdge2Mesrchannel18OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel18OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel19OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel19OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel19OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel19OutputPwr_Object = MibScalar
pmdge2Mesrchannel19OutputPwr = _Pmdge2Mesrchannel19OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 182),
    _Pmdge2Mesrchannel19OutputPwr_Type()
)
pmdge2Mesrchannel19OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel19OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel20OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel20OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel20OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel20OutputPwr_Object = MibScalar
pmdge2Mesrchannel20OutputPwr = _Pmdge2Mesrchannel20OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 183),
    _Pmdge2Mesrchannel20OutputPwr_Type()
)
pmdge2Mesrchannel20OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel20OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel21OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel21OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel21OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel21OutputPwr_Object = MibScalar
pmdge2Mesrchannel21OutputPwr = _Pmdge2Mesrchannel21OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 184),
    _Pmdge2Mesrchannel21OutputPwr_Type()
)
pmdge2Mesrchannel21OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel21OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel22OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel22OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel22OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel22OutputPwr_Object = MibScalar
pmdge2Mesrchannel22OutputPwr = _Pmdge2Mesrchannel22OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 185),
    _Pmdge2Mesrchannel22OutputPwr_Type()
)
pmdge2Mesrchannel22OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel22OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel23OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel23OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel23OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel23OutputPwr_Object = MibScalar
pmdge2Mesrchannel23OutputPwr = _Pmdge2Mesrchannel23OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 186),
    _Pmdge2Mesrchannel23OutputPwr_Type()
)
pmdge2Mesrchannel23OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel23OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel24OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel24OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel24OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel24OutputPwr_Object = MibScalar
pmdge2Mesrchannel24OutputPwr = _Pmdge2Mesrchannel24OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 187),
    _Pmdge2Mesrchannel24OutputPwr_Type()
)
pmdge2Mesrchannel24OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel24OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel25OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel25OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel25OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel25OutputPwr_Object = MibScalar
pmdge2Mesrchannel25OutputPwr = _Pmdge2Mesrchannel25OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 188),
    _Pmdge2Mesrchannel25OutputPwr_Type()
)
pmdge2Mesrchannel25OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel25OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel26OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel26OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel26OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel26OutputPwr_Object = MibScalar
pmdge2Mesrchannel26OutputPwr = _Pmdge2Mesrchannel26OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 189),
    _Pmdge2Mesrchannel26OutputPwr_Type()
)
pmdge2Mesrchannel26OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel26OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel27OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel27OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel27OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel27OutputPwr_Object = MibScalar
pmdge2Mesrchannel27OutputPwr = _Pmdge2Mesrchannel27OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 190),
    _Pmdge2Mesrchannel27OutputPwr_Type()
)
pmdge2Mesrchannel27OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel27OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel28OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel28OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel28OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel28OutputPwr_Object = MibScalar
pmdge2Mesrchannel28OutputPwr = _Pmdge2Mesrchannel28OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 191),
    _Pmdge2Mesrchannel28OutputPwr_Type()
)
pmdge2Mesrchannel28OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel28OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel29OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel29OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel29OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel29OutputPwr_Object = MibScalar
pmdge2Mesrchannel29OutputPwr = _Pmdge2Mesrchannel29OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 192),
    _Pmdge2Mesrchannel29OutputPwr_Type()
)
pmdge2Mesrchannel29OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel29OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel30OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel30OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel30OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel30OutputPwr_Object = MibScalar
pmdge2Mesrchannel30OutputPwr = _Pmdge2Mesrchannel30OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 193),
    _Pmdge2Mesrchannel30OutputPwr_Type()
)
pmdge2Mesrchannel30OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel30OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel31OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel31OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel31OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel31OutputPwr_Object = MibScalar
pmdge2Mesrchannel31OutputPwr = _Pmdge2Mesrchannel31OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 194),
    _Pmdge2Mesrchannel31OutputPwr_Type()
)
pmdge2Mesrchannel31OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel31OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel32OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel32OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel32OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel32OutputPwr_Object = MibScalar
pmdge2Mesrchannel32OutputPwr = _Pmdge2Mesrchannel32OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 195),
    _Pmdge2Mesrchannel32OutputPwr_Type()
)
pmdge2Mesrchannel32OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel32OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel33OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel33OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel33OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel33OutputPwr_Object = MibScalar
pmdge2Mesrchannel33OutputPwr = _Pmdge2Mesrchannel33OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 196),
    _Pmdge2Mesrchannel33OutputPwr_Type()
)
pmdge2Mesrchannel33OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel33OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel34OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel34OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel34OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel34OutputPwr_Object = MibScalar
pmdge2Mesrchannel34OutputPwr = _Pmdge2Mesrchannel34OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 197),
    _Pmdge2Mesrchannel34OutputPwr_Type()
)
pmdge2Mesrchannel34OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel34OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel35OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel35OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel35OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel35OutputPwr_Object = MibScalar
pmdge2Mesrchannel35OutputPwr = _Pmdge2Mesrchannel35OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 198),
    _Pmdge2Mesrchannel35OutputPwr_Type()
)
pmdge2Mesrchannel35OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel35OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel36OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel36OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel36OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel36OutputPwr_Object = MibScalar
pmdge2Mesrchannel36OutputPwr = _Pmdge2Mesrchannel36OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 199),
    _Pmdge2Mesrchannel36OutputPwr_Type()
)
pmdge2Mesrchannel36OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel36OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel37OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel37OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel37OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel37OutputPwr_Object = MibScalar
pmdge2Mesrchannel37OutputPwr = _Pmdge2Mesrchannel37OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 200),
    _Pmdge2Mesrchannel37OutputPwr_Type()
)
pmdge2Mesrchannel37OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel37OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel38OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel38OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel38OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel38OutputPwr_Object = MibScalar
pmdge2Mesrchannel38OutputPwr = _Pmdge2Mesrchannel38OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 201),
    _Pmdge2Mesrchannel38OutputPwr_Type()
)
pmdge2Mesrchannel38OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel38OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel39OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel39OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel39OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel39OutputPwr_Object = MibScalar
pmdge2Mesrchannel39OutputPwr = _Pmdge2Mesrchannel39OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 202),
    _Pmdge2Mesrchannel39OutputPwr_Type()
)
pmdge2Mesrchannel39OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel39OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel40OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel40OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel40OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel40OutputPwr_Object = MibScalar
pmdge2Mesrchannel40OutputPwr = _Pmdge2Mesrchannel40OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 203),
    _Pmdge2Mesrchannel40OutputPwr_Type()
)
pmdge2Mesrchannel40OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel40OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel41OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel41OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel41OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel41OutputPwr_Object = MibScalar
pmdge2Mesrchannel41OutputPwr = _Pmdge2Mesrchannel41OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 204),
    _Pmdge2Mesrchannel41OutputPwr_Type()
)
pmdge2Mesrchannel41OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel41OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel42OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel42OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel42OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel42OutputPwr_Object = MibScalar
pmdge2Mesrchannel42OutputPwr = _Pmdge2Mesrchannel42OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 205),
    _Pmdge2Mesrchannel42OutputPwr_Type()
)
pmdge2Mesrchannel42OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel42OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel43OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel43OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel43OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel43OutputPwr_Object = MibScalar
pmdge2Mesrchannel43OutputPwr = _Pmdge2Mesrchannel43OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 206),
    _Pmdge2Mesrchannel43OutputPwr_Type()
)
pmdge2Mesrchannel43OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel43OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel44OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel44OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel44OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel44OutputPwr_Object = MibScalar
pmdge2Mesrchannel44OutputPwr = _Pmdge2Mesrchannel44OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 207),
    _Pmdge2Mesrchannel44OutputPwr_Type()
)
pmdge2Mesrchannel44OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel44OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel45OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel45OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel45OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel45OutputPwr_Object = MibScalar
pmdge2Mesrchannel45OutputPwr = _Pmdge2Mesrchannel45OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 208),
    _Pmdge2Mesrchannel45OutputPwr_Type()
)
pmdge2Mesrchannel45OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel45OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel46OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel46OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel46OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel46OutputPwr_Object = MibScalar
pmdge2Mesrchannel46OutputPwr = _Pmdge2Mesrchannel46OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 209),
    _Pmdge2Mesrchannel46OutputPwr_Type()
)
pmdge2Mesrchannel46OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel46OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel47OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel47OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel47OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel47OutputPwr_Object = MibScalar
pmdge2Mesrchannel47OutputPwr = _Pmdge2Mesrchannel47OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 210),
    _Pmdge2Mesrchannel47OutputPwr_Type()
)
pmdge2Mesrchannel47OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel47OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel48OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel48OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel48OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel48OutputPwr_Object = MibScalar
pmdge2Mesrchannel48OutputPwr = _Pmdge2Mesrchannel48OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 211),
    _Pmdge2Mesrchannel48OutputPwr_Type()
)
pmdge2Mesrchannel48OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel48OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel49OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel49OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel49OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel49OutputPwr_Object = MibScalar
pmdge2Mesrchannel49OutputPwr = _Pmdge2Mesrchannel49OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 212),
    _Pmdge2Mesrchannel49OutputPwr_Type()
)
pmdge2Mesrchannel49OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel49OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel50OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel50OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel50OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel50OutputPwr_Object = MibScalar
pmdge2Mesrchannel50OutputPwr = _Pmdge2Mesrchannel50OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 213),
    _Pmdge2Mesrchannel50OutputPwr_Type()
)
pmdge2Mesrchannel50OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel50OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel51OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel51OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel51OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel51OutputPwr_Object = MibScalar
pmdge2Mesrchannel51OutputPwr = _Pmdge2Mesrchannel51OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 214),
    _Pmdge2Mesrchannel51OutputPwr_Type()
)
pmdge2Mesrchannel51OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel51OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel52OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel52OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel52OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel52OutputPwr_Object = MibScalar
pmdge2Mesrchannel52OutputPwr = _Pmdge2Mesrchannel52OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 215),
    _Pmdge2Mesrchannel52OutputPwr_Type()
)
pmdge2Mesrchannel52OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel52OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel53OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel53OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel53OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel53OutputPwr_Object = MibScalar
pmdge2Mesrchannel53OutputPwr = _Pmdge2Mesrchannel53OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 216),
    _Pmdge2Mesrchannel53OutputPwr_Type()
)
pmdge2Mesrchannel53OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel53OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel54OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel54OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel54OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel54OutputPwr_Object = MibScalar
pmdge2Mesrchannel54OutputPwr = _Pmdge2Mesrchannel54OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 217),
    _Pmdge2Mesrchannel54OutputPwr_Type()
)
pmdge2Mesrchannel54OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel54OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel55OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel55OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel55OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel55OutputPwr_Object = MibScalar
pmdge2Mesrchannel55OutputPwr = _Pmdge2Mesrchannel55OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 218),
    _Pmdge2Mesrchannel55OutputPwr_Type()
)
pmdge2Mesrchannel55OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel55OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel56OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel56OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel56OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel56OutputPwr_Object = MibScalar
pmdge2Mesrchannel56OutputPwr = _Pmdge2Mesrchannel56OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 219),
    _Pmdge2Mesrchannel56OutputPwr_Type()
)
pmdge2Mesrchannel56OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel56OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel57OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel57OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel57OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel57OutputPwr_Object = MibScalar
pmdge2Mesrchannel57OutputPwr = _Pmdge2Mesrchannel57OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 220),
    _Pmdge2Mesrchannel57OutputPwr_Type()
)
pmdge2Mesrchannel57OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel57OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel58OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel58OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel58OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel58OutputPwr_Object = MibScalar
pmdge2Mesrchannel58OutputPwr = _Pmdge2Mesrchannel58OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 221),
    _Pmdge2Mesrchannel58OutputPwr_Type()
)
pmdge2Mesrchannel58OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel58OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel59OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel59OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel59OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel59OutputPwr_Object = MibScalar
pmdge2Mesrchannel59OutputPwr = _Pmdge2Mesrchannel59OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 222),
    _Pmdge2Mesrchannel59OutputPwr_Type()
)
pmdge2Mesrchannel59OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel59OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel60OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel60OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel60OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel60OutputPwr_Object = MibScalar
pmdge2Mesrchannel60OutputPwr = _Pmdge2Mesrchannel60OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 223),
    _Pmdge2Mesrchannel60OutputPwr_Type()
)
pmdge2Mesrchannel60OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel60OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel61OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel61OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel61OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel61OutputPwr_Object = MibScalar
pmdge2Mesrchannel61OutputPwr = _Pmdge2Mesrchannel61OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 224),
    _Pmdge2Mesrchannel61OutputPwr_Type()
)
pmdge2Mesrchannel61OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel61OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel62OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel62OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel62OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel62OutputPwr_Object = MibScalar
pmdge2Mesrchannel62OutputPwr = _Pmdge2Mesrchannel62OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 225),
    _Pmdge2Mesrchannel62OutputPwr_Type()
)
pmdge2Mesrchannel62OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel62OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel63OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel63OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel63OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel63OutputPwr_Object = MibScalar
pmdge2Mesrchannel63OutputPwr = _Pmdge2Mesrchannel63OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 226),
    _Pmdge2Mesrchannel63OutputPwr_Type()
)
pmdge2Mesrchannel63OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel63OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel64OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel64OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel64OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel64OutputPwr_Object = MibScalar
pmdge2Mesrchannel64OutputPwr = _Pmdge2Mesrchannel64OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 227),
    _Pmdge2Mesrchannel64OutputPwr_Type()
)
pmdge2Mesrchannel64OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel64OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel65OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel65OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel65OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel65OutputPwr_Object = MibScalar
pmdge2Mesrchannel65OutputPwr = _Pmdge2Mesrchannel65OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 228),
    _Pmdge2Mesrchannel65OutputPwr_Type()
)
pmdge2Mesrchannel65OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel65OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel66OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel66OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel66OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel66OutputPwr_Object = MibScalar
pmdge2Mesrchannel66OutputPwr = _Pmdge2Mesrchannel66OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 229),
    _Pmdge2Mesrchannel66OutputPwr_Type()
)
pmdge2Mesrchannel66OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel66OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel67OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel67OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel67OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel67OutputPwr_Object = MibScalar
pmdge2Mesrchannel67OutputPwr = _Pmdge2Mesrchannel67OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 230),
    _Pmdge2Mesrchannel67OutputPwr_Type()
)
pmdge2Mesrchannel67OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel67OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel68OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel68OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel68OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel68OutputPwr_Object = MibScalar
pmdge2Mesrchannel68OutputPwr = _Pmdge2Mesrchannel68OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 231),
    _Pmdge2Mesrchannel68OutputPwr_Type()
)
pmdge2Mesrchannel68OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel68OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel69OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel69OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel69OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel69OutputPwr_Object = MibScalar
pmdge2Mesrchannel69OutputPwr = _Pmdge2Mesrchannel69OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 232),
    _Pmdge2Mesrchannel69OutputPwr_Type()
)
pmdge2Mesrchannel69OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel69OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel70OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel70OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel70OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel70OutputPwr_Object = MibScalar
pmdge2Mesrchannel70OutputPwr = _Pmdge2Mesrchannel70OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 233),
    _Pmdge2Mesrchannel70OutputPwr_Type()
)
pmdge2Mesrchannel70OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel70OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel71OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel71OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel71OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel71OutputPwr_Object = MibScalar
pmdge2Mesrchannel71OutputPwr = _Pmdge2Mesrchannel71OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 234),
    _Pmdge2Mesrchannel71OutputPwr_Type()
)
pmdge2Mesrchannel71OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel71OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel72OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel72OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel72OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel72OutputPwr_Object = MibScalar
pmdge2Mesrchannel72OutputPwr = _Pmdge2Mesrchannel72OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 235),
    _Pmdge2Mesrchannel72OutputPwr_Type()
)
pmdge2Mesrchannel72OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel72OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel73OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel73OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel73OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel73OutputPwr_Object = MibScalar
pmdge2Mesrchannel73OutputPwr = _Pmdge2Mesrchannel73OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 236),
    _Pmdge2Mesrchannel73OutputPwr_Type()
)
pmdge2Mesrchannel73OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel73OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel74OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel74OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel74OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel74OutputPwr_Object = MibScalar
pmdge2Mesrchannel74OutputPwr = _Pmdge2Mesrchannel74OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 237),
    _Pmdge2Mesrchannel74OutputPwr_Type()
)
pmdge2Mesrchannel74OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel74OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel75OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel75OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel75OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel75OutputPwr_Object = MibScalar
pmdge2Mesrchannel75OutputPwr = _Pmdge2Mesrchannel75OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 238),
    _Pmdge2Mesrchannel75OutputPwr_Type()
)
pmdge2Mesrchannel75OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel75OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel76OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel76OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel76OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel76OutputPwr_Object = MibScalar
pmdge2Mesrchannel76OutputPwr = _Pmdge2Mesrchannel76OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 239),
    _Pmdge2Mesrchannel76OutputPwr_Type()
)
pmdge2Mesrchannel76OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel76OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel77OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel77OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel77OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel77OutputPwr_Object = MibScalar
pmdge2Mesrchannel77OutputPwr = _Pmdge2Mesrchannel77OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 240),
    _Pmdge2Mesrchannel77OutputPwr_Type()
)
pmdge2Mesrchannel77OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel77OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel78OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel78OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel78OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel78OutputPwr_Object = MibScalar
pmdge2Mesrchannel78OutputPwr = _Pmdge2Mesrchannel78OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 241),
    _Pmdge2Mesrchannel78OutputPwr_Type()
)
pmdge2Mesrchannel78OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel78OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel79OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel79OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel79OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel79OutputPwr_Object = MibScalar
pmdge2Mesrchannel79OutputPwr = _Pmdge2Mesrchannel79OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 242),
    _Pmdge2Mesrchannel79OutputPwr_Type()
)
pmdge2Mesrchannel79OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel79OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel80OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel80OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel80OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel80OutputPwr_Object = MibScalar
pmdge2Mesrchannel80OutputPwr = _Pmdge2Mesrchannel80OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 243),
    _Pmdge2Mesrchannel80OutputPwr_Type()
)
pmdge2Mesrchannel80OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel80OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel81OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel81OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel81OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel81OutputPwr_Object = MibScalar
pmdge2Mesrchannel81OutputPwr = _Pmdge2Mesrchannel81OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 244),
    _Pmdge2Mesrchannel81OutputPwr_Type()
)
pmdge2Mesrchannel81OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel81OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel82OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel82OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel82OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel82OutputPwr_Object = MibScalar
pmdge2Mesrchannel82OutputPwr = _Pmdge2Mesrchannel82OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 245),
    _Pmdge2Mesrchannel82OutputPwr_Type()
)
pmdge2Mesrchannel82OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel82OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel83OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel83OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel83OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel83OutputPwr_Object = MibScalar
pmdge2Mesrchannel83OutputPwr = _Pmdge2Mesrchannel83OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 246),
    _Pmdge2Mesrchannel83OutputPwr_Type()
)
pmdge2Mesrchannel83OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel83OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel84OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel84OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel84OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel84OutputPwr_Object = MibScalar
pmdge2Mesrchannel84OutputPwr = _Pmdge2Mesrchannel84OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 247),
    _Pmdge2Mesrchannel84OutputPwr_Type()
)
pmdge2Mesrchannel84OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel84OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel85OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel85OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel85OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel85OutputPwr_Object = MibScalar
pmdge2Mesrchannel85OutputPwr = _Pmdge2Mesrchannel85OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 248),
    _Pmdge2Mesrchannel85OutputPwr_Type()
)
pmdge2Mesrchannel85OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel85OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel86OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel86OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel86OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel86OutputPwr_Object = MibScalar
pmdge2Mesrchannel86OutputPwr = _Pmdge2Mesrchannel86OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 249),
    _Pmdge2Mesrchannel86OutputPwr_Type()
)
pmdge2Mesrchannel86OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel86OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel87OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel87OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel87OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel87OutputPwr_Object = MibScalar
pmdge2Mesrchannel87OutputPwr = _Pmdge2Mesrchannel87OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 250),
    _Pmdge2Mesrchannel87OutputPwr_Type()
)
pmdge2Mesrchannel87OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel87OutputPwr.setStatus("current")


class _Pmdge2Mesrchannel88OutputPwr_Type(Unsigned32):
    """Custom type pmdge2Mesrchannel88OutputPwr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmdge2Mesrchannel88OutputPwr_Type.__name__ = "Unsigned32"
_Pmdge2Mesrchannel88OutputPwr_Object = MibScalar
pmdge2Mesrchannel88OutputPwr = _Pmdge2Mesrchannel88OutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 3, 1, 251),
    _Pmdge2Mesrchannel88OutputPwr_Type()
)
pmdge2Mesrchannel88OutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Mesrchannel88OutputPwr.setStatus("current")
_Pmdge2controlsWrite_ObjectIdentity = ObjectIdentity
pmdge2controlsWrite = _Pmdge2controlsWrite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 65, 6)
)
_Pmdge2CtrlOther_ObjectIdentity = ObjectIdentity
pmdge2CtrlOther = _Pmdge2CtrlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 65, 6, 1)
)
_Pmdge2Ctrlsynth0_ObjectIdentity = ObjectIdentity
pmdge2Ctrlsynth0 = _Pmdge2Ctrlsynth0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 65, 6, 1, 0)
)
_Pmdge2CtrlConfLoad_Type = EkiOnOff
_Pmdge2CtrlConfLoad_Object = MibScalar
pmdge2CtrlConfLoad = _Pmdge2CtrlConfLoad_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 6, 1, 0, 1),
    _Pmdge2CtrlConfLoad_Type()
)
pmdge2CtrlConfLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmdge2CtrlConfLoad.setStatus("current")
_Pmdge2CtrlConfFlash_Type = EkiOnOff
_Pmdge2CtrlConfFlash_Object = MibScalar
pmdge2CtrlConfFlash = _Pmdge2CtrlConfFlash_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 6, 1, 0, 9),
    _Pmdge2CtrlConfFlash_Type()
)
pmdge2CtrlConfFlash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmdge2CtrlConfFlash.setStatus("current")
_Pmdge2CtrlConfClear_Type = EkiOnOff
_Pmdge2CtrlConfClear_Object = MibScalar
pmdge2CtrlConfClear = _Pmdge2CtrlConfClear_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 6, 1, 0, 13),
    _Pmdge2CtrlConfClear_Type()
)
pmdge2CtrlConfClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmdge2CtrlConfClear.setStatus("current")
_Pmdge2Ctrlsynth4_ObjectIdentity = ObjectIdentity
pmdge2Ctrlsynth4 = _Pmdge2Ctrlsynth4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 65, 6, 1, 4)
)
_Pmdge2CtrlCorrelatOn_Type = EkiOnOff
_Pmdge2CtrlCorrelatOn_Object = MibScalar
pmdge2CtrlCorrelatOn = _Pmdge2CtrlCorrelatOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 6, 1, 4, 1),
    _Pmdge2CtrlCorrelatOn_Type()
)
pmdge2CtrlCorrelatOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmdge2CtrlCorrelatOn.setStatus("current")
_Pmdge2CtrlCorrelatOff_Type = EkiOnOff
_Pmdge2CtrlCorrelatOff_Object = MibScalar
pmdge2CtrlCorrelatOff = _Pmdge2CtrlCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 6, 1, 4, 2),
    _Pmdge2CtrlCorrelatOff_Type()
)
pmdge2CtrlCorrelatOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmdge2CtrlCorrelatOff.setStatus("current")
_Pmdge2CtrlswMgnt_ObjectIdentity = ObjectIdentity
pmdge2CtrlswMgnt = _Pmdge2CtrlswMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 65, 6, 1, 5)
)
_Pmdge2CtrlColdReset_Type = EkiOnOff
_Pmdge2CtrlColdReset_Object = MibScalar
pmdge2CtrlColdReset = _Pmdge2CtrlColdReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 6, 1, 5, 2),
    _Pmdge2CtrlColdReset_Type()
)
pmdge2CtrlColdReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmdge2CtrlColdReset.setStatus("current")
_Pmdge2CtrlWarmReset_Type = EkiOnOff
_Pmdge2CtrlWarmReset_Object = MibScalar
pmdge2CtrlWarmReset = _Pmdge2CtrlWarmReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 6, 1, 5, 3),
    _Pmdge2CtrlWarmReset_Type()
)
pmdge2CtrlWarmReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmdge2CtrlWarmReset.setStatus("current")
_Pmdge2CtrlswitchCtrl_ObjectIdentity = ObjectIdentity
pmdge2CtrlswitchCtrl = _Pmdge2CtrlswitchCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 65, 6, 1, 16)
)
_Pmdge2CtrlAllChannelsHighLoss_Type = EkiOnOff
_Pmdge2CtrlAllChannelsHighLoss_Object = MibScalar
pmdge2CtrlAllChannelsHighLoss = _Pmdge2CtrlAllChannelsHighLoss_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 6, 1, 16, 1),
    _Pmdge2CtrlAllChannelsHighLoss_Type()
)
pmdge2CtrlAllChannelsHighLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmdge2CtrlAllChannelsHighLoss.setStatus("current")
_Pmdge2CtrlmanualStart_ObjectIdentity = ObjectIdentity
pmdge2CtrlmanualStart = _Pmdge2CtrlmanualStart_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 65, 6, 1, 17)
)
_Pmdge2CtrlManualStart_Type = EkiOnOff
_Pmdge2CtrlManualStart_Object = MibScalar
pmdge2CtrlManualStart = _Pmdge2CtrlManualStart_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 6, 1, 17, 1),
    _Pmdge2CtrlManualStart_Type()
)
pmdge2CtrlManualStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmdge2CtrlManualStart.setStatus("current")
_Pmdge2CtrlledTest_ObjectIdentity = ObjectIdentity
pmdge2CtrlledTest = _Pmdge2CtrlledTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 65, 6, 1, 64)
)
_Pmdge2CtrlGreenLed_Type = EkiOnOff
_Pmdge2CtrlGreenLed_Object = MibScalar
pmdge2CtrlGreenLed = _Pmdge2CtrlGreenLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 6, 1, 64, 1),
    _Pmdge2CtrlGreenLed_Type()
)
pmdge2CtrlGreenLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmdge2CtrlGreenLed.setStatus("current")
_Pmdge2CtrlRedLed_Type = EkiOnOff
_Pmdge2CtrlRedLed_Object = MibScalar
pmdge2CtrlRedLed = _Pmdge2CtrlRedLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 6, 1, 64, 2),
    _Pmdge2CtrlRedLed_Type()
)
pmdge2CtrlRedLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmdge2CtrlRedLed.setStatus("current")
_Pmdge2CtrlLedOff_Type = EkiOnOff
_Pmdge2CtrlLedOff_Object = MibScalar
pmdge2CtrlLedOff = _Pmdge2CtrlLedOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 6, 1, 64, 3),
    _Pmdge2CtrlLedOff_Type()
)
pmdge2CtrlLedOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmdge2CtrlLedOff.setStatus("current")
_Pmdge2CtrlEqualizer_ObjectIdentity = ObjectIdentity
pmdge2CtrlEqualizer = _Pmdge2CtrlEqualizer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 65, 6, 2)
)
_Pmdge2CtrlLine_ObjectIdentity = ObjectIdentity
pmdge2CtrlLine = _Pmdge2CtrlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 65, 6, 3)
)
_Pmdge2ri_ObjectIdentity = ObjectIdentity
pmdge2ri = _Pmdge2ri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 65, 7)
)
_Pmdge2riTable_ObjectIdentity = ObjectIdentity
pmdge2riTable = _Pmdge2riTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 65, 7, 1)
)
_Pmdge2RinvPortTable_Object = MibTable
pmdge2RinvPortTable = _Pmdge2RinvPortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 7, 1, 1)
)
if mibBuilder.loadTexts:
    pmdge2RinvPortTable.setStatus("current")
_Pmdge2RinvPortEntry_Object = MibTableRow
pmdge2RinvPortEntry = _Pmdge2RinvPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 7, 1, 1, 1)
)
pmdge2RinvPortEntry.setIndexNames(
    (0, "EKINOPS-PmDGE2-MIB", "pmdge2RinvPortIndex"),
)
if mibBuilder.loadTexts:
    pmdge2RinvPortEntry.setStatus("current")


class _Pmdge2RinvPortIndex_Type(Integer32):
    """Custom type pmdge2RinvPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Pmdge2RinvPortIndex_Type.__name__ = "Integer32"
_Pmdge2RinvPortIndex_Object = MibTableColumn
pmdge2RinvPortIndex = _Pmdge2RinvPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 7, 1, 1, 1, 1),
    _Pmdge2RinvPortIndex_Type()
)
pmdge2RinvPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2RinvPortIndex.setStatus("current")
_Pmdge2RinvPort_Type = DisplayString
_Pmdge2RinvPort_Object = MibTableColumn
pmdge2RinvPort = _Pmdge2RinvPort_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 7, 1, 1, 1, 2),
    _Pmdge2RinvPort_Type()
)
pmdge2RinvPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2RinvPort.setStatus("current")
_Pmdge2RinvLineTable_Object = MibTable
pmdge2RinvLineTable = _Pmdge2RinvLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 7, 1, 2)
)
if mibBuilder.loadTexts:
    pmdge2RinvLineTable.setStatus("current")
_Pmdge2RinvLineEntry_Object = MibTableRow
pmdge2RinvLineEntry = _Pmdge2RinvLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 7, 1, 2, 1)
)
pmdge2RinvLineEntry.setIndexNames(
    (0, "EKINOPS-PmDGE2-MIB", "pmdge2RinvLineIndex"),
)
if mibBuilder.loadTexts:
    pmdge2RinvLineEntry.setStatus("current")


class _Pmdge2RinvLineIndex_Type(Integer32):
    """Custom type pmdge2RinvLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Pmdge2RinvLineIndex_Type.__name__ = "Integer32"
_Pmdge2RinvLineIndex_Object = MibTableColumn
pmdge2RinvLineIndex = _Pmdge2RinvLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 7, 1, 2, 1, 1),
    _Pmdge2RinvLineIndex_Type()
)
pmdge2RinvLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2RinvLineIndex.setStatus("current")
_Pmdge2RinvxfpLine_Type = DisplayString
_Pmdge2RinvxfpLine_Object = MibTableColumn
pmdge2RinvxfpLine = _Pmdge2RinvxfpLine_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 7, 1, 2, 1, 2),
    _Pmdge2RinvxfpLine_Type()
)
pmdge2RinvxfpLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2RinvxfpLine.setStatus("current")
_Pmdge2RinvReloadInventory_Type = EkiOnOff
_Pmdge2RinvReloadInventory_Object = MibScalar
pmdge2RinvReloadInventory = _Pmdge2RinvReloadInventory_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 7, 2),
    _Pmdge2RinvReloadInventory_Type()
)
pmdge2RinvReloadInventory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmdge2RinvReloadInventory.setStatus("current")
_Pmdge2RinvHwPlatform_Type = DisplayString
_Pmdge2RinvHwPlatform_Object = MibScalar
pmdge2RinvHwPlatform = _Pmdge2RinvHwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 7, 4),
    _Pmdge2RinvHwPlatform_Type()
)
pmdge2RinvHwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2RinvHwPlatform.setStatus("current")
_Pmdge2RinvSwPlatform_Type = DisplayString
_Pmdge2RinvSwPlatform_Object = MibScalar
pmdge2RinvSwPlatform = _Pmdge2RinvSwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 7, 5),
    _Pmdge2RinvSwPlatform_Type()
)
pmdge2RinvSwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2RinvSwPlatform.setStatus("current")
_Pmdge2Config_ObjectIdentity = ObjectIdentity
pmdge2Config = _Pmdge2Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 65, 9)
)
_Pmdge2CfgLsd_ObjectIdentity = ObjectIdentity
pmdge2CfgLsd = _Pmdge2CfgLsd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 65, 9, 1)
)
_Pmdge2tableclientLsd_ObjectIdentity = ObjectIdentity
pmdge2tableclientLsd = _Pmdge2tableclientLsd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 65, 9, 1, 1)
)
_Pmdge2CfgStartup_ObjectIdentity = ObjectIdentity
pmdge2CfgStartup = _Pmdge2CfgStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 65, 9, 2)
)
_Pmdge2tableother_ObjectIdentity = ObjectIdentity
pmdge2tableother = _Pmdge2tableother_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 65, 9, 2, 1)
)


class _Pmdge2Cfggrid_Type(Unsigned32):
    """Custom type pmdge2Cfggrid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmdge2Cfggrid_Type.__name__ = "Unsigned32"
_Pmdge2Cfggrid_Object = MibScalar
pmdge2Cfggrid = _Pmdge2Cfggrid_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 9, 2, 1, 2),
    _Pmdge2Cfggrid_Type()
)
pmdge2Cfggrid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmdge2Cfggrid.setStatus("current")


class _Pmdge2CfgequalizationReference_Type(Unsigned32):
    """Custom type pmdge2CfgequalizationReference based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmdge2CfgequalizationReference_Type.__name__ = "Unsigned32"
_Pmdge2CfgequalizationReference_Object = MibScalar
pmdge2CfgequalizationReference = _Pmdge2CfgequalizationReference_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 9, 2, 1, 3),
    _Pmdge2CfgequalizationReference_Type()
)
pmdge2CfgequalizationReference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmdge2CfgequalizationReference.setStatus("current")


class _Pmdge2CfgequalizationMode_Type(Unsigned32):
    """Custom type pmdge2CfgequalizationMode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmdge2CfgequalizationMode_Type.__name__ = "Unsigned32"
_Pmdge2CfgequalizationMode_Object = MibScalar
pmdge2CfgequalizationMode = _Pmdge2CfgequalizationMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 9, 2, 1, 4),
    _Pmdge2CfgequalizationMode_Type()
)
pmdge2CfgequalizationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmdge2CfgequalizationMode.setStatus("current")


class _Pmdge2CfgchannelPowerRefValue_Type(Unsigned32):
    """Custom type pmdge2CfgchannelPowerRefValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmdge2CfgchannelPowerRefValue_Type.__name__ = "Unsigned32"
_Pmdge2CfgchannelPowerRefValue_Object = MibScalar
pmdge2CfgchannelPowerRefValue = _Pmdge2CfgchannelPowerRefValue_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 9, 2, 1, 5),
    _Pmdge2CfgchannelPowerRefValue_Type()
)
pmdge2CfgchannelPowerRefValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmdge2CfgchannelPowerRefValue.setStatus("current")


class _Pmdge2CfgchannelPresenceThreshold_Type(Unsigned32):
    """Custom type pmdge2CfgchannelPresenceThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmdge2CfgchannelPresenceThreshold_Type.__name__ = "Unsigned32"
_Pmdge2CfgchannelPresenceThreshold_Object = MibScalar
pmdge2CfgchannelPresenceThreshold = _Pmdge2CfgchannelPresenceThreshold_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 9, 2, 1, 6),
    _Pmdge2CfgchannelPresenceThreshold_Type()
)
pmdge2CfgchannelPresenceThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmdge2CfgchannelPresenceThreshold.setStatus("current")


class _Pmdge2CfgmonitoringPortAtt_Type(Unsigned32):
    """Custom type pmdge2CfgmonitoringPortAtt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmdge2CfgmonitoringPortAtt_Type.__name__ = "Unsigned32"
_Pmdge2CfgmonitoringPortAtt_Object = MibScalar
pmdge2CfgmonitoringPortAtt = _Pmdge2CfgmonitoringPortAtt_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 9, 2, 1, 7),
    _Pmdge2CfgmonitoringPortAtt_Type()
)
pmdge2CfgmonitoringPortAtt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmdge2CfgmonitoringPortAtt.setStatus("current")


class _Pmdge2CfgscanningPeriod_Type(Unsigned32):
    """Custom type pmdge2CfgscanningPeriod based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmdge2CfgscanningPeriod_Type.__name__ = "Unsigned32"
_Pmdge2CfgscanningPeriod_Object = MibScalar
pmdge2CfgscanningPeriod = _Pmdge2CfgscanningPeriod_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 9, 2, 1, 8),
    _Pmdge2CfgscanningPeriod_Type()
)
pmdge2CfgscanningPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmdge2CfgscanningPeriod.setStatus("current")
_Pmdge2tableother1_ObjectIdentity = ObjectIdentity
pmdge2tableother1 = _Pmdge2tableother1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 65, 9, 2, 2)
)


class _Pmdge2CfgcomponentType_Type(Unsigned32):
    """Custom type pmdge2CfgcomponentType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmdge2CfgcomponentType_Type.__name__ = "Unsigned32"
_Pmdge2CfgcomponentType_Object = MibScalar
pmdge2CfgcomponentType = _Pmdge2CfgcomponentType_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 9, 2, 2, 2),
    _Pmdge2CfgcomponentType_Type()
)
pmdge2CfgcomponentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2CfgcomponentType.setStatus("current")


class _Pmdge2Cfgmiscellaneous_Type(Unsigned32):
    """Custom type pmdge2Cfgmiscellaneous based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmdge2Cfgmiscellaneous_Type.__name__ = "Unsigned32"
_Pmdge2Cfgmiscellaneous_Object = MibScalar
pmdge2Cfgmiscellaneous = _Pmdge2Cfgmiscellaneous_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 9, 2, 2, 3),
    _Pmdge2Cfgmiscellaneous_Type()
)
pmdge2Cfgmiscellaneous.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2Cfgmiscellaneous.setStatus("current")


class _Pmdge2CfgfirstChannel_Type(Unsigned32):
    """Custom type pmdge2CfgfirstChannel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmdge2CfgfirstChannel_Type.__name__ = "Unsigned32"
_Pmdge2CfgfirstChannel_Object = MibScalar
pmdge2CfgfirstChannel = _Pmdge2CfgfirstChannel_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 9, 2, 2, 4),
    _Pmdge2CfgfirstChannel_Type()
)
pmdge2CfgfirstChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2CfgfirstChannel.setStatus("current")


class _Pmdge2CfglastChannel_Type(Unsigned32):
    """Custom type pmdge2CfglastChannel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmdge2CfglastChannel_Type.__name__ = "Unsigned32"
_Pmdge2CfglastChannel_Object = MibScalar
pmdge2CfglastChannel = _Pmdge2CfglastChannel_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 9, 2, 2, 5),
    _Pmdge2CfglastChannel_Type()
)
pmdge2CfglastChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2CfglastChannel.setStatus("current")


class _Pmdge2CfggridUsed_Type(Unsigned32):
    """Custom type pmdge2CfggridUsed based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmdge2CfggridUsed_Type.__name__ = "Unsigned32"
_Pmdge2CfggridUsed_Object = MibScalar
pmdge2CfggridUsed = _Pmdge2CfggridUsed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 9, 2, 2, 6),
    _Pmdge2CfggridUsed_Type()
)
pmdge2CfggridUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2CfggridUsed.setStatus("current")
_Pmdge2CfgLabels_ObjectIdentity = ObjectIdentity
pmdge2CfgLabels = _Pmdge2CfgLabels_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 65, 9, 3)
)
_Pmdge2CfgLabelclientTable_Object = MibTable
pmdge2CfgLabelclientTable = _Pmdge2CfgLabelclientTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 9, 3, 1)
)
if mibBuilder.loadTexts:
    pmdge2CfgLabelclientTable.setStatus("current")
_Pmdge2CfgLabelclientEntry_Object = MibTableRow
pmdge2CfgLabelclientEntry = _Pmdge2CfgLabelclientEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 9, 3, 1, 1)
)
pmdge2CfgLabelclientEntry.setIndexNames(
    (0, "EKINOPS-PmDGE2-MIB", "pmdge2CfgLabelclientIndex"),
)
if mibBuilder.loadTexts:
    pmdge2CfgLabelclientEntry.setStatus("current")


class _Pmdge2CfgLabelclientIndex_Type(Integer32):
    """Custom type pmdge2CfgLabelclientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmdge2CfgLabelclientIndex_Type.__name__ = "Integer32"
_Pmdge2CfgLabelclientIndex_Object = MibTableColumn
pmdge2CfgLabelclientIndex = _Pmdge2CfgLabelclientIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 9, 3, 1, 1, 1),
    _Pmdge2CfgLabelclientIndex_Type()
)
pmdge2CfgLabelclientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2CfgLabelclientIndex.setStatus("current")


class _Pmdge2CfgLabelclientPortn_Type(DisplayString):
    """Custom type pmdge2CfgLabelclientPortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pmdge2CfgLabelclientPortn_Type.__name__ = "DisplayString"
_Pmdge2CfgLabelclientPortn_Object = MibTableColumn
pmdge2CfgLabelclientPortn = _Pmdge2CfgLabelclientPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 9, 3, 1, 1, 3),
    _Pmdge2CfgLabelclientPortn_Type()
)
pmdge2CfgLabelclientPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmdge2CfgLabelclientPortn.setStatus("current")
_Pmdge2CfgLabellineTable_Object = MibTable
pmdge2CfgLabellineTable = _Pmdge2CfgLabellineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 9, 3, 2)
)
if mibBuilder.loadTexts:
    pmdge2CfgLabellineTable.setStatus("current")
_Pmdge2CfgLabellineEntry_Object = MibTableRow
pmdge2CfgLabellineEntry = _Pmdge2CfgLabellineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 9, 3, 2, 1)
)
pmdge2CfgLabellineEntry.setIndexNames(
    (0, "EKINOPS-PmDGE2-MIB", "pmdge2CfgLabellineIndex"),
)
if mibBuilder.loadTexts:
    pmdge2CfgLabellineEntry.setStatus("current")


class _Pmdge2CfgLabellineIndex_Type(Integer32):
    """Custom type pmdge2CfgLabellineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmdge2CfgLabellineIndex_Type.__name__ = "Integer32"
_Pmdge2CfgLabellineIndex_Object = MibTableColumn
pmdge2CfgLabellineIndex = _Pmdge2CfgLabellineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 9, 3, 2, 1, 1),
    _Pmdge2CfgLabellineIndex_Type()
)
pmdge2CfgLabellineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2CfgLabellineIndex.setStatus("current")


class _Pmdge2CfgLabellinePortn_Type(DisplayString):
    """Custom type pmdge2CfgLabellinePortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pmdge2CfgLabellinePortn_Type.__name__ = "DisplayString"
_Pmdge2CfgLabellinePortn_Object = MibTableColumn
pmdge2CfgLabellinePortn = _Pmdge2CfgLabellinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 9, 3, 2, 1, 3),
    _Pmdge2CfgLabellinePortn_Type()
)
pmdge2CfgLabellinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmdge2CfgLabellinePortn.setStatus("current")
_Pmdge2CfgWriteConfiguration_Type = EkiOnOff
_Pmdge2CfgWriteConfiguration_Object = MibScalar
pmdge2CfgWriteConfiguration = _Pmdge2CfgWriteConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 9, 257),
    _Pmdge2CfgWriteConfiguration_Type()
)
pmdge2CfgWriteConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmdge2CfgWriteConfiguration.setStatus("current")
_Pmdge2traps_ObjectIdentity = ObjectIdentity
pmdge2traps = _Pmdge2traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 65, 10)
)


class _Pmdge2trapBoardNumber_Type(Integer32):
    """Custom type pmdge2trapBoardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pmdge2trapBoardNumber_Type.__name__ = "Integer32"
_Pmdge2trapBoardNumber_Object = MibScalar
pmdge2trapBoardNumber = _Pmdge2trapBoardNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 65, 10, 4),
    _Pmdge2trapBoardNumber_Type()
)
pmdge2trapBoardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdge2trapBoardNumber.setStatus("current")

# Managed Objects groups


# Notification objects

pmdge2PowerTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 65, 10, 50)
)
pmdge2PowerTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-PmDGE2-MIB", "pmdge2AlmDefFuseB"),
        ("EKINOPS-PmDGE2-MIB", "pmdge2AlmDefFuseA"),
        ("EKINOPS-PmDGE2-MIB", "pmdge2trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmdge2PowerTrapUrgentGoesOn.setStatus(
        "current"
    )

pmdge2PowerTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 65, 10, 51)
)
pmdge2PowerTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-PmDGE2-MIB", "pmdge2AlmDefFuseB"),
        ("EKINOPS-PmDGE2-MIB", "pmdge2AlmDefFuseA"),
        ("EKINOPS-PmDGE2-MIB", "pmdge2trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmdge2PowerTrapUrgentGoesOff.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EKINOPS-PmDGE2-MIB",
    **{"Pmdge2Grid": Pmdge2Grid,
       "Pmdge2EqualizerMode": Pmdge2EqualizerMode,
       "Pmdge2EqualizerReference": Pmdge2EqualizerReference,
       "Pmdge2Channel": Pmdge2Channel,
       "modulepmdge2": modulepmdge2,
       "pmdge2alarms": pmdge2alarms,
       "pmdge2AlmOther": pmdge2AlmOther,
       "pmdge2AlmOtherNurg": pmdge2AlmOtherNurg,
       "pmdge2AlmswitchDegrade": pmdge2AlmswitchDegrade,
       "pmdge2AlmSwitchTempHighDeg": pmdge2AlmSwitchTempHighDeg,
       "pmdge2AlmequalizationStatus": pmdge2AlmequalizationStatus,
       "pmdge2AlmEqualizationFail": pmdge2AlmEqualizationFail,
       "pmdge2AlmEqualizationInprogress": pmdge2AlmEqualizationInprogress,
       "pmdge2AlmEqualizationComplete": pmdge2AlmEqualizationComplete,
       "pmdge2AlmEqualizationOff": pmdge2AlmEqualizationOff,
       "pmdge2AlmPowerOverRange": pmdge2AlmPowerOverRange,
       "pmdge2AlmAttenuationOverRange": pmdge2AlmAttenuationOverRange,
       "pmdge2AlmLossOfSpectrum": pmdge2AlmLossOfSpectrum,
       "pmdge2AlmOtherUrg": pmdge2AlmOtherUrg,
       "pmdge2AlmswitchAlarms": pmdge2AlmswitchAlarms,
       "pmdge2AlmSwitchTempHighAla": pmdge2AlmSwitchTempHighAla,
       "pmdge2AlmmoduleStatus": pmdge2AlmmoduleStatus,
       "pmdge2AlmSwitchNotReady": pmdge2AlmSwitchNotReady,
       "pmdge2AlmmoduleAlarms": pmdge2AlmmoduleAlarms,
       "pmdge2AlmModuleTempHighAla": pmdge2AlmModuleTempHighAla,
       "pmdge2AlmCaseTempHighAla": pmdge2AlmCaseTempHighAla,
       "pmdge2AlmmoduleDegrad": pmdge2AlmmoduleDegrad,
       "pmdge2AlmModuleTempHighDeg": pmdge2AlmModuleTempHighDeg,
       "pmdge2AlmCaseTempHighDeg": pmdge2AlmCaseTempHighDeg,
       "pmdge2AlmOtherCrit": pmdge2AlmOtherCrit,
       "pmdge2AlmsynthAlm0": pmdge2AlmsynthAlm0,
       "pmdge2AlmModuleGlobFailure": pmdge2AlmModuleGlobFailure,
       "pmdge2AlmDefFuseA": pmdge2AlmDefFuseA,
       "pmdge2AlmDefFuseB": pmdge2AlmDefFuseB,
       "pmdge2AlmsynthAlm7": pmdge2AlmsynthAlm7,
       "pmdge2AlmInitNotCompl": pmdge2AlmInitNotCompl,
       "pmdge2AlmSwitchDegrade": pmdge2AlmSwitchDegrade,
       "pmdge2AlmSwitchAlm": pmdge2AlmSwitchAlm,
       "pmdge2measures": pmdge2measures,
       "pmdge2MesrOther": pmdge2MesrOther,
       "pmdge2MesrswitchTemp": pmdge2MesrswitchTemp,
       "pmdge2MesrchannelLowestPowerValue": pmdge2MesrchannelLowestPowerValue,
       "pmdge2MesrchannelNumber": pmdge2MesrchannelNumber,
       "pmdge2MesrmoduleTemp": pmdge2MesrmoduleTemp,
       "pmdge2MesrtargetRequest": pmdge2MesrtargetRequest,
       "pmdge2MesrchannelPresenceThreshold": pmdge2MesrchannelPresenceThreshold,
       "pmdge2Mesrchannel1InputPwr": pmdge2Mesrchannel1InputPwr,
       "pmdge2Mesrchannel2InputPwr": pmdge2Mesrchannel2InputPwr,
       "pmdge2Mesrchannel3InputPwr": pmdge2Mesrchannel3InputPwr,
       "pmdge2Mesrchannel4InputPwr": pmdge2Mesrchannel4InputPwr,
       "pmdge2Mesrchannel5InputPwr": pmdge2Mesrchannel5InputPwr,
       "pmdge2Mesrchannel6InputPwr": pmdge2Mesrchannel6InputPwr,
       "pmdge2Mesrchannel7InputPwr": pmdge2Mesrchannel7InputPwr,
       "pmdge2Mesrchannel8InputPwr": pmdge2Mesrchannel8InputPwr,
       "pmdge2Mesrchannel9InputPwr": pmdge2Mesrchannel9InputPwr,
       "pmdge2Mesrchannel10InputPwr": pmdge2Mesrchannel10InputPwr,
       "pmdge2Mesrchannel11InputPwr": pmdge2Mesrchannel11InputPwr,
       "pmdge2Mesrchannel12InputPwr": pmdge2Mesrchannel12InputPwr,
       "pmdge2Mesrchannel13InputPwr": pmdge2Mesrchannel13InputPwr,
       "pmdge2Mesrchannel14InputPwr": pmdge2Mesrchannel14InputPwr,
       "pmdge2Mesrchannel15InputPwr": pmdge2Mesrchannel15InputPwr,
       "pmdge2Mesrchannel16InputPwr": pmdge2Mesrchannel16InputPwr,
       "pmdge2Mesrchannel17InputPwr": pmdge2Mesrchannel17InputPwr,
       "pmdge2Mesrchannel18InputPwr": pmdge2Mesrchannel18InputPwr,
       "pmdge2Mesrchannel19InputPwr": pmdge2Mesrchannel19InputPwr,
       "pmdge2Mesrchannel20InputPwr": pmdge2Mesrchannel20InputPwr,
       "pmdge2Mesrchannel21InputPwr": pmdge2Mesrchannel21InputPwr,
       "pmdge2Mesrchannel22InputPwr": pmdge2Mesrchannel22InputPwr,
       "pmdge2Mesrchannel23InputPwr": pmdge2Mesrchannel23InputPwr,
       "pmdge2Mesrchannel24InputPwr": pmdge2Mesrchannel24InputPwr,
       "pmdge2Mesrchannel25InputPwr": pmdge2Mesrchannel25InputPwr,
       "pmdge2Mesrchannel26InputPwr": pmdge2Mesrchannel26InputPwr,
       "pmdge2Mesrchannel27InputPwr": pmdge2Mesrchannel27InputPwr,
       "pmdge2Mesrchannel28InputPwr": pmdge2Mesrchannel28InputPwr,
       "pmdge2Mesrchannel29InputPwr": pmdge2Mesrchannel29InputPwr,
       "pmdge2Mesrchannel30InputPwr": pmdge2Mesrchannel30InputPwr,
       "pmdge2Mesrchannel31InputPwr": pmdge2Mesrchannel31InputPwr,
       "pmdge2Mesrchannel32InputPwr": pmdge2Mesrchannel32InputPwr,
       "pmdge2Mesrchannel33InputPwr": pmdge2Mesrchannel33InputPwr,
       "pmdge2Mesrchannel34InputPwr": pmdge2Mesrchannel34InputPwr,
       "pmdge2Mesrchannel35InputPwr": pmdge2Mesrchannel35InputPwr,
       "pmdge2Mesrchannel36InputPwr": pmdge2Mesrchannel36InputPwr,
       "pmdge2Mesrchannel37InputPwr": pmdge2Mesrchannel37InputPwr,
       "pmdge2Mesrchannel38InputPwr": pmdge2Mesrchannel38InputPwr,
       "pmdge2Mesrchannel39InputPwr": pmdge2Mesrchannel39InputPwr,
       "pmdge2Mesrchannel40InputPwr": pmdge2Mesrchannel40InputPwr,
       "pmdge2Mesrchannel41InputPwr": pmdge2Mesrchannel41InputPwr,
       "pmdge2Mesrchannel42InputPwr": pmdge2Mesrchannel42InputPwr,
       "pmdge2Mesrchannel43InputPwr": pmdge2Mesrchannel43InputPwr,
       "pmdge2Mesrchannel44InputPwr": pmdge2Mesrchannel44InputPwr,
       "pmdge2Mesrchannel45InputPwr": pmdge2Mesrchannel45InputPwr,
       "pmdge2Mesrchannel46InputPwr": pmdge2Mesrchannel46InputPwr,
       "pmdge2Mesrchannel47InputPwr": pmdge2Mesrchannel47InputPwr,
       "pmdge2Mesrchannel48InputPwr": pmdge2Mesrchannel48InputPwr,
       "pmdge2Mesrchannel49InputPwr": pmdge2Mesrchannel49InputPwr,
       "pmdge2Mesrchannel50InputPwr": pmdge2Mesrchannel50InputPwr,
       "pmdge2Mesrchannel51InputPwr": pmdge2Mesrchannel51InputPwr,
       "pmdge2Mesrchannel52InputPwr": pmdge2Mesrchannel52InputPwr,
       "pmdge2Mesrchannel53InputPwr": pmdge2Mesrchannel53InputPwr,
       "pmdge2Mesrchannel54InputPwr": pmdge2Mesrchannel54InputPwr,
       "pmdge2Mesrchannel55InputPwr": pmdge2Mesrchannel55InputPwr,
       "pmdge2Mesrchannel56InputPwr": pmdge2Mesrchannel56InputPwr,
       "pmdge2Mesrchannel57InputPwr": pmdge2Mesrchannel57InputPwr,
       "pmdge2Mesrchannel58InputPwr": pmdge2Mesrchannel58InputPwr,
       "pmdge2Mesrchannel59InputPwr": pmdge2Mesrchannel59InputPwr,
       "pmdge2Mesrchannel60InputPwr": pmdge2Mesrchannel60InputPwr,
       "pmdge2Mesrchannel61InputPwr": pmdge2Mesrchannel61InputPwr,
       "pmdge2Mesrchannel62InputPwr": pmdge2Mesrchannel62InputPwr,
       "pmdge2Mesrchannel63InputPwr": pmdge2Mesrchannel63InputPwr,
       "pmdge2Mesrchannel64InputPwr": pmdge2Mesrchannel64InputPwr,
       "pmdge2Mesrchannel65InputPwr": pmdge2Mesrchannel65InputPwr,
       "pmdge2Mesrchannel66InputPwr": pmdge2Mesrchannel66InputPwr,
       "pmdge2Mesrchannel67InputPwr": pmdge2Mesrchannel67InputPwr,
       "pmdge2Mesrchannel68InputPwr": pmdge2Mesrchannel68InputPwr,
       "pmdge2Mesrchannel69InputPwr": pmdge2Mesrchannel69InputPwr,
       "pmdge2Mesrchannel70InputPwr": pmdge2Mesrchannel70InputPwr,
       "pmdge2Mesrchannel71InputPwr": pmdge2Mesrchannel71InputPwr,
       "pmdge2Mesrchannel72InputPwr": pmdge2Mesrchannel72InputPwr,
       "pmdge2Mesrchannel73InputPwr": pmdge2Mesrchannel73InputPwr,
       "pmdge2Mesrchannel74InputPwr": pmdge2Mesrchannel74InputPwr,
       "pmdge2Mesrchannel75InputPwr": pmdge2Mesrchannel75InputPwr,
       "pmdge2Mesrchannel76InputPwr": pmdge2Mesrchannel76InputPwr,
       "pmdge2Mesrchannel77InputPwr": pmdge2Mesrchannel77InputPwr,
       "pmdge2Mesrchannel78InputPwr": pmdge2Mesrchannel78InputPwr,
       "pmdge2Mesrchannel79InputPwr": pmdge2Mesrchannel79InputPwr,
       "pmdge2Mesrchannel80InputPwr": pmdge2Mesrchannel80InputPwr,
       "pmdge2Mesrchannel81InputPwr": pmdge2Mesrchannel81InputPwr,
       "pmdge2Mesrchannel82InputPwr": pmdge2Mesrchannel82InputPwr,
       "pmdge2Mesrchannel83InputPwr": pmdge2Mesrchannel83InputPwr,
       "pmdge2Mesrchannel84InputPwr": pmdge2Mesrchannel84InputPwr,
       "pmdge2Mesrchannel85InputPwr": pmdge2Mesrchannel85InputPwr,
       "pmdge2Mesrchannel86InputPwr": pmdge2Mesrchannel86InputPwr,
       "pmdge2Mesrchannel87InputPwr": pmdge2Mesrchannel87InputPwr,
       "pmdge2Mesrchannel88InputPwr": pmdge2Mesrchannel88InputPwr,
       "pmdge2Mesrchannel1OutputPwr": pmdge2Mesrchannel1OutputPwr,
       "pmdge2Mesrchannel2OutputPwr": pmdge2Mesrchannel2OutputPwr,
       "pmdge2Mesrchannel3OutputPwr": pmdge2Mesrchannel3OutputPwr,
       "pmdge2Mesrchannel4OutputPwr": pmdge2Mesrchannel4OutputPwr,
       "pmdge2Mesrchannel5OutputPwr": pmdge2Mesrchannel5OutputPwr,
       "pmdge2Mesrchannel6OutputPwr": pmdge2Mesrchannel6OutputPwr,
       "pmdge2Mesrchannel7OutputPwr": pmdge2Mesrchannel7OutputPwr,
       "pmdge2Mesrchannel8OutputPwr": pmdge2Mesrchannel8OutputPwr,
       "pmdge2Mesrchannel9OutputPwr": pmdge2Mesrchannel9OutputPwr,
       "pmdge2Mesrchannel10OutputPwr": pmdge2Mesrchannel10OutputPwr,
       "pmdge2Mesrchannel11OutputPwr": pmdge2Mesrchannel11OutputPwr,
       "pmdge2Mesrchannel12OutputPwr": pmdge2Mesrchannel12OutputPwr,
       "pmdge2Mesrchannel13OutputPwr": pmdge2Mesrchannel13OutputPwr,
       "pmdge2Mesrchannel14OutputPwr": pmdge2Mesrchannel14OutputPwr,
       "pmdge2Mesrchannel15OutputPwr": pmdge2Mesrchannel15OutputPwr,
       "pmdge2Mesrchannel16OutputPwr": pmdge2Mesrchannel16OutputPwr,
       "pmdge2Mesrchannel17OutputPwr": pmdge2Mesrchannel17OutputPwr,
       "pmdge2Mesrchannel18OutputPwr": pmdge2Mesrchannel18OutputPwr,
       "pmdge2Mesrchannel19OutputPwr": pmdge2Mesrchannel19OutputPwr,
       "pmdge2Mesrchannel20OutputPwr": pmdge2Mesrchannel20OutputPwr,
       "pmdge2Mesrchannel21OutputPwr": pmdge2Mesrchannel21OutputPwr,
       "pmdge2Mesrchannel22OutputPwr": pmdge2Mesrchannel22OutputPwr,
       "pmdge2Mesrchannel23OutputPwr": pmdge2Mesrchannel23OutputPwr,
       "pmdge2Mesrchannel24OutputPwr": pmdge2Mesrchannel24OutputPwr,
       "pmdge2Mesrchannel25OutputPwr": pmdge2Mesrchannel25OutputPwr,
       "pmdge2Mesrchannel26OutputPwr": pmdge2Mesrchannel26OutputPwr,
       "pmdge2Mesrchannel27OutputPwr": pmdge2Mesrchannel27OutputPwr,
       "pmdge2Mesrchannel28OutputPwr": pmdge2Mesrchannel28OutputPwr,
       "pmdge2Mesrchannel29OutputPwr": pmdge2Mesrchannel29OutputPwr,
       "pmdge2Mesrchannel30OutputPwr": pmdge2Mesrchannel30OutputPwr,
       "pmdge2Mesrchannel31OutputPwr": pmdge2Mesrchannel31OutputPwr,
       "pmdge2Mesrchannel32OutputPwr": pmdge2Mesrchannel32OutputPwr,
       "pmdge2Mesrchannel33OutputPwr": pmdge2Mesrchannel33OutputPwr,
       "pmdge2Mesrchannel34OutputPwr": pmdge2Mesrchannel34OutputPwr,
       "pmdge2Mesrchannel35OutputPwr": pmdge2Mesrchannel35OutputPwr,
       "pmdge2Mesrchannel36OutputPwr": pmdge2Mesrchannel36OutputPwr,
       "pmdge2Mesrchannel37OutputPwr": pmdge2Mesrchannel37OutputPwr,
       "pmdge2Mesrchannel38OutputPwr": pmdge2Mesrchannel38OutputPwr,
       "pmdge2Mesrchannel39OutputPwr": pmdge2Mesrchannel39OutputPwr,
       "pmdge2Mesrchannel40OutputPwr": pmdge2Mesrchannel40OutputPwr,
       "pmdge2Mesrchannel41OutputPwr": pmdge2Mesrchannel41OutputPwr,
       "pmdge2Mesrchannel42OutputPwr": pmdge2Mesrchannel42OutputPwr,
       "pmdge2Mesrchannel43OutputPwr": pmdge2Mesrchannel43OutputPwr,
       "pmdge2Mesrchannel44OutputPwr": pmdge2Mesrchannel44OutputPwr,
       "pmdge2Mesrchannel45OutputPwr": pmdge2Mesrchannel45OutputPwr,
       "pmdge2Mesrchannel46OutputPwr": pmdge2Mesrchannel46OutputPwr,
       "pmdge2Mesrchannel47OutputPwr": pmdge2Mesrchannel47OutputPwr,
       "pmdge2Mesrchannel48OutputPwr": pmdge2Mesrchannel48OutputPwr,
       "pmdge2Mesrchannel49OutputPwr": pmdge2Mesrchannel49OutputPwr,
       "pmdge2Mesrchannel50OutputPwr": pmdge2Mesrchannel50OutputPwr,
       "pmdge2Mesrchannel51OutputPwr": pmdge2Mesrchannel51OutputPwr,
       "pmdge2Mesrchannel52OutputPwr": pmdge2Mesrchannel52OutputPwr,
       "pmdge2Mesrchannel53OutputPwr": pmdge2Mesrchannel53OutputPwr,
       "pmdge2Mesrchannel54OutputPwr": pmdge2Mesrchannel54OutputPwr,
       "pmdge2Mesrchannel55OutputPwr": pmdge2Mesrchannel55OutputPwr,
       "pmdge2Mesrchannel56OutputPwr": pmdge2Mesrchannel56OutputPwr,
       "pmdge2Mesrchannel57OutputPwr": pmdge2Mesrchannel57OutputPwr,
       "pmdge2Mesrchannel58OutputPwr": pmdge2Mesrchannel58OutputPwr,
       "pmdge2Mesrchannel59OutputPwr": pmdge2Mesrchannel59OutputPwr,
       "pmdge2Mesrchannel60OutputPwr": pmdge2Mesrchannel60OutputPwr,
       "pmdge2Mesrchannel61OutputPwr": pmdge2Mesrchannel61OutputPwr,
       "pmdge2Mesrchannel62OutputPwr": pmdge2Mesrchannel62OutputPwr,
       "pmdge2Mesrchannel63OutputPwr": pmdge2Mesrchannel63OutputPwr,
       "pmdge2Mesrchannel64OutputPwr": pmdge2Mesrchannel64OutputPwr,
       "pmdge2Mesrchannel65OutputPwr": pmdge2Mesrchannel65OutputPwr,
       "pmdge2Mesrchannel66OutputPwr": pmdge2Mesrchannel66OutputPwr,
       "pmdge2Mesrchannel67OutputPwr": pmdge2Mesrchannel67OutputPwr,
       "pmdge2Mesrchannel68OutputPwr": pmdge2Mesrchannel68OutputPwr,
       "pmdge2Mesrchannel69OutputPwr": pmdge2Mesrchannel69OutputPwr,
       "pmdge2Mesrchannel70OutputPwr": pmdge2Mesrchannel70OutputPwr,
       "pmdge2Mesrchannel71OutputPwr": pmdge2Mesrchannel71OutputPwr,
       "pmdge2Mesrchannel72OutputPwr": pmdge2Mesrchannel72OutputPwr,
       "pmdge2Mesrchannel73OutputPwr": pmdge2Mesrchannel73OutputPwr,
       "pmdge2Mesrchannel74OutputPwr": pmdge2Mesrchannel74OutputPwr,
       "pmdge2Mesrchannel75OutputPwr": pmdge2Mesrchannel75OutputPwr,
       "pmdge2Mesrchannel76OutputPwr": pmdge2Mesrchannel76OutputPwr,
       "pmdge2Mesrchannel77OutputPwr": pmdge2Mesrchannel77OutputPwr,
       "pmdge2Mesrchannel78OutputPwr": pmdge2Mesrchannel78OutputPwr,
       "pmdge2Mesrchannel79OutputPwr": pmdge2Mesrchannel79OutputPwr,
       "pmdge2Mesrchannel80OutputPwr": pmdge2Mesrchannel80OutputPwr,
       "pmdge2Mesrchannel81OutputPwr": pmdge2Mesrchannel81OutputPwr,
       "pmdge2Mesrchannel82OutputPwr": pmdge2Mesrchannel82OutputPwr,
       "pmdge2Mesrchannel83OutputPwr": pmdge2Mesrchannel83OutputPwr,
       "pmdge2Mesrchannel84OutputPwr": pmdge2Mesrchannel84OutputPwr,
       "pmdge2Mesrchannel85OutputPwr": pmdge2Mesrchannel85OutputPwr,
       "pmdge2Mesrchannel86OutputPwr": pmdge2Mesrchannel86OutputPwr,
       "pmdge2Mesrchannel87OutputPwr": pmdge2Mesrchannel87OutputPwr,
       "pmdge2Mesrchannel88OutputPwr": pmdge2Mesrchannel88OutputPwr,
       "pmdge2controlsWrite": pmdge2controlsWrite,
       "pmdge2CtrlOther": pmdge2CtrlOther,
       "pmdge2Ctrlsynth0": pmdge2Ctrlsynth0,
       "pmdge2CtrlConfLoad": pmdge2CtrlConfLoad,
       "pmdge2CtrlConfFlash": pmdge2CtrlConfFlash,
       "pmdge2CtrlConfClear": pmdge2CtrlConfClear,
       "pmdge2Ctrlsynth4": pmdge2Ctrlsynth4,
       "pmdge2CtrlCorrelatOn": pmdge2CtrlCorrelatOn,
       "pmdge2CtrlCorrelatOff": pmdge2CtrlCorrelatOff,
       "pmdge2CtrlswMgnt": pmdge2CtrlswMgnt,
       "pmdge2CtrlColdReset": pmdge2CtrlColdReset,
       "pmdge2CtrlWarmReset": pmdge2CtrlWarmReset,
       "pmdge2CtrlswitchCtrl": pmdge2CtrlswitchCtrl,
       "pmdge2CtrlAllChannelsHighLoss": pmdge2CtrlAllChannelsHighLoss,
       "pmdge2CtrlmanualStart": pmdge2CtrlmanualStart,
       "pmdge2CtrlManualStart": pmdge2CtrlManualStart,
       "pmdge2CtrlledTest": pmdge2CtrlledTest,
       "pmdge2CtrlGreenLed": pmdge2CtrlGreenLed,
       "pmdge2CtrlRedLed": pmdge2CtrlRedLed,
       "pmdge2CtrlLedOff": pmdge2CtrlLedOff,
       "pmdge2CtrlEqualizer": pmdge2CtrlEqualizer,
       "pmdge2CtrlLine": pmdge2CtrlLine,
       "pmdge2ri": pmdge2ri,
       "pmdge2riTable": pmdge2riTable,
       "pmdge2RinvPortTable": pmdge2RinvPortTable,
       "pmdge2RinvPortEntry": pmdge2RinvPortEntry,
       "pmdge2RinvPortIndex": pmdge2RinvPortIndex,
       "pmdge2RinvPort": pmdge2RinvPort,
       "pmdge2RinvLineTable": pmdge2RinvLineTable,
       "pmdge2RinvLineEntry": pmdge2RinvLineEntry,
       "pmdge2RinvLineIndex": pmdge2RinvLineIndex,
       "pmdge2RinvxfpLine": pmdge2RinvxfpLine,
       "pmdge2RinvReloadInventory": pmdge2RinvReloadInventory,
       "pmdge2RinvHwPlatform": pmdge2RinvHwPlatform,
       "pmdge2RinvSwPlatform": pmdge2RinvSwPlatform,
       "pmdge2Config": pmdge2Config,
       "pmdge2CfgLsd": pmdge2CfgLsd,
       "pmdge2tableclientLsd": pmdge2tableclientLsd,
       "pmdge2CfgStartup": pmdge2CfgStartup,
       "pmdge2tableother": pmdge2tableother,
       "pmdge2Cfggrid": pmdge2Cfggrid,
       "pmdge2CfgequalizationReference": pmdge2CfgequalizationReference,
       "pmdge2CfgequalizationMode": pmdge2CfgequalizationMode,
       "pmdge2CfgchannelPowerRefValue": pmdge2CfgchannelPowerRefValue,
       "pmdge2CfgchannelPresenceThreshold": pmdge2CfgchannelPresenceThreshold,
       "pmdge2CfgmonitoringPortAtt": pmdge2CfgmonitoringPortAtt,
       "pmdge2CfgscanningPeriod": pmdge2CfgscanningPeriod,
       "pmdge2tableother1": pmdge2tableother1,
       "pmdge2CfgcomponentType": pmdge2CfgcomponentType,
       "pmdge2Cfgmiscellaneous": pmdge2Cfgmiscellaneous,
       "pmdge2CfgfirstChannel": pmdge2CfgfirstChannel,
       "pmdge2CfglastChannel": pmdge2CfglastChannel,
       "pmdge2CfggridUsed": pmdge2CfggridUsed,
       "pmdge2CfgLabels": pmdge2CfgLabels,
       "pmdge2CfgLabelclientTable": pmdge2CfgLabelclientTable,
       "pmdge2CfgLabelclientEntry": pmdge2CfgLabelclientEntry,
       "pmdge2CfgLabelclientIndex": pmdge2CfgLabelclientIndex,
       "pmdge2CfgLabelclientPortn": pmdge2CfgLabelclientPortn,
       "pmdge2CfgLabellineTable": pmdge2CfgLabellineTable,
       "pmdge2CfgLabellineEntry": pmdge2CfgLabellineEntry,
       "pmdge2CfgLabellineIndex": pmdge2CfgLabellineIndex,
       "pmdge2CfgLabellinePortn": pmdge2CfgLabellinePortn,
       "pmdge2CfgWriteConfiguration": pmdge2CfgWriteConfiguration,
       "pmdge2traps": pmdge2traps,
       "pmdge2trapBoardNumber": pmdge2trapBoardNumber,
       "pmdge2PowerTrapUrgentGoesOn": pmdge2PowerTrapUrgentGoesOn,
       "pmdge2PowerTrapUrgentGoesOff": pmdge2PowerTrapUrgentGoesOff}
)
