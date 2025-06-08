# SNMP MIB module (EKINOPS-PmDGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ekinops_20044/EKINOPS-PmDGE-MIB.mib
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

modulepmdge = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 56)
)
if mibBuilder.loadTexts:
    modulepmdge.setRevisions(
        ("2012-10-16 00:00",
         "2013-03-28 00:00",
         "2014-03-26 00:00",
         "2014-11-25 00:00",
         "2016-05-23 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PmdgeGrid(TextualConvention, Integer32):
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
        *(("dgegrid50", 50),
          ("dgegrid100", 100),
          ("dgegrid200", 200))
    )



class PmdgePlanNumber(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              7)
        )
    )
    namedValues = NamedValues(
        *(("workingPlan", 0),
          ("savedPlan1", 1),
          ("savedPlan2", 2),
          ("usedPlan", 7))
    )



class PmdgeChannel(TextualConvention, Integer32):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_Pmdgealarms_ObjectIdentity = ObjectIdentity
pmdgealarms = _Pmdgealarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 56, 2)
)
_PmdgeAlmOther_ObjectIdentity = ObjectIdentity
pmdgeAlmOther = _PmdgeAlmOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 56, 2, 1)
)
_PmdgeAlmOtherNurg_ObjectIdentity = ObjectIdentity
pmdgeAlmOtherNurg = _PmdgeAlmOtherNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 56, 2, 1, 1)
)
_PmdgeAlmswitchDegrade_ObjectIdentity = ObjectIdentity
pmdgeAlmswitchDegrade = _PmdgeAlmswitchDegrade_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 56, 2, 1, 1, 17)
)
_PmdgeAlmSwitchTempHighDeg_Type = EkiOnOff
_PmdgeAlmSwitchTempHighDeg_Object = MibScalar
pmdgeAlmSwitchTempHighDeg = _PmdgeAlmSwitchTempHighDeg_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 2, 1, 1, 17, 2),
    _PmdgeAlmSwitchTempHighDeg_Type()
)
pmdgeAlmSwitchTempHighDeg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdgeAlmSwitchTempHighDeg.setStatus("current")
_PmdgeAlmOtherUrg_ObjectIdentity = ObjectIdentity
pmdgeAlmOtherUrg = _PmdgeAlmOtherUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 56, 2, 1, 2)
)
_PmdgeAlmswitchAlarms_ObjectIdentity = ObjectIdentity
pmdgeAlmswitchAlarms = _PmdgeAlmswitchAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 56, 2, 1, 2, 16)
)
_PmdgeAlmSwitchTempHighAla_Type = EkiOnOff
_PmdgeAlmSwitchTempHighAla_Object = MibScalar
pmdgeAlmSwitchTempHighAla = _PmdgeAlmSwitchTempHighAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 2, 1, 2, 16, 2),
    _PmdgeAlmSwitchTempHighAla_Type()
)
pmdgeAlmSwitchTempHighAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdgeAlmSwitchTempHighAla.setStatus("current")
_PmdgeAlmmoduleStatus_ObjectIdentity = ObjectIdentity
pmdgeAlmmoduleStatus = _PmdgeAlmmoduleStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 56, 2, 1, 2, 66)
)
_PmdgeAlmColdReset_Type = EkiOnOff
_PmdgeAlmColdReset_Object = MibScalar
pmdgeAlmColdReset = _PmdgeAlmColdReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 2, 1, 2, 66, 1),
    _PmdgeAlmColdReset_Type()
)
pmdgeAlmColdReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdgeAlmColdReset.setStatus("current")
_PmdgeAlmWarmReset_Type = EkiOnOff
_PmdgeAlmWarmReset_Object = MibScalar
pmdgeAlmWarmReset = _PmdgeAlmWarmReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 2, 1, 2, 66, 2),
    _PmdgeAlmWarmReset_Type()
)
pmdgeAlmWarmReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdgeAlmWarmReset.setStatus("current")
_PmdgeAlmHotReset_Type = EkiOnOff
_PmdgeAlmHotReset_Object = MibScalar
pmdgeAlmHotReset = _PmdgeAlmHotReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 2, 1, 2, 66, 3),
    _PmdgeAlmHotReset_Type()
)
pmdgeAlmHotReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdgeAlmHotReset.setStatus("current")
_PmdgeAlmSwitchNotReady_Type = EkiOnOff
_PmdgeAlmSwitchNotReady_Object = MibScalar
pmdgeAlmSwitchNotReady = _PmdgeAlmSwitchNotReady_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 2, 1, 2, 66, 5),
    _PmdgeAlmSwitchNotReady_Type()
)
pmdgeAlmSwitchNotReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdgeAlmSwitchNotReady.setStatus("current")
_PmdgeAlmmoduleAlarms_ObjectIdentity = ObjectIdentity
pmdgeAlmmoduleAlarms = _PmdgeAlmmoduleAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 56, 2, 1, 2, 67)
)
_PmdgeAlmModuleTempHighAla_Type = EkiOnOff
_PmdgeAlmModuleTempHighAla_Object = MibScalar
pmdgeAlmModuleTempHighAla = _PmdgeAlmModuleTempHighAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 2, 1, 2, 67, 2),
    _PmdgeAlmModuleTempHighAla_Type()
)
pmdgeAlmModuleTempHighAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdgeAlmModuleTempHighAla.setStatus("current")
_PmdgeAlmCaseTempHighAla_Type = EkiOnOff
_PmdgeAlmCaseTempHighAla_Object = MibScalar
pmdgeAlmCaseTempHighAla = _PmdgeAlmCaseTempHighAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 2, 1, 2, 67, 4),
    _PmdgeAlmCaseTempHighAla_Type()
)
pmdgeAlmCaseTempHighAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdgeAlmCaseTempHighAla.setStatus("current")
_PmdgeAlmmoduleDegrad_ObjectIdentity = ObjectIdentity
pmdgeAlmmoduleDegrad = _PmdgeAlmmoduleDegrad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 56, 2, 1, 2, 68)
)
_PmdgeAlmModuleTempHighDeg_Type = EkiOnOff
_PmdgeAlmModuleTempHighDeg_Object = MibScalar
pmdgeAlmModuleTempHighDeg = _PmdgeAlmModuleTempHighDeg_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 2, 1, 2, 68, 2),
    _PmdgeAlmModuleTempHighDeg_Type()
)
pmdgeAlmModuleTempHighDeg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdgeAlmModuleTempHighDeg.setStatus("current")
_PmdgeAlmCaseTempHighDeg_Type = EkiOnOff
_PmdgeAlmCaseTempHighDeg_Object = MibScalar
pmdgeAlmCaseTempHighDeg = _PmdgeAlmCaseTempHighDeg_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 2, 1, 2, 68, 4),
    _PmdgeAlmCaseTempHighDeg_Type()
)
pmdgeAlmCaseTempHighDeg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdgeAlmCaseTempHighDeg.setStatus("current")
_PmdgeAlmOtherCrit_ObjectIdentity = ObjectIdentity
pmdgeAlmOtherCrit = _PmdgeAlmOtherCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 56, 2, 1, 3)
)
_PmdgeAlmsynthAlm0_ObjectIdentity = ObjectIdentity
pmdgeAlmsynthAlm0 = _PmdgeAlmsynthAlm0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 56, 2, 1, 3, 0)
)
_PmdgeAlmInServiceNotReady_Type = EkiOnOff
_PmdgeAlmInServiceNotReady_Object = MibScalar
pmdgeAlmInServiceNotReady = _PmdgeAlmInServiceNotReady_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 2, 1, 3, 0, 1),
    _PmdgeAlmInServiceNotReady_Type()
)
pmdgeAlmInServiceNotReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdgeAlmInServiceNotReady.setStatus("current")
_PmdgeAlmModuleGlobFailure_Type = EkiOnOff
_PmdgeAlmModuleGlobFailure_Object = MibScalar
pmdgeAlmModuleGlobFailure = _PmdgeAlmModuleGlobFailure_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 2, 1, 3, 0, 9),
    _PmdgeAlmModuleGlobFailure_Type()
)
pmdgeAlmModuleGlobFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdgeAlmModuleGlobFailure.setStatus("current")
_PmdgeAlmDefFuseA_Type = EkiOnOff
_PmdgeAlmDefFuseA_Object = MibScalar
pmdgeAlmDefFuseA = _PmdgeAlmDefFuseA_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 2, 1, 3, 0, 15),
    _PmdgeAlmDefFuseA_Type()
)
pmdgeAlmDefFuseA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdgeAlmDefFuseA.setStatus("current")
_PmdgeAlmDefFuseB_Type = EkiOnOff
_PmdgeAlmDefFuseB_Object = MibScalar
pmdgeAlmDefFuseB = _PmdgeAlmDefFuseB_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 2, 1, 3, 0, 16),
    _PmdgeAlmDefFuseB_Type()
)
pmdgeAlmDefFuseB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdgeAlmDefFuseB.setStatus("current")
_PmdgeAlmsynthAlm7_ObjectIdentity = ObjectIdentity
pmdgeAlmsynthAlm7 = _PmdgeAlmsynthAlm7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 56, 2, 1, 3, 7)
)
_PmdgeAlmInitNotCompl_Type = EkiOnOff
_PmdgeAlmInitNotCompl_Object = MibScalar
pmdgeAlmInitNotCompl = _PmdgeAlmInitNotCompl_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 2, 1, 3, 7, 2),
    _PmdgeAlmInitNotCompl_Type()
)
pmdgeAlmInitNotCompl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdgeAlmInitNotCompl.setStatus("current")
_PmdgeAlmSwitchDegrade_Type = EkiOnOff
_PmdgeAlmSwitchDegrade_Object = MibScalar
pmdgeAlmSwitchDegrade = _PmdgeAlmSwitchDegrade_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 2, 1, 3, 7, 9),
    _PmdgeAlmSwitchDegrade_Type()
)
pmdgeAlmSwitchDegrade.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdgeAlmSwitchDegrade.setStatus("current")
_PmdgeAlmSwitchAlm_Type = EkiOnOff
_PmdgeAlmSwitchAlm_Object = MibScalar
pmdgeAlmSwitchAlm = _PmdgeAlmSwitchAlm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 2, 1, 3, 7, 10),
    _PmdgeAlmSwitchAlm_Type()
)
pmdgeAlmSwitchAlm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdgeAlmSwitchAlm.setStatus("current")
_Pmdgemeasures_ObjectIdentity = ObjectIdentity
pmdgemeasures = _Pmdgemeasures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 56, 3)
)
_PmdgeMesrOther_ObjectIdentity = ObjectIdentity
pmdgeMesrOther = _PmdgeMesrOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 56, 3, 1)
)


class _PmdgeMesrswitchTemp_Type(Unsigned32):
    """Custom type pmdgeMesrswitchTemp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmdgeMesrswitchTemp_Type.__name__ = "Unsigned32"
_PmdgeMesrswitchTemp_Object = MibScalar
pmdgeMesrswitchTemp = _PmdgeMesrswitchTemp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 3, 1, 16),
    _PmdgeMesrswitchTemp_Type()
)
pmdgeMesrswitchTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdgeMesrswitchTemp.setStatus("current")


class _PmdgeMesrmoduleTemp_Type(Unsigned32):
    """Custom type pmdgeMesrmoduleTemp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmdgeMesrmoduleTemp_Type.__name__ = "Unsigned32"
_PmdgeMesrmoduleTemp_Object = MibScalar
pmdgeMesrmoduleTemp = _PmdgeMesrmoduleTemp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 3, 1, 64),
    _PmdgeMesrmoduleTemp_Type()
)
pmdgeMesrmoduleTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdgeMesrmoduleTemp.setStatus("current")


class _PmdgeMesrcaseTemp_Type(Unsigned32):
    """Custom type pmdgeMesrcaseTemp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmdgeMesrcaseTemp_Type.__name__ = "Unsigned32"
_PmdgeMesrcaseTemp_Object = MibScalar
pmdgeMesrcaseTemp = _PmdgeMesrcaseTemp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 3, 1, 65),
    _PmdgeMesrcaseTemp_Type()
)
pmdgeMesrcaseTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdgeMesrcaseTemp.setStatus("current")
_PmdgecontrolsWrite_ObjectIdentity = ObjectIdentity
pmdgecontrolsWrite = _PmdgecontrolsWrite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 56, 6)
)
_PmdgeCtrlOther_ObjectIdentity = ObjectIdentity
pmdgeCtrlOther = _PmdgeCtrlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 56, 6, 1)
)
_PmdgeCtrlsynth0_ObjectIdentity = ObjectIdentity
pmdgeCtrlsynth0 = _PmdgeCtrlsynth0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 56, 6, 1, 0)
)
_PmdgeCtrlConfLoad_Type = EkiOnOff
_PmdgeCtrlConfLoad_Object = MibScalar
pmdgeCtrlConfLoad = _PmdgeCtrlConfLoad_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 6, 1, 0, 1),
    _PmdgeCtrlConfLoad_Type()
)
pmdgeCtrlConfLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmdgeCtrlConfLoad.setStatus("current")
_PmdgeCtrlConfFlash_Type = EkiOnOff
_PmdgeCtrlConfFlash_Object = MibScalar
pmdgeCtrlConfFlash = _PmdgeCtrlConfFlash_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 6, 1, 0, 9),
    _PmdgeCtrlConfFlash_Type()
)
pmdgeCtrlConfFlash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmdgeCtrlConfFlash.setStatus("current")
_PmdgeCtrlConfClear_Type = EkiOnOff
_PmdgeCtrlConfClear_Object = MibScalar
pmdgeCtrlConfClear = _PmdgeCtrlConfClear_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 6, 1, 0, 13),
    _PmdgeCtrlConfClear_Type()
)
pmdgeCtrlConfClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmdgeCtrlConfClear.setStatus("current")
_PmdgeCtrlsynth4_ObjectIdentity = ObjectIdentity
pmdgeCtrlsynth4 = _PmdgeCtrlsynth4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 56, 6, 1, 4)
)
_PmdgeCtrlCorrelatOn_Type = EkiOnOff
_PmdgeCtrlCorrelatOn_Object = MibScalar
pmdgeCtrlCorrelatOn = _PmdgeCtrlCorrelatOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 6, 1, 4, 1),
    _PmdgeCtrlCorrelatOn_Type()
)
pmdgeCtrlCorrelatOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmdgeCtrlCorrelatOn.setStatus("current")
_PmdgeCtrlCorrelatOff_Type = EkiOnOff
_PmdgeCtrlCorrelatOff_Object = MibScalar
pmdgeCtrlCorrelatOff = _PmdgeCtrlCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 6, 1, 4, 2),
    _PmdgeCtrlCorrelatOff_Type()
)
pmdgeCtrlCorrelatOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmdgeCtrlCorrelatOff.setStatus("current")
_PmdgeCtrlswMgnt_ObjectIdentity = ObjectIdentity
pmdgeCtrlswMgnt = _PmdgeCtrlswMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 56, 6, 1, 5)
)
_PmdgeCtrlColdReset_Type = EkiOnOff
_PmdgeCtrlColdReset_Object = MibScalar
pmdgeCtrlColdReset = _PmdgeCtrlColdReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 6, 1, 5, 2),
    _PmdgeCtrlColdReset_Type()
)
pmdgeCtrlColdReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmdgeCtrlColdReset.setStatus("current")
_PmdgeCtrlWarmReset_Type = EkiOnOff
_PmdgeCtrlWarmReset_Object = MibScalar
pmdgeCtrlWarmReset = _PmdgeCtrlWarmReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 6, 1, 5, 3),
    _PmdgeCtrlWarmReset_Type()
)
pmdgeCtrlWarmReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmdgeCtrlWarmReset.setStatus("current")
_PmdgeCtrlswitchCtrl_ObjectIdentity = ObjectIdentity
pmdgeCtrlswitchCtrl = _PmdgeCtrlswitchCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 56, 6, 1, 16)
)
_PmdgeCtrlAllChannelsHighLoss_Type = EkiOnOff
_PmdgeCtrlAllChannelsHighLoss_Object = MibScalar
pmdgeCtrlAllChannelsHighLoss = _PmdgeCtrlAllChannelsHighLoss_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 6, 1, 16, 1),
    _PmdgeCtrlAllChannelsHighLoss_Type()
)
pmdgeCtrlAllChannelsHighLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmdgeCtrlAllChannelsHighLoss.setStatus("current")


class _PmdgeCtrlcraftSynch_Type(Unsigned32):
    """Custom type pmdgeCtrlcraftSynch based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmdgeCtrlcraftSynch_Type.__name__ = "Unsigned32"
_PmdgeCtrlcraftSynch_Object = MibScalar
pmdgeCtrlcraftSynch = _PmdgeCtrlcraftSynch_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 6, 1, 17),
    _PmdgeCtrlcraftSynch_Type()
)
pmdgeCtrlcraftSynch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmdgeCtrlcraftSynch.setStatus("current")
_PmdgeCtrlledTest_ObjectIdentity = ObjectIdentity
pmdgeCtrlledTest = _PmdgeCtrlledTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 56, 6, 1, 64)
)
_PmdgeCtrlGreenLed_Type = EkiOnOff
_PmdgeCtrlGreenLed_Object = MibScalar
pmdgeCtrlGreenLed = _PmdgeCtrlGreenLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 6, 1, 64, 1),
    _PmdgeCtrlGreenLed_Type()
)
pmdgeCtrlGreenLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmdgeCtrlGreenLed.setStatus("current")
_PmdgeCtrlRedLed_Type = EkiOnOff
_PmdgeCtrlRedLed_Object = MibScalar
pmdgeCtrlRedLed = _PmdgeCtrlRedLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 6, 1, 64, 2),
    _PmdgeCtrlRedLed_Type()
)
pmdgeCtrlRedLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmdgeCtrlRedLed.setStatus("current")
_PmdgeCtrlLedOff_Type = EkiOnOff
_PmdgeCtrlLedOff_Object = MibScalar
pmdgeCtrlLedOff = _PmdgeCtrlLedOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 6, 1, 64, 3),
    _PmdgeCtrlLedOff_Type()
)
pmdgeCtrlLedOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmdgeCtrlLedOff.setStatus("current")
_PmdgeCtrlwavePlanAssignmentsRefreshTable_Object = MibTable
pmdgeCtrlwavePlanAssignmentsRefreshTable = _PmdgeCtrlwavePlanAssignmentsRefreshTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 6, 1, 65)
)
if mibBuilder.loadTexts:
    pmdgeCtrlwavePlanAssignmentsRefreshTable.setStatus("current")
_PmdgeCtrlwavePlanAssignmentsRefreshEntry_Object = MibTableRow
pmdgeCtrlwavePlanAssignmentsRefreshEntry = _PmdgeCtrlwavePlanAssignmentsRefreshEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 6, 1, 65, 1)
)
pmdgeCtrlwavePlanAssignmentsRefreshEntry.setIndexNames(
    (0, "EKINOPS-PmDGE-MIB", "pmdgeCtrlwavePlanAssignmentsRefreshIndex"),
)
if mibBuilder.loadTexts:
    pmdgeCtrlwavePlanAssignmentsRefreshEntry.setStatus("current")


class _PmdgeCtrlwavePlanAssignmentsRefreshIndex_Type(Integer32):
    """Custom type pmdgeCtrlwavePlanAssignmentsRefreshIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_PmdgeCtrlwavePlanAssignmentsRefreshIndex_Type.__name__ = "Integer32"
_PmdgeCtrlwavePlanAssignmentsRefreshIndex_Object = MibTableColumn
pmdgeCtrlwavePlanAssignmentsRefreshIndex = _PmdgeCtrlwavePlanAssignmentsRefreshIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 6, 1, 65, 1, 1),
    _PmdgeCtrlwavePlanAssignmentsRefreshIndex_Type()
)
pmdgeCtrlwavePlanAssignmentsRefreshIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdgeCtrlwavePlanAssignmentsRefreshIndex.setStatus("current")
_PmdgeCtrlWaveStatusRefreshPortn_Type = EkiOnOff
_PmdgeCtrlWaveStatusRefreshPortn_Object = MibTableColumn
pmdgeCtrlWaveStatusRefreshPortn = _PmdgeCtrlWaveStatusRefreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 6, 1, 65, 1, 2),
    _PmdgeCtrlWaveStatusRefreshPortn_Type()
)
pmdgeCtrlWaveStatusRefreshPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdgeCtrlWaveStatusRefreshPortn.setStatus("current")
_PmdgeCtrlWaveNarrowingRefreshPortn_Type = Integer32
_PmdgeCtrlWaveNarrowingRefreshPortn_Object = MibTableColumn
pmdgeCtrlWaveNarrowingRefreshPortn = _PmdgeCtrlWaveNarrowingRefreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 6, 1, 65, 1, 3),
    _PmdgeCtrlWaveNarrowingRefreshPortn_Type()
)
pmdgeCtrlWaveNarrowingRefreshPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdgeCtrlWaveNarrowingRefreshPortn.setStatus("current")
_PmdgeCtrlWaveCenterFrequencyRefreshPortn_Type = Integer32
_PmdgeCtrlWaveCenterFrequencyRefreshPortn_Object = MibTableColumn
pmdgeCtrlWaveCenterFrequencyRefreshPortn = _PmdgeCtrlWaveCenterFrequencyRefreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 6, 1, 65, 1, 4),
    _PmdgeCtrlWaveCenterFrequencyRefreshPortn_Type()
)
pmdgeCtrlWaveCenterFrequencyRefreshPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdgeCtrlWaveCenterFrequencyRefreshPortn.setStatus("current")
_PmdgeCtrlWaveOOSRefreshPortn_Type = EkiOnOff
_PmdgeCtrlWaveOOSRefreshPortn_Object = MibTableColumn
pmdgeCtrlWaveOOSRefreshPortn = _PmdgeCtrlWaveOOSRefreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 6, 1, 65, 1, 5),
    _PmdgeCtrlWaveOOSRefreshPortn_Type()
)
pmdgeCtrlWaveOOSRefreshPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdgeCtrlWaveOOSRefreshPortn.setStatus("current")
_PmdgeCtrlWaveAttenuationRefreshPortn_Type = Integer32
_PmdgeCtrlWaveAttenuationRefreshPortn_Object = MibTableColumn
pmdgeCtrlWaveAttenuationRefreshPortn = _PmdgeCtrlWaveAttenuationRefreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 6, 1, 65, 1, 6),
    _PmdgeCtrlWaveAttenuationRefreshPortn_Type()
)
pmdgeCtrlWaveAttenuationRefreshPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdgeCtrlWaveAttenuationRefreshPortn.setStatus("current")
_PmdgeCtrlWaveItuRefreshPortn_Type = DisplayString
_PmdgeCtrlWaveItuRefreshPortn_Object = MibTableColumn
pmdgeCtrlWaveItuRefreshPortn = _PmdgeCtrlWaveItuRefreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 6, 1, 65, 1, 7),
    _PmdgeCtrlWaveItuRefreshPortn_Type()
)
pmdgeCtrlWaveItuRefreshPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdgeCtrlWaveItuRefreshPortn.setStatus("current")
_PmdgeCtrlWaveDegreeRefreshPortn_Type = Integer32
_PmdgeCtrlWaveDegreeRefreshPortn_Object = MibTableColumn
pmdgeCtrlWaveDegreeRefreshPortn = _PmdgeCtrlWaveDegreeRefreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 6, 1, 65, 1, 8),
    _PmdgeCtrlWaveDegreeRefreshPortn_Type()
)
pmdgeCtrlWaveDegreeRefreshPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdgeCtrlWaveDegreeRefreshPortn.setStatus("current")
_PmdgeCtrlUsageRefreshPortn_Type = EkiOnOff
_PmdgeCtrlUsageRefreshPortn_Object = MibTableColumn
pmdgeCtrlUsageRefreshPortn = _PmdgeCtrlUsageRefreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 6, 1, 65, 1, 16),
    _PmdgeCtrlUsageRefreshPortn_Type()
)
pmdgeCtrlUsageRefreshPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdgeCtrlUsageRefreshPortn.setStatus("current")
_PmdgeCtrlwavePlanAssignmentsWorkTable_Object = MibTable
pmdgeCtrlwavePlanAssignmentsWorkTable = _PmdgeCtrlwavePlanAssignmentsWorkTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 6, 1, 66)
)
if mibBuilder.loadTexts:
    pmdgeCtrlwavePlanAssignmentsWorkTable.setStatus("current")
_PmdgeCtrlwavePlanAssignmentsWorkEntry_Object = MibTableRow
pmdgeCtrlwavePlanAssignmentsWorkEntry = _PmdgeCtrlwavePlanAssignmentsWorkEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 6, 1, 66, 1)
)
pmdgeCtrlwavePlanAssignmentsWorkEntry.setIndexNames(
    (0, "EKINOPS-PmDGE-MIB", "pmdgeCtrlwavePlanAssignmentsWorkIndex"),
)
if mibBuilder.loadTexts:
    pmdgeCtrlwavePlanAssignmentsWorkEntry.setStatus("current")


class _PmdgeCtrlwavePlanAssignmentsWorkIndex_Type(Integer32):
    """Custom type pmdgeCtrlwavePlanAssignmentsWorkIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_PmdgeCtrlwavePlanAssignmentsWorkIndex_Type.__name__ = "Integer32"
_PmdgeCtrlwavePlanAssignmentsWorkIndex_Object = MibTableColumn
pmdgeCtrlwavePlanAssignmentsWorkIndex = _PmdgeCtrlwavePlanAssignmentsWorkIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 6, 1, 66, 1, 1),
    _PmdgeCtrlwavePlanAssignmentsWorkIndex_Type()
)
pmdgeCtrlwavePlanAssignmentsWorkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdgeCtrlwavePlanAssignmentsWorkIndex.setStatus("current")
_PmdgeCtrlWaveStatusWorkPortn_Type = EkiOnOff
_PmdgeCtrlWaveStatusWorkPortn_Object = MibTableColumn
pmdgeCtrlWaveStatusWorkPortn = _PmdgeCtrlWaveStatusWorkPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 6, 1, 66, 1, 2),
    _PmdgeCtrlWaveStatusWorkPortn_Type()
)
pmdgeCtrlWaveStatusWorkPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmdgeCtrlWaveStatusWorkPortn.setStatus("current")
_PmdgeCtrlWaveNarrowingWorkPortn_Type = Integer32
_PmdgeCtrlWaveNarrowingWorkPortn_Object = MibTableColumn
pmdgeCtrlWaveNarrowingWorkPortn = _PmdgeCtrlWaveNarrowingWorkPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 6, 1, 66, 1, 3),
    _PmdgeCtrlWaveNarrowingWorkPortn_Type()
)
pmdgeCtrlWaveNarrowingWorkPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmdgeCtrlWaveNarrowingWorkPortn.setStatus("current")
_PmdgeCtrlWaveCenterFrequencyWorkPortn_Type = Integer32
_PmdgeCtrlWaveCenterFrequencyWorkPortn_Object = MibTableColumn
pmdgeCtrlWaveCenterFrequencyWorkPortn = _PmdgeCtrlWaveCenterFrequencyWorkPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 6, 1, 66, 1, 4),
    _PmdgeCtrlWaveCenterFrequencyWorkPortn_Type()
)
pmdgeCtrlWaveCenterFrequencyWorkPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmdgeCtrlWaveCenterFrequencyWorkPortn.setStatus("current")
_PmdgeCtrlWaveOOSWorkPortn_Type = EkiOnOff
_PmdgeCtrlWaveOOSWorkPortn_Object = MibTableColumn
pmdgeCtrlWaveOOSWorkPortn = _PmdgeCtrlWaveOOSWorkPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 6, 1, 66, 1, 5),
    _PmdgeCtrlWaveOOSWorkPortn_Type()
)
pmdgeCtrlWaveOOSWorkPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmdgeCtrlWaveOOSWorkPortn.setStatus("current")
_PmdgeCtrlWaveAttenuationWorkPortn_Type = Integer32
_PmdgeCtrlWaveAttenuationWorkPortn_Object = MibTableColumn
pmdgeCtrlWaveAttenuationWorkPortn = _PmdgeCtrlWaveAttenuationWorkPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 6, 1, 66, 1, 6),
    _PmdgeCtrlWaveAttenuationWorkPortn_Type()
)
pmdgeCtrlWaveAttenuationWorkPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmdgeCtrlWaveAttenuationWorkPortn.setStatus("current")
_PmdgeCtrlWaveItuWorkPortn_Type = DisplayString
_PmdgeCtrlWaveItuWorkPortn_Object = MibTableColumn
pmdgeCtrlWaveItuWorkPortn = _PmdgeCtrlWaveItuWorkPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 6, 1, 66, 1, 7),
    _PmdgeCtrlWaveItuWorkPortn_Type()
)
pmdgeCtrlWaveItuWorkPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdgeCtrlWaveItuWorkPortn.setStatus("current")
_PmdgeCtrlWaveDegreeWorkPortn_Type = Integer32
_PmdgeCtrlWaveDegreeWorkPortn_Object = MibTableColumn
pmdgeCtrlWaveDegreeWorkPortn = _PmdgeCtrlWaveDegreeWorkPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 6, 1, 66, 1, 8),
    _PmdgeCtrlWaveDegreeWorkPortn_Type()
)
pmdgeCtrlWaveDegreeWorkPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmdgeCtrlWaveDegreeWorkPortn.setStatus("current")
_PmdgeCtrlUsageWorkPortn_Type = EkiOnOff
_PmdgeCtrlUsageWorkPortn_Object = MibTableColumn
pmdgeCtrlUsageWorkPortn = _PmdgeCtrlUsageWorkPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 6, 1, 66, 1, 16),
    _PmdgeCtrlUsageWorkPortn_Type()
)
pmdgeCtrlUsageWorkPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdgeCtrlUsageWorkPortn.setStatus("current")
_PmdgeCtrlbuildFromMgntPlan_Type = DisplayString
_PmdgeCtrlbuildFromMgntPlan_Object = MibScalar
pmdgeCtrlbuildFromMgntPlan = _PmdgeCtrlbuildFromMgntPlan_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 6, 1, 67),
    _PmdgeCtrlbuildFromMgntPlan_Type()
)
pmdgeCtrlbuildFromMgntPlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmdgeCtrlbuildFromMgntPlan.setStatus("current")
_PmdgeCtrlloadToWorkplan_Type = PmdgePlanNumber
_PmdgeCtrlloadToWorkplan_Object = MibScalar
pmdgeCtrlloadToWorkplan = _PmdgeCtrlloadToWorkplan_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 6, 1, 68),
    _PmdgeCtrlloadToWorkplan_Type()
)
pmdgeCtrlloadToWorkplan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmdgeCtrlloadToWorkplan.setStatus("current")
_PmdgeCtrlsaveWorkPlanTo_Type = PmdgePlanNumber
_PmdgeCtrlsaveWorkPlanTo_Object = MibScalar
pmdgeCtrlsaveWorkPlanTo = _PmdgeCtrlsaveWorkPlanTo_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 6, 1, 69),
    _PmdgeCtrlsaveWorkPlanTo_Type()
)
pmdgeCtrlsaveWorkPlanTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmdgeCtrlsaveWorkPlanTo.setStatus("current")
_PmdgeCtrlloadPlanToUse_Type = PmdgePlanNumber
_PmdgeCtrlloadPlanToUse_Object = MibScalar
pmdgeCtrlloadPlanToUse = _PmdgeCtrlloadPlanToUse_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 6, 1, 70),
    _PmdgeCtrlloadPlanToUse_Type()
)
pmdgeCtrlloadPlanToUse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmdgeCtrlloadPlanToUse.setStatus("current")
_PmdgeCtrlrefreshWithPlan_Type = PmdgePlanNumber
_PmdgeCtrlrefreshWithPlan_Object = MibScalar
pmdgeCtrlrefreshWithPlan = _PmdgeCtrlrefreshWithPlan_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 6, 1, 71),
    _PmdgeCtrlrefreshWithPlan_Type()
)
pmdgeCtrlrefreshWithPlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmdgeCtrlrefreshWithPlan.setStatus("current")
_PmdgeCtrlsavePlanToFile_Type = PmdgePlanNumber
_PmdgeCtrlsavePlanToFile_Object = MibScalar
pmdgeCtrlsavePlanToFile = _PmdgeCtrlsavePlanToFile_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 6, 1, 72),
    _PmdgeCtrlsavePlanToFile_Type()
)
pmdgeCtrlsavePlanToFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmdgeCtrlsavePlanToFile.setStatus("current")
_PmdgeCtrlloadPlanFromFile_Type = PmdgePlanNumber
_PmdgeCtrlloadPlanFromFile_Object = MibScalar
pmdgeCtrlloadPlanFromFile = _PmdgeCtrlloadPlanFromFile_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 6, 1, 73),
    _PmdgeCtrlloadPlanFromFile_Type()
)
pmdgeCtrlloadPlanFromFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmdgeCtrlloadPlanFromFile.setStatus("current")
_PmdgeCtrlEqualizer_ObjectIdentity = ObjectIdentity
pmdgeCtrlEqualizer = _PmdgeCtrlEqualizer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 56, 6, 2)
)
_PmdgeCtrlequTxCommonAttDegTable_Object = MibTable
pmdgeCtrlequTxCommonAttDegTable = _PmdgeCtrlequTxCommonAttDegTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 6, 2, 19)
)
if mibBuilder.loadTexts:
    pmdgeCtrlequTxCommonAttDegTable.setStatus("current")
_PmdgeCtrlequTxCommonAttDegEntry_Object = MibTableRow
pmdgeCtrlequTxCommonAttDegEntry = _PmdgeCtrlequTxCommonAttDegEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 6, 2, 19, 1)
)
pmdgeCtrlequTxCommonAttDegEntry.setIndexNames(
    (0, "EKINOPS-PmDGE-MIB", "pmdgeCtrlequTxCommonAttDegIndex"),
)
if mibBuilder.loadTexts:
    pmdgeCtrlequTxCommonAttDegEntry.setStatus("current")


class _PmdgeCtrlequTxCommonAttDegIndex_Type(Integer32):
    """Custom type pmdgeCtrlequTxCommonAttDegIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_PmdgeCtrlequTxCommonAttDegIndex_Type.__name__ = "Integer32"
_PmdgeCtrlequTxCommonAttDegIndex_Object = MibTableColumn
pmdgeCtrlequTxCommonAttDegIndex = _PmdgeCtrlequTxCommonAttDegIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 6, 2, 19, 1, 1),
    _PmdgeCtrlequTxCommonAttDegIndex_Type()
)
pmdgeCtrlequTxCommonAttDegIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdgeCtrlequTxCommonAttDegIndex.setStatus("current")


class _PmdgeCtrlequTxCommonAttDegPortn_Type(Integer32):
    """Custom type pmdgeCtrlequTxCommonAttDegPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmdgeCtrlequTxCommonAttDegPortn_Type.__name__ = "Integer32"
_PmdgeCtrlequTxCommonAttDegPortn_Object = MibTableColumn
pmdgeCtrlequTxCommonAttDegPortn = _PmdgeCtrlequTxCommonAttDegPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 6, 2, 19, 1, 2),
    _PmdgeCtrlequTxCommonAttDegPortn_Type()
)
pmdgeCtrlequTxCommonAttDegPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmdgeCtrlequTxCommonAttDegPortn.setStatus("current")
_PmdgeCtrlapplyPlanUpdate_ObjectIdentity = ObjectIdentity
pmdgeCtrlapplyPlanUpdate = _PmdgeCtrlapplyPlanUpdate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 56, 6, 2, 44)
)
_PmdgeCtrlApply_Type = EkiOnOff
_PmdgeCtrlApply_Object = MibScalar
pmdgeCtrlApply = _PmdgeCtrlApply_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 6, 2, 44, 1),
    _PmdgeCtrlApply_Type()
)
pmdgeCtrlApply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmdgeCtrlApply.setStatus("current")
_PmdgeCtrlLine_ObjectIdentity = ObjectIdentity
pmdgeCtrlLine = _PmdgeCtrlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 56, 6, 3)
)
_Pmdgeri_ObjectIdentity = ObjectIdentity
pmdgeri = _Pmdgeri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 56, 7)
)
_PmdgeriTable_ObjectIdentity = ObjectIdentity
pmdgeriTable = _PmdgeriTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 56, 7, 1)
)
_PmdgeRinvPortTable_Object = MibTable
pmdgeRinvPortTable = _PmdgeRinvPortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 7, 1, 1)
)
if mibBuilder.loadTexts:
    pmdgeRinvPortTable.setStatus("current")
_PmdgeRinvPortEntry_Object = MibTableRow
pmdgeRinvPortEntry = _PmdgeRinvPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 7, 1, 1, 1)
)
pmdgeRinvPortEntry.setIndexNames(
    (0, "EKINOPS-PmDGE-MIB", "pmdgeRinvPortIndex"),
)
if mibBuilder.loadTexts:
    pmdgeRinvPortEntry.setStatus("current")


class _PmdgeRinvPortIndex_Type(Integer32):
    """Custom type pmdgeRinvPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_PmdgeRinvPortIndex_Type.__name__ = "Integer32"
_PmdgeRinvPortIndex_Object = MibTableColumn
pmdgeRinvPortIndex = _PmdgeRinvPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 7, 1, 1, 1, 1),
    _PmdgeRinvPortIndex_Type()
)
pmdgeRinvPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdgeRinvPortIndex.setStatus("current")
_PmdgeRinvPort_Type = DisplayString
_PmdgeRinvPort_Object = MibTableColumn
pmdgeRinvPort = _PmdgeRinvPort_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 7, 1, 1, 1, 2),
    _PmdgeRinvPort_Type()
)
pmdgeRinvPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdgeRinvPort.setStatus("current")
_PmdgeRinvLineTable_Object = MibTable
pmdgeRinvLineTable = _PmdgeRinvLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 7, 1, 2)
)
if mibBuilder.loadTexts:
    pmdgeRinvLineTable.setStatus("current")
_PmdgeRinvLineEntry_Object = MibTableRow
pmdgeRinvLineEntry = _PmdgeRinvLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 7, 1, 2, 1)
)
pmdgeRinvLineEntry.setIndexNames(
    (0, "EKINOPS-PmDGE-MIB", "pmdgeRinvLineIndex"),
)
if mibBuilder.loadTexts:
    pmdgeRinvLineEntry.setStatus("current")


class _PmdgeRinvLineIndex_Type(Integer32):
    """Custom type pmdgeRinvLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_PmdgeRinvLineIndex_Type.__name__ = "Integer32"
_PmdgeRinvLineIndex_Object = MibTableColumn
pmdgeRinvLineIndex = _PmdgeRinvLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 7, 1, 2, 1, 1),
    _PmdgeRinvLineIndex_Type()
)
pmdgeRinvLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdgeRinvLineIndex.setStatus("current")
_PmdgeRinvxfpLine_Type = DisplayString
_PmdgeRinvxfpLine_Object = MibTableColumn
pmdgeRinvxfpLine = _PmdgeRinvxfpLine_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 7, 1, 2, 1, 2),
    _PmdgeRinvxfpLine_Type()
)
pmdgeRinvxfpLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdgeRinvxfpLine.setStatus("current")
_PmdgeRinvReloadInventory_Type = EkiOnOff
_PmdgeRinvReloadInventory_Object = MibScalar
pmdgeRinvReloadInventory = _PmdgeRinvReloadInventory_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 7, 2),
    _PmdgeRinvReloadInventory_Type()
)
pmdgeRinvReloadInventory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmdgeRinvReloadInventory.setStatus("current")
_PmdgeRinvHwPlatform_Type = DisplayString
_PmdgeRinvHwPlatform_Object = MibScalar
pmdgeRinvHwPlatform = _PmdgeRinvHwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 7, 4),
    _PmdgeRinvHwPlatform_Type()
)
pmdgeRinvHwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdgeRinvHwPlatform.setStatus("current")
_PmdgeRinvSwPlatform_Type = DisplayString
_PmdgeRinvSwPlatform_Object = MibScalar
pmdgeRinvSwPlatform = _PmdgeRinvSwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 7, 5),
    _PmdgeRinvSwPlatform_Type()
)
pmdgeRinvSwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdgeRinvSwPlatform.setStatus("current")
_PmdgeConfig_ObjectIdentity = ObjectIdentity
pmdgeConfig = _PmdgeConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 56, 9)
)
_PmdgeCfgLsd_ObjectIdentity = ObjectIdentity
pmdgeCfgLsd = _PmdgeCfgLsd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 56, 9, 1)
)
_PmdgetableclientLsd_ObjectIdentity = ObjectIdentity
pmdgetableclientLsd = _PmdgetableclientLsd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 56, 9, 1, 1)
)
_PmdgeCfgStartup_ObjectIdentity = ObjectIdentity
pmdgeCfgStartup = _PmdgeCfgStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 56, 9, 2)
)
_PmdgeCfgClientStartupTable_Object = MibTable
pmdgeCfgClientStartupTable = _PmdgeCfgClientStartupTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 9, 2, 1)
)
if mibBuilder.loadTexts:
    pmdgeCfgClientStartupTable.setStatus("current")
_PmdgeCfgClientStartupEntry_Object = MibTableRow
pmdgeCfgClientStartupEntry = _PmdgeCfgClientStartupEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 9, 2, 1, 1)
)
pmdgeCfgClientStartupEntry.setIndexNames(
    (0, "EKINOPS-PmDGE-MIB", "pmdgeCfgClientStartupIndex"),
)
if mibBuilder.loadTexts:
    pmdgeCfgClientStartupEntry.setStatus("current")


class _PmdgeCfgClientStartupIndex_Type(Integer32):
    """Custom type pmdgeCfgClientStartupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_PmdgeCfgClientStartupIndex_Type.__name__ = "Integer32"
_PmdgeCfgClientStartupIndex_Object = MibTableColumn
pmdgeCfgClientStartupIndex = _PmdgeCfgClientStartupIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 9, 2, 1, 1, 1),
    _PmdgeCfgClientStartupIndex_Type()
)
pmdgeCfgClientStartupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdgeCfgClientStartupIndex.setStatus("current")


class _PmdgeCfgLineaRxCommonAttDegPortn_Type(Unsigned32):
    """Custom type pmdgeCfgLineaRxCommonAttDegPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmdgeCfgLineaRxCommonAttDegPortn_Type.__name__ = "Unsigned32"
_PmdgeCfgLineaRxCommonAttDegPortn_Object = MibTableColumn
pmdgeCfgLineaRxCommonAttDegPortn = _PmdgeCfgLineaRxCommonAttDegPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 9, 2, 1, 1, 3),
    _PmdgeCfgLineaRxCommonAttDegPortn_Type()
)
pmdgeCfgLineaRxCommonAttDegPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmdgeCfgLineaRxCommonAttDegPortn.setStatus("current")
_PmdgetablelineStartup_ObjectIdentity = ObjectIdentity
pmdgetablelineStartup = _PmdgetablelineStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 56, 9, 2, 2)
)
_PmdgetableclientsDge_ObjectIdentity = ObjectIdentity
pmdgetableclientsDge = _PmdgetableclientsDge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 56, 9, 2, 3)
)
_PmdgetablelinesDge_ObjectIdentity = ObjectIdentity
pmdgetablelinesDge = _PmdgetablelinesDge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 56, 9, 2, 4)
)


class _PmdgeCfgequGridCurrent_Type(Unsigned32):
    """Custom type pmdgeCfgequGridCurrent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmdgeCfgequGridCurrent_Type.__name__ = "Unsigned32"
_PmdgeCfgequGridCurrent_Object = MibScalar
pmdgeCfgequGridCurrent = _PmdgeCfgequGridCurrent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 9, 2, 4, 2),
    _PmdgeCfgequGridCurrent_Type()
)
pmdgeCfgequGridCurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmdgeCfgequGridCurrent.setStatus("current")
_Pmdgetableother_ObjectIdentity = ObjectIdentity
pmdgetableother = _Pmdgetableother_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 56, 9, 2, 5)
)


class _PmdgeCfgcomponentType_Type(Unsigned32):
    """Custom type pmdgeCfgcomponentType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmdgeCfgcomponentType_Type.__name__ = "Unsigned32"
_PmdgeCfgcomponentType_Object = MibScalar
pmdgeCfgcomponentType = _PmdgeCfgcomponentType_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 9, 2, 5, 2),
    _PmdgeCfgcomponentType_Type()
)
pmdgeCfgcomponentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdgeCfgcomponentType.setStatus("current")


class _PmdgeCfgmiscellaneous_Type(Unsigned32):
    """Custom type pmdgeCfgmiscellaneous based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmdgeCfgmiscellaneous_Type.__name__ = "Unsigned32"
_PmdgeCfgmiscellaneous_Object = MibScalar
pmdgeCfgmiscellaneous = _PmdgeCfgmiscellaneous_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 9, 2, 5, 3),
    _PmdgeCfgmiscellaneous_Type()
)
pmdgeCfgmiscellaneous.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdgeCfgmiscellaneous.setStatus("current")


class _PmdgeCfgfirstChannel_Type(Unsigned32):
    """Custom type pmdgeCfgfirstChannel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmdgeCfgfirstChannel_Type.__name__ = "Unsigned32"
_PmdgeCfgfirstChannel_Object = MibScalar
pmdgeCfgfirstChannel = _PmdgeCfgfirstChannel_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 9, 2, 5, 4),
    _PmdgeCfgfirstChannel_Type()
)
pmdgeCfgfirstChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdgeCfgfirstChannel.setStatus("current")


class _PmdgeCfglastChannel_Type(Unsigned32):
    """Custom type pmdgeCfglastChannel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmdgeCfglastChannel_Type.__name__ = "Unsigned32"
_PmdgeCfglastChannel_Object = MibScalar
pmdgeCfglastChannel = _PmdgeCfglastChannel_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 9, 2, 5, 5),
    _PmdgeCfglastChannel_Type()
)
pmdgeCfglastChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdgeCfglastChannel.setStatus("current")


class _PmdgeCfggrid_Type(Unsigned32):
    """Custom type pmdgeCfggrid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmdgeCfggrid_Type.__name__ = "Unsigned32"
_PmdgeCfggrid_Object = MibScalar
pmdgeCfggrid = _PmdgeCfggrid_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 9, 2, 5, 6),
    _PmdgeCfggrid_Type()
)
pmdgeCfggrid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdgeCfggrid.setStatus("current")
_PmdgeCfgLabels_ObjectIdentity = ObjectIdentity
pmdgeCfgLabels = _PmdgeCfgLabels_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 56, 9, 3)
)
_PmdgeCfgLabelclientTable_Object = MibTable
pmdgeCfgLabelclientTable = _PmdgeCfgLabelclientTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 9, 3, 1)
)
if mibBuilder.loadTexts:
    pmdgeCfgLabelclientTable.setStatus("current")
_PmdgeCfgLabelclientEntry_Object = MibTableRow
pmdgeCfgLabelclientEntry = _PmdgeCfgLabelclientEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 9, 3, 1, 1)
)
pmdgeCfgLabelclientEntry.setIndexNames(
    (0, "EKINOPS-PmDGE-MIB", "pmdgeCfgLabelclientIndex"),
)
if mibBuilder.loadTexts:
    pmdgeCfgLabelclientEntry.setStatus("current")


class _PmdgeCfgLabelclientIndex_Type(Integer32):
    """Custom type pmdgeCfgLabelclientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_PmdgeCfgLabelclientIndex_Type.__name__ = "Integer32"
_PmdgeCfgLabelclientIndex_Object = MibTableColumn
pmdgeCfgLabelclientIndex = _PmdgeCfgLabelclientIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 9, 3, 1, 1, 1),
    _PmdgeCfgLabelclientIndex_Type()
)
pmdgeCfgLabelclientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdgeCfgLabelclientIndex.setStatus("current")


class _PmdgeCfgLabelclientPortn_Type(DisplayString):
    """Custom type pmdgeCfgLabelclientPortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_PmdgeCfgLabelclientPortn_Type.__name__ = "DisplayString"
_PmdgeCfgLabelclientPortn_Object = MibTableColumn
pmdgeCfgLabelclientPortn = _PmdgeCfgLabelclientPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 9, 3, 1, 1, 3),
    _PmdgeCfgLabelclientPortn_Type()
)
pmdgeCfgLabelclientPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmdgeCfgLabelclientPortn.setStatus("current")
_PmdgeCfgLabellineTable_Object = MibTable
pmdgeCfgLabellineTable = _PmdgeCfgLabellineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 9, 3, 2)
)
if mibBuilder.loadTexts:
    pmdgeCfgLabellineTable.setStatus("current")
_PmdgeCfgLabellineEntry_Object = MibTableRow
pmdgeCfgLabellineEntry = _PmdgeCfgLabellineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 9, 3, 2, 1)
)
pmdgeCfgLabellineEntry.setIndexNames(
    (0, "EKINOPS-PmDGE-MIB", "pmdgeCfgLabellineIndex"),
)
if mibBuilder.loadTexts:
    pmdgeCfgLabellineEntry.setStatus("current")


class _PmdgeCfgLabellineIndex_Type(Integer32):
    """Custom type pmdgeCfgLabellineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_PmdgeCfgLabellineIndex_Type.__name__ = "Integer32"
_PmdgeCfgLabellineIndex_Object = MibTableColumn
pmdgeCfgLabellineIndex = _PmdgeCfgLabellineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 9, 3, 2, 1, 1),
    _PmdgeCfgLabellineIndex_Type()
)
pmdgeCfgLabellineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdgeCfgLabellineIndex.setStatus("current")


class _PmdgeCfgLabellinePortn_Type(DisplayString):
    """Custom type pmdgeCfgLabellinePortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_PmdgeCfgLabellinePortn_Type.__name__ = "DisplayString"
_PmdgeCfgLabellinePortn_Object = MibTableColumn
pmdgeCfgLabellinePortn = _PmdgeCfgLabellinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 9, 3, 2, 1, 3),
    _PmdgeCfgLabellinePortn_Type()
)
pmdgeCfgLabellinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmdgeCfgLabellinePortn.setStatus("current")
_PmdgeCfgWriteConfiguration_Type = EkiOnOff
_PmdgeCfgWriteConfiguration_Object = MibScalar
pmdgeCfgWriteConfiguration = _PmdgeCfgWriteConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 9, 257),
    _PmdgeCfgWriteConfiguration_Type()
)
pmdgeCfgWriteConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmdgeCfgWriteConfiguration.setStatus("current")
_Pmdgetraps_ObjectIdentity = ObjectIdentity
pmdgetraps = _Pmdgetraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 56, 10)
)


class _PmdgetrapBoardNumber_Type(Integer32):
    """Custom type pmdgetrapBoardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_PmdgetrapBoardNumber_Type.__name__ = "Integer32"
_PmdgetrapBoardNumber_Object = MibScalar
pmdgetrapBoardNumber = _PmdgetrapBoardNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 56, 10, 4),
    _PmdgetrapBoardNumber_Type()
)
pmdgetrapBoardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmdgetrapBoardNumber.setStatus("current")

# Managed Objects groups


# Notification objects

pmdgePowerTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 56, 10, 50)
)
pmdgePowerTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-PmDGE-MIB", "pmdgeAlmDefFuseB"),
        ("EKINOPS-PmDGE-MIB", "pmdgeAlmDefFuseA"),
        ("EKINOPS-PmDGE-MIB", "pmdgetrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmdgePowerTrapUrgentGoesOn.setStatus(
        "current"
    )

pmdgePowerTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 56, 10, 51)
)
pmdgePowerTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-PmDGE-MIB", "pmdgeAlmDefFuseB"),
        ("EKINOPS-PmDGE-MIB", "pmdgeAlmDefFuseA"),
        ("EKINOPS-PmDGE-MIB", "pmdgetrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmdgePowerTrapUrgentGoesOff.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EKINOPS-PmDGE-MIB",
    **{"PmdgeGrid": PmdgeGrid,
       "PmdgePlanNumber": PmdgePlanNumber,
       "PmdgeChannel": PmdgeChannel,
       "modulepmdge": modulepmdge,
       "pmdgealarms": pmdgealarms,
       "pmdgeAlmOther": pmdgeAlmOther,
       "pmdgeAlmOtherNurg": pmdgeAlmOtherNurg,
       "pmdgeAlmswitchDegrade": pmdgeAlmswitchDegrade,
       "pmdgeAlmSwitchTempHighDeg": pmdgeAlmSwitchTempHighDeg,
       "pmdgeAlmOtherUrg": pmdgeAlmOtherUrg,
       "pmdgeAlmswitchAlarms": pmdgeAlmswitchAlarms,
       "pmdgeAlmSwitchTempHighAla": pmdgeAlmSwitchTempHighAla,
       "pmdgeAlmmoduleStatus": pmdgeAlmmoduleStatus,
       "pmdgeAlmColdReset": pmdgeAlmColdReset,
       "pmdgeAlmWarmReset": pmdgeAlmWarmReset,
       "pmdgeAlmHotReset": pmdgeAlmHotReset,
       "pmdgeAlmSwitchNotReady": pmdgeAlmSwitchNotReady,
       "pmdgeAlmmoduleAlarms": pmdgeAlmmoduleAlarms,
       "pmdgeAlmModuleTempHighAla": pmdgeAlmModuleTempHighAla,
       "pmdgeAlmCaseTempHighAla": pmdgeAlmCaseTempHighAla,
       "pmdgeAlmmoduleDegrad": pmdgeAlmmoduleDegrad,
       "pmdgeAlmModuleTempHighDeg": pmdgeAlmModuleTempHighDeg,
       "pmdgeAlmCaseTempHighDeg": pmdgeAlmCaseTempHighDeg,
       "pmdgeAlmOtherCrit": pmdgeAlmOtherCrit,
       "pmdgeAlmsynthAlm0": pmdgeAlmsynthAlm0,
       "pmdgeAlmInServiceNotReady": pmdgeAlmInServiceNotReady,
       "pmdgeAlmModuleGlobFailure": pmdgeAlmModuleGlobFailure,
       "pmdgeAlmDefFuseA": pmdgeAlmDefFuseA,
       "pmdgeAlmDefFuseB": pmdgeAlmDefFuseB,
       "pmdgeAlmsynthAlm7": pmdgeAlmsynthAlm7,
       "pmdgeAlmInitNotCompl": pmdgeAlmInitNotCompl,
       "pmdgeAlmSwitchDegrade": pmdgeAlmSwitchDegrade,
       "pmdgeAlmSwitchAlm": pmdgeAlmSwitchAlm,
       "pmdgemeasures": pmdgemeasures,
       "pmdgeMesrOther": pmdgeMesrOther,
       "pmdgeMesrswitchTemp": pmdgeMesrswitchTemp,
       "pmdgeMesrmoduleTemp": pmdgeMesrmoduleTemp,
       "pmdgeMesrcaseTemp": pmdgeMesrcaseTemp,
       "pmdgecontrolsWrite": pmdgecontrolsWrite,
       "pmdgeCtrlOther": pmdgeCtrlOther,
       "pmdgeCtrlsynth0": pmdgeCtrlsynth0,
       "pmdgeCtrlConfLoad": pmdgeCtrlConfLoad,
       "pmdgeCtrlConfFlash": pmdgeCtrlConfFlash,
       "pmdgeCtrlConfClear": pmdgeCtrlConfClear,
       "pmdgeCtrlsynth4": pmdgeCtrlsynth4,
       "pmdgeCtrlCorrelatOn": pmdgeCtrlCorrelatOn,
       "pmdgeCtrlCorrelatOff": pmdgeCtrlCorrelatOff,
       "pmdgeCtrlswMgnt": pmdgeCtrlswMgnt,
       "pmdgeCtrlColdReset": pmdgeCtrlColdReset,
       "pmdgeCtrlWarmReset": pmdgeCtrlWarmReset,
       "pmdgeCtrlswitchCtrl": pmdgeCtrlswitchCtrl,
       "pmdgeCtrlAllChannelsHighLoss": pmdgeCtrlAllChannelsHighLoss,
       "pmdgeCtrlcraftSynch": pmdgeCtrlcraftSynch,
       "pmdgeCtrlledTest": pmdgeCtrlledTest,
       "pmdgeCtrlGreenLed": pmdgeCtrlGreenLed,
       "pmdgeCtrlRedLed": pmdgeCtrlRedLed,
       "pmdgeCtrlLedOff": pmdgeCtrlLedOff,
       "pmdgeCtrlwavePlanAssignmentsRefreshTable": pmdgeCtrlwavePlanAssignmentsRefreshTable,
       "pmdgeCtrlwavePlanAssignmentsRefreshEntry": pmdgeCtrlwavePlanAssignmentsRefreshEntry,
       "pmdgeCtrlwavePlanAssignmentsRefreshIndex": pmdgeCtrlwavePlanAssignmentsRefreshIndex,
       "pmdgeCtrlWaveStatusRefreshPortn": pmdgeCtrlWaveStatusRefreshPortn,
       "pmdgeCtrlWaveNarrowingRefreshPortn": pmdgeCtrlWaveNarrowingRefreshPortn,
       "pmdgeCtrlWaveCenterFrequencyRefreshPortn": pmdgeCtrlWaveCenterFrequencyRefreshPortn,
       "pmdgeCtrlWaveOOSRefreshPortn": pmdgeCtrlWaveOOSRefreshPortn,
       "pmdgeCtrlWaveAttenuationRefreshPortn": pmdgeCtrlWaveAttenuationRefreshPortn,
       "pmdgeCtrlWaveItuRefreshPortn": pmdgeCtrlWaveItuRefreshPortn,
       "pmdgeCtrlWaveDegreeRefreshPortn": pmdgeCtrlWaveDegreeRefreshPortn,
       "pmdgeCtrlUsageRefreshPortn": pmdgeCtrlUsageRefreshPortn,
       "pmdgeCtrlwavePlanAssignmentsWorkTable": pmdgeCtrlwavePlanAssignmentsWorkTable,
       "pmdgeCtrlwavePlanAssignmentsWorkEntry": pmdgeCtrlwavePlanAssignmentsWorkEntry,
       "pmdgeCtrlwavePlanAssignmentsWorkIndex": pmdgeCtrlwavePlanAssignmentsWorkIndex,
       "pmdgeCtrlWaveStatusWorkPortn": pmdgeCtrlWaveStatusWorkPortn,
       "pmdgeCtrlWaveNarrowingWorkPortn": pmdgeCtrlWaveNarrowingWorkPortn,
       "pmdgeCtrlWaveCenterFrequencyWorkPortn": pmdgeCtrlWaveCenterFrequencyWorkPortn,
       "pmdgeCtrlWaveOOSWorkPortn": pmdgeCtrlWaveOOSWorkPortn,
       "pmdgeCtrlWaveAttenuationWorkPortn": pmdgeCtrlWaveAttenuationWorkPortn,
       "pmdgeCtrlWaveItuWorkPortn": pmdgeCtrlWaveItuWorkPortn,
       "pmdgeCtrlWaveDegreeWorkPortn": pmdgeCtrlWaveDegreeWorkPortn,
       "pmdgeCtrlUsageWorkPortn": pmdgeCtrlUsageWorkPortn,
       "pmdgeCtrlbuildFromMgntPlan": pmdgeCtrlbuildFromMgntPlan,
       "pmdgeCtrlloadToWorkplan": pmdgeCtrlloadToWorkplan,
       "pmdgeCtrlsaveWorkPlanTo": pmdgeCtrlsaveWorkPlanTo,
       "pmdgeCtrlloadPlanToUse": pmdgeCtrlloadPlanToUse,
       "pmdgeCtrlrefreshWithPlan": pmdgeCtrlrefreshWithPlan,
       "pmdgeCtrlsavePlanToFile": pmdgeCtrlsavePlanToFile,
       "pmdgeCtrlloadPlanFromFile": pmdgeCtrlloadPlanFromFile,
       "pmdgeCtrlEqualizer": pmdgeCtrlEqualizer,
       "pmdgeCtrlequTxCommonAttDegTable": pmdgeCtrlequTxCommonAttDegTable,
       "pmdgeCtrlequTxCommonAttDegEntry": pmdgeCtrlequTxCommonAttDegEntry,
       "pmdgeCtrlequTxCommonAttDegIndex": pmdgeCtrlequTxCommonAttDegIndex,
       "pmdgeCtrlequTxCommonAttDegPortn": pmdgeCtrlequTxCommonAttDegPortn,
       "pmdgeCtrlapplyPlanUpdate": pmdgeCtrlapplyPlanUpdate,
       "pmdgeCtrlApply": pmdgeCtrlApply,
       "pmdgeCtrlLine": pmdgeCtrlLine,
       "pmdgeri": pmdgeri,
       "pmdgeriTable": pmdgeriTable,
       "pmdgeRinvPortTable": pmdgeRinvPortTable,
       "pmdgeRinvPortEntry": pmdgeRinvPortEntry,
       "pmdgeRinvPortIndex": pmdgeRinvPortIndex,
       "pmdgeRinvPort": pmdgeRinvPort,
       "pmdgeRinvLineTable": pmdgeRinvLineTable,
       "pmdgeRinvLineEntry": pmdgeRinvLineEntry,
       "pmdgeRinvLineIndex": pmdgeRinvLineIndex,
       "pmdgeRinvxfpLine": pmdgeRinvxfpLine,
       "pmdgeRinvReloadInventory": pmdgeRinvReloadInventory,
       "pmdgeRinvHwPlatform": pmdgeRinvHwPlatform,
       "pmdgeRinvSwPlatform": pmdgeRinvSwPlatform,
       "pmdgeConfig": pmdgeConfig,
       "pmdgeCfgLsd": pmdgeCfgLsd,
       "pmdgetableclientLsd": pmdgetableclientLsd,
       "pmdgeCfgStartup": pmdgeCfgStartup,
       "pmdgeCfgClientStartupTable": pmdgeCfgClientStartupTable,
       "pmdgeCfgClientStartupEntry": pmdgeCfgClientStartupEntry,
       "pmdgeCfgClientStartupIndex": pmdgeCfgClientStartupIndex,
       "pmdgeCfgLineaRxCommonAttDegPortn": pmdgeCfgLineaRxCommonAttDegPortn,
       "pmdgetablelineStartup": pmdgetablelineStartup,
       "pmdgetableclientsDge": pmdgetableclientsDge,
       "pmdgetablelinesDge": pmdgetablelinesDge,
       "pmdgeCfgequGridCurrent": pmdgeCfgequGridCurrent,
       "pmdgetableother": pmdgetableother,
       "pmdgeCfgcomponentType": pmdgeCfgcomponentType,
       "pmdgeCfgmiscellaneous": pmdgeCfgmiscellaneous,
       "pmdgeCfgfirstChannel": pmdgeCfgfirstChannel,
       "pmdgeCfglastChannel": pmdgeCfglastChannel,
       "pmdgeCfggrid": pmdgeCfggrid,
       "pmdgeCfgLabels": pmdgeCfgLabels,
       "pmdgeCfgLabelclientTable": pmdgeCfgLabelclientTable,
       "pmdgeCfgLabelclientEntry": pmdgeCfgLabelclientEntry,
       "pmdgeCfgLabelclientIndex": pmdgeCfgLabelclientIndex,
       "pmdgeCfgLabelclientPortn": pmdgeCfgLabelclientPortn,
       "pmdgeCfgLabellineTable": pmdgeCfgLabellineTable,
       "pmdgeCfgLabellineEntry": pmdgeCfgLabellineEntry,
       "pmdgeCfgLabellineIndex": pmdgeCfgLabellineIndex,
       "pmdgeCfgLabellinePortn": pmdgeCfgLabellinePortn,
       "pmdgeCfgWriteConfiguration": pmdgeCfgWriteConfiguration,
       "pmdgetraps": pmdgetraps,
       "pmdgetrapBoardNumber": pmdgetrapBoardNumber,
       "pmdgePowerTrapUrgentGoesOn": pmdgePowerTrapUrgentGoesOn,
       "pmdgePowerTrapUrgentGoesOff": pmdgePowerTrapUrgentGoesOff}
)
