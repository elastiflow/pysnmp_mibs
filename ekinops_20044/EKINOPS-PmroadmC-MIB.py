# SNMP MIB module (EKINOPS-PmroadmC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ekinops_20044/EKINOPS-PmroadmC-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 12:01:49 2025
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

modulepmroadmC = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 35)
)
if mibBuilder.loadTexts:
    modulepmroadmC.setRevisions(
        ("2008-08-21 00:00",
         "2009-02-05 00:00",
         "2009-09-29 00:00",
         "2010-02-05 00:00",
         "2010-02-24 00:00",
         "2010-11-04 00:00",
         "2010-12-15 00:00",
         "2012-07-04 00:00",
         "2012-07-05 00:00",
         "2012-07-09 00:00",
         "2014-03-26 00:00",
         "2014-12-16 00:00",
         "2016-05-23 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PmroadmCGrid(TextualConvention, Integer32):
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
        *(("roadmCgrid50", 50),
          ("roadmCgrid100", 100),
          ("roadmCgrid200", 200))
    )



class PmroadmCPlanNumber(TextualConvention, Integer32):
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



class PmroadmCChannel(TextualConvention, Integer32):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_PmroadmCalarms_ObjectIdentity = ObjectIdentity
pmroadmCalarms = _PmroadmCalarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 35, 2)
)
_PmroadmCAlmOther_ObjectIdentity = ObjectIdentity
pmroadmCAlmOther = _PmroadmCAlmOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 35, 2, 1)
)
_PmroadmCAlmOtherNurg_ObjectIdentity = ObjectIdentity
pmroadmCAlmOtherNurg = _PmroadmCAlmOtherNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 35, 2, 1, 1)
)
_PmroadmCAlmswitchDegrade_ObjectIdentity = ObjectIdentity
pmroadmCAlmswitchDegrade = _PmroadmCAlmswitchDegrade_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 35, 2, 1, 1, 17)
)
_PmroadmCAlmSwitchTempHighDeg_Type = EkiOnOff
_PmroadmCAlmSwitchTempHighDeg_Object = MibScalar
pmroadmCAlmSwitchTempHighDeg = _PmroadmCAlmSwitchTempHighDeg_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 2, 1, 1, 17, 2),
    _PmroadmCAlmSwitchTempHighDeg_Type()
)
pmroadmCAlmSwitchTempHighDeg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmroadmCAlmSwitchTempHighDeg.setStatus("current")
_PmroadmCAlmOtherUrg_ObjectIdentity = ObjectIdentity
pmroadmCAlmOtherUrg = _PmroadmCAlmOtherUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 35, 2, 1, 2)
)
_PmroadmCAlmswitchAlarms_ObjectIdentity = ObjectIdentity
pmroadmCAlmswitchAlarms = _PmroadmCAlmswitchAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 35, 2, 1, 2, 16)
)
_PmroadmCAlmSwitchTempHighAla_Type = EkiOnOff
_PmroadmCAlmSwitchTempHighAla_Object = MibScalar
pmroadmCAlmSwitchTempHighAla = _PmroadmCAlmSwitchTempHighAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 2, 1, 2, 16, 2),
    _PmroadmCAlmSwitchTempHighAla_Type()
)
pmroadmCAlmSwitchTempHighAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmroadmCAlmSwitchTempHighAla.setStatus("current")
_PmroadmCAlmmoduleStatus_ObjectIdentity = ObjectIdentity
pmroadmCAlmmoduleStatus = _PmroadmCAlmmoduleStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 35, 2, 1, 2, 66)
)
_PmroadmCAlmColdReset_Type = EkiOnOff
_PmroadmCAlmColdReset_Object = MibScalar
pmroadmCAlmColdReset = _PmroadmCAlmColdReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 2, 1, 2, 66, 1),
    _PmroadmCAlmColdReset_Type()
)
pmroadmCAlmColdReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmroadmCAlmColdReset.setStatus("current")
_PmroadmCAlmWarmReset_Type = EkiOnOff
_PmroadmCAlmWarmReset_Object = MibScalar
pmroadmCAlmWarmReset = _PmroadmCAlmWarmReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 2, 1, 2, 66, 2),
    _PmroadmCAlmWarmReset_Type()
)
pmroadmCAlmWarmReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmroadmCAlmWarmReset.setStatus("current")
_PmroadmCAlmHotReset_Type = EkiOnOff
_PmroadmCAlmHotReset_Object = MibScalar
pmroadmCAlmHotReset = _PmroadmCAlmHotReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 2, 1, 2, 66, 3),
    _PmroadmCAlmHotReset_Type()
)
pmroadmCAlmHotReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmroadmCAlmHotReset.setStatus("current")
_PmroadmCAlmSwitchNotReady_Type = EkiOnOff
_PmroadmCAlmSwitchNotReady_Object = MibScalar
pmroadmCAlmSwitchNotReady = _PmroadmCAlmSwitchNotReady_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 2, 1, 2, 66, 5),
    _PmroadmCAlmSwitchNotReady_Type()
)
pmroadmCAlmSwitchNotReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmroadmCAlmSwitchNotReady.setStatus("current")
_PmroadmCAlmmoduleAlarms_ObjectIdentity = ObjectIdentity
pmroadmCAlmmoduleAlarms = _PmroadmCAlmmoduleAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 35, 2, 1, 2, 67)
)
_PmroadmCAlmModuleTempHighAla_Type = EkiOnOff
_PmroadmCAlmModuleTempHighAla_Object = MibScalar
pmroadmCAlmModuleTempHighAla = _PmroadmCAlmModuleTempHighAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 2, 1, 2, 67, 2),
    _PmroadmCAlmModuleTempHighAla_Type()
)
pmroadmCAlmModuleTempHighAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmroadmCAlmModuleTempHighAla.setStatus("current")
_PmroadmCAlmCaseTempHighAla_Type = EkiOnOff
_PmroadmCAlmCaseTempHighAla_Object = MibScalar
pmroadmCAlmCaseTempHighAla = _PmroadmCAlmCaseTempHighAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 2, 1, 2, 67, 4),
    _PmroadmCAlmCaseTempHighAla_Type()
)
pmroadmCAlmCaseTempHighAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmroadmCAlmCaseTempHighAla.setStatus("current")
_PmroadmCAlmmoduleDegrad_ObjectIdentity = ObjectIdentity
pmroadmCAlmmoduleDegrad = _PmroadmCAlmmoduleDegrad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 35, 2, 1, 2, 68)
)
_PmroadmCAlmModuleTempHighDeg_Type = EkiOnOff
_PmroadmCAlmModuleTempHighDeg_Object = MibScalar
pmroadmCAlmModuleTempHighDeg = _PmroadmCAlmModuleTempHighDeg_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 2, 1, 2, 68, 2),
    _PmroadmCAlmModuleTempHighDeg_Type()
)
pmroadmCAlmModuleTempHighDeg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmroadmCAlmModuleTempHighDeg.setStatus("current")
_PmroadmCAlmCaseTempHighDeg_Type = EkiOnOff
_PmroadmCAlmCaseTempHighDeg_Object = MibScalar
pmroadmCAlmCaseTempHighDeg = _PmroadmCAlmCaseTempHighDeg_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 2, 1, 2, 68, 4),
    _PmroadmCAlmCaseTempHighDeg_Type()
)
pmroadmCAlmCaseTempHighDeg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmroadmCAlmCaseTempHighDeg.setStatus("current")
_PmroadmCAlmOtherCrit_ObjectIdentity = ObjectIdentity
pmroadmCAlmOtherCrit = _PmroadmCAlmOtherCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 35, 2, 1, 3)
)
_PmroadmCAlmsynthAlm0_ObjectIdentity = ObjectIdentity
pmroadmCAlmsynthAlm0 = _PmroadmCAlmsynthAlm0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 35, 2, 1, 3, 0)
)
_PmroadmCAlmInServiceNotReady_Type = EkiOnOff
_PmroadmCAlmInServiceNotReady_Object = MibScalar
pmroadmCAlmInServiceNotReady = _PmroadmCAlmInServiceNotReady_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 2, 1, 3, 0, 1),
    _PmroadmCAlmInServiceNotReady_Type()
)
pmroadmCAlmInServiceNotReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmroadmCAlmInServiceNotReady.setStatus("current")
_PmroadmCAlmModuleGlobFailure_Type = EkiOnOff
_PmroadmCAlmModuleGlobFailure_Object = MibScalar
pmroadmCAlmModuleGlobFailure = _PmroadmCAlmModuleGlobFailure_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 2, 1, 3, 0, 9),
    _PmroadmCAlmModuleGlobFailure_Type()
)
pmroadmCAlmModuleGlobFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmroadmCAlmModuleGlobFailure.setStatus("current")
_PmroadmCAlmDefFuseA_Type = EkiOnOff
_PmroadmCAlmDefFuseA_Object = MibScalar
pmroadmCAlmDefFuseA = _PmroadmCAlmDefFuseA_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 2, 1, 3, 0, 15),
    _PmroadmCAlmDefFuseA_Type()
)
pmroadmCAlmDefFuseA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmroadmCAlmDefFuseA.setStatus("current")
_PmroadmCAlmDefFuseB_Type = EkiOnOff
_PmroadmCAlmDefFuseB_Object = MibScalar
pmroadmCAlmDefFuseB = _PmroadmCAlmDefFuseB_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 2, 1, 3, 0, 16),
    _PmroadmCAlmDefFuseB_Type()
)
pmroadmCAlmDefFuseB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmroadmCAlmDefFuseB.setStatus("current")
_PmroadmCAlmsynthAlm7_ObjectIdentity = ObjectIdentity
pmroadmCAlmsynthAlm7 = _PmroadmCAlmsynthAlm7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 35, 2, 1, 3, 7)
)
_PmroadmCAlmInitNotCompl_Type = EkiOnOff
_PmroadmCAlmInitNotCompl_Object = MibScalar
pmroadmCAlmInitNotCompl = _PmroadmCAlmInitNotCompl_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 2, 1, 3, 7, 2),
    _PmroadmCAlmInitNotCompl_Type()
)
pmroadmCAlmInitNotCompl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmroadmCAlmInitNotCompl.setStatus("current")
_PmroadmCAlmSwitchDegrade_Type = EkiOnOff
_PmroadmCAlmSwitchDegrade_Object = MibScalar
pmroadmCAlmSwitchDegrade = _PmroadmCAlmSwitchDegrade_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 2, 1, 3, 7, 9),
    _PmroadmCAlmSwitchDegrade_Type()
)
pmroadmCAlmSwitchDegrade.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmroadmCAlmSwitchDegrade.setStatus("current")
_PmroadmCAlmSwitchAlm_Type = EkiOnOff
_PmroadmCAlmSwitchAlm_Object = MibScalar
pmroadmCAlmSwitchAlm = _PmroadmCAlmSwitchAlm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 2, 1, 3, 7, 10),
    _PmroadmCAlmSwitchAlm_Type()
)
pmroadmCAlmSwitchAlm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmroadmCAlmSwitchAlm.setStatus("current")
_PmroadmCmeasures_ObjectIdentity = ObjectIdentity
pmroadmCmeasures = _PmroadmCmeasures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 35, 3)
)
_PmroadmCMesrOther_ObjectIdentity = ObjectIdentity
pmroadmCMesrOther = _PmroadmCMesrOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 35, 3, 1)
)


class _PmroadmCMesrswitchTemp_Type(Unsigned32):
    """Custom type pmroadmCMesrswitchTemp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmroadmCMesrswitchTemp_Type.__name__ = "Unsigned32"
_PmroadmCMesrswitchTemp_Object = MibScalar
pmroadmCMesrswitchTemp = _PmroadmCMesrswitchTemp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 3, 1, 16),
    _PmroadmCMesrswitchTemp_Type()
)
pmroadmCMesrswitchTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmroadmCMesrswitchTemp.setStatus("current")


class _PmroadmCMesrmoduleTemp_Type(Unsigned32):
    """Custom type pmroadmCMesrmoduleTemp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmroadmCMesrmoduleTemp_Type.__name__ = "Unsigned32"
_PmroadmCMesrmoduleTemp_Object = MibScalar
pmroadmCMesrmoduleTemp = _PmroadmCMesrmoduleTemp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 3, 1, 64),
    _PmroadmCMesrmoduleTemp_Type()
)
pmroadmCMesrmoduleTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmroadmCMesrmoduleTemp.setStatus("current")


class _PmroadmCMesrcaseTemp_Type(Unsigned32):
    """Custom type pmroadmCMesrcaseTemp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmroadmCMesrcaseTemp_Type.__name__ = "Unsigned32"
_PmroadmCMesrcaseTemp_Object = MibScalar
pmroadmCMesrcaseTemp = _PmroadmCMesrcaseTemp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 3, 1, 65),
    _PmroadmCMesrcaseTemp_Type()
)
pmroadmCMesrcaseTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmroadmCMesrcaseTemp.setStatus("current")
_PmroadmCcontrolsWrite_ObjectIdentity = ObjectIdentity
pmroadmCcontrolsWrite = _PmroadmCcontrolsWrite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 35, 6)
)
_PmroadmCCtrlOther_ObjectIdentity = ObjectIdentity
pmroadmCCtrlOther = _PmroadmCCtrlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 35, 6, 1)
)
_PmroadmCCtrlsynth0_ObjectIdentity = ObjectIdentity
pmroadmCCtrlsynth0 = _PmroadmCCtrlsynth0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 35, 6, 1, 0)
)
_PmroadmCCtrlConfLoad_Type = EkiOnOff
_PmroadmCCtrlConfLoad_Object = MibScalar
pmroadmCCtrlConfLoad = _PmroadmCCtrlConfLoad_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 6, 1, 0, 1),
    _PmroadmCCtrlConfLoad_Type()
)
pmroadmCCtrlConfLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmroadmCCtrlConfLoad.setStatus("current")
_PmroadmCCtrlConfFlash_Type = EkiOnOff
_PmroadmCCtrlConfFlash_Object = MibScalar
pmroadmCCtrlConfFlash = _PmroadmCCtrlConfFlash_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 6, 1, 0, 9),
    _PmroadmCCtrlConfFlash_Type()
)
pmroadmCCtrlConfFlash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmroadmCCtrlConfFlash.setStatus("current")
_PmroadmCCtrlConfClear_Type = EkiOnOff
_PmroadmCCtrlConfClear_Object = MibScalar
pmroadmCCtrlConfClear = _PmroadmCCtrlConfClear_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 6, 1, 0, 13),
    _PmroadmCCtrlConfClear_Type()
)
pmroadmCCtrlConfClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmroadmCCtrlConfClear.setStatus("current")
_PmroadmCCtrlsynth4_ObjectIdentity = ObjectIdentity
pmroadmCCtrlsynth4 = _PmroadmCCtrlsynth4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 35, 6, 1, 4)
)
_PmroadmCCtrlCorrelatOn_Type = EkiOnOff
_PmroadmCCtrlCorrelatOn_Object = MibScalar
pmroadmCCtrlCorrelatOn = _PmroadmCCtrlCorrelatOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 6, 1, 4, 1),
    _PmroadmCCtrlCorrelatOn_Type()
)
pmroadmCCtrlCorrelatOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmroadmCCtrlCorrelatOn.setStatus("current")
_PmroadmCCtrlCorrelatOff_Type = EkiOnOff
_PmroadmCCtrlCorrelatOff_Object = MibScalar
pmroadmCCtrlCorrelatOff = _PmroadmCCtrlCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 6, 1, 4, 2),
    _PmroadmCCtrlCorrelatOff_Type()
)
pmroadmCCtrlCorrelatOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmroadmCCtrlCorrelatOff.setStatus("current")
_PmroadmCCtrlswMgnt_ObjectIdentity = ObjectIdentity
pmroadmCCtrlswMgnt = _PmroadmCCtrlswMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 35, 6, 1, 5)
)
_PmroadmCCtrlColdReset_Type = EkiOnOff
_PmroadmCCtrlColdReset_Object = MibScalar
pmroadmCCtrlColdReset = _PmroadmCCtrlColdReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 6, 1, 5, 2),
    _PmroadmCCtrlColdReset_Type()
)
pmroadmCCtrlColdReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmroadmCCtrlColdReset.setStatus("current")
_PmroadmCCtrlWarmReset_Type = EkiOnOff
_PmroadmCCtrlWarmReset_Object = MibScalar
pmroadmCCtrlWarmReset = _PmroadmCCtrlWarmReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 6, 1, 5, 3),
    _PmroadmCCtrlWarmReset_Type()
)
pmroadmCCtrlWarmReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmroadmCCtrlWarmReset.setStatus("current")
_PmroadmCCtrlswitchCtrl_ObjectIdentity = ObjectIdentity
pmroadmCCtrlswitchCtrl = _PmroadmCCtrlswitchCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 35, 6, 1, 16)
)
_PmroadmCCtrlAllChannelsHighLoss_Type = EkiOnOff
_PmroadmCCtrlAllChannelsHighLoss_Object = MibScalar
pmroadmCCtrlAllChannelsHighLoss = _PmroadmCCtrlAllChannelsHighLoss_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 6, 1, 16, 1),
    _PmroadmCCtrlAllChannelsHighLoss_Type()
)
pmroadmCCtrlAllChannelsHighLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmroadmCCtrlAllChannelsHighLoss.setStatus("current")


class _PmroadmCCtrlcraftSynch_Type(Unsigned32):
    """Custom type pmroadmCCtrlcraftSynch based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmroadmCCtrlcraftSynch_Type.__name__ = "Unsigned32"
_PmroadmCCtrlcraftSynch_Object = MibScalar
pmroadmCCtrlcraftSynch = _PmroadmCCtrlcraftSynch_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 6, 1, 17),
    _PmroadmCCtrlcraftSynch_Type()
)
pmroadmCCtrlcraftSynch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmroadmCCtrlcraftSynch.setStatus("current")
_PmroadmCCtrlledTest_ObjectIdentity = ObjectIdentity
pmroadmCCtrlledTest = _PmroadmCCtrlledTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 35, 6, 1, 64)
)
_PmroadmCCtrlGreenLed_Type = EkiOnOff
_PmroadmCCtrlGreenLed_Object = MibScalar
pmroadmCCtrlGreenLed = _PmroadmCCtrlGreenLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 6, 1, 64, 1),
    _PmroadmCCtrlGreenLed_Type()
)
pmroadmCCtrlGreenLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmroadmCCtrlGreenLed.setStatus("current")
_PmroadmCCtrlRedLed_Type = EkiOnOff
_PmroadmCCtrlRedLed_Object = MibScalar
pmroadmCCtrlRedLed = _PmroadmCCtrlRedLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 6, 1, 64, 2),
    _PmroadmCCtrlRedLed_Type()
)
pmroadmCCtrlRedLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmroadmCCtrlRedLed.setStatus("current")
_PmroadmCCtrlLedOff_Type = EkiOnOff
_PmroadmCCtrlLedOff_Object = MibScalar
pmroadmCCtrlLedOff = _PmroadmCCtrlLedOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 6, 1, 64, 3),
    _PmroadmCCtrlLedOff_Type()
)
pmroadmCCtrlLedOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmroadmCCtrlLedOff.setStatus("current")
_PmroadmCCtrlwavePlanAssignmentsRefreshTable_Object = MibTable
pmroadmCCtrlwavePlanAssignmentsRefreshTable = _PmroadmCCtrlwavePlanAssignmentsRefreshTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 6, 1, 65)
)
if mibBuilder.loadTexts:
    pmroadmCCtrlwavePlanAssignmentsRefreshTable.setStatus("current")
_PmroadmCCtrlwavePlanAssignmentsRefreshEntry_Object = MibTableRow
pmroadmCCtrlwavePlanAssignmentsRefreshEntry = _PmroadmCCtrlwavePlanAssignmentsRefreshEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 6, 1, 65, 1)
)
pmroadmCCtrlwavePlanAssignmentsRefreshEntry.setIndexNames(
    (0, "EKINOPS-PmroadmC-MIB", "pmroadmCCtrlwavePlanAssignmentsRefreshIndex"),
)
if mibBuilder.loadTexts:
    pmroadmCCtrlwavePlanAssignmentsRefreshEntry.setStatus("current")


class _PmroadmCCtrlwavePlanAssignmentsRefreshIndex_Type(Integer32):
    """Custom type pmroadmCCtrlwavePlanAssignmentsRefreshIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_PmroadmCCtrlwavePlanAssignmentsRefreshIndex_Type.__name__ = "Integer32"
_PmroadmCCtrlwavePlanAssignmentsRefreshIndex_Object = MibTableColumn
pmroadmCCtrlwavePlanAssignmentsRefreshIndex = _PmroadmCCtrlwavePlanAssignmentsRefreshIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 6, 1, 65, 1, 1),
    _PmroadmCCtrlwavePlanAssignmentsRefreshIndex_Type()
)
pmroadmCCtrlwavePlanAssignmentsRefreshIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmroadmCCtrlwavePlanAssignmentsRefreshIndex.setStatus("current")
_PmroadmCCtrlWaveStatusRefreshPortn_Type = EkiOnOff
_PmroadmCCtrlWaveStatusRefreshPortn_Object = MibTableColumn
pmroadmCCtrlWaveStatusRefreshPortn = _PmroadmCCtrlWaveStatusRefreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 6, 1, 65, 1, 2),
    _PmroadmCCtrlWaveStatusRefreshPortn_Type()
)
pmroadmCCtrlWaveStatusRefreshPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmroadmCCtrlWaveStatusRefreshPortn.setStatus("current")
_PmroadmCCtrlWaveNarrowingRefreshPortn_Type = Integer32
_PmroadmCCtrlWaveNarrowingRefreshPortn_Object = MibTableColumn
pmroadmCCtrlWaveNarrowingRefreshPortn = _PmroadmCCtrlWaveNarrowingRefreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 6, 1, 65, 1, 3),
    _PmroadmCCtrlWaveNarrowingRefreshPortn_Type()
)
pmroadmCCtrlWaveNarrowingRefreshPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmroadmCCtrlWaveNarrowingRefreshPortn.setStatus("current")
_PmroadmCCtrlWaveCenterFrequencyRefreshPortn_Type = Integer32
_PmroadmCCtrlWaveCenterFrequencyRefreshPortn_Object = MibTableColumn
pmroadmCCtrlWaveCenterFrequencyRefreshPortn = _PmroadmCCtrlWaveCenterFrequencyRefreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 6, 1, 65, 1, 4),
    _PmroadmCCtrlWaveCenterFrequencyRefreshPortn_Type()
)
pmroadmCCtrlWaveCenterFrequencyRefreshPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmroadmCCtrlWaveCenterFrequencyRefreshPortn.setStatus("current")
_PmroadmCCtrlWaveOOSRefreshPortn_Type = EkiOnOff
_PmroadmCCtrlWaveOOSRefreshPortn_Object = MibTableColumn
pmroadmCCtrlWaveOOSRefreshPortn = _PmroadmCCtrlWaveOOSRefreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 6, 1, 65, 1, 5),
    _PmroadmCCtrlWaveOOSRefreshPortn_Type()
)
pmroadmCCtrlWaveOOSRefreshPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmroadmCCtrlWaveOOSRefreshPortn.setStatus("current")
_PmroadmCCtrlWaveAttenuationRefreshPortn_Type = Integer32
_PmroadmCCtrlWaveAttenuationRefreshPortn_Object = MibTableColumn
pmroadmCCtrlWaveAttenuationRefreshPortn = _PmroadmCCtrlWaveAttenuationRefreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 6, 1, 65, 1, 6),
    _PmroadmCCtrlWaveAttenuationRefreshPortn_Type()
)
pmroadmCCtrlWaveAttenuationRefreshPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmroadmCCtrlWaveAttenuationRefreshPortn.setStatus("current")
_PmroadmCCtrlWaveItuRefreshPortn_Type = DisplayString
_PmroadmCCtrlWaveItuRefreshPortn_Object = MibTableColumn
pmroadmCCtrlWaveItuRefreshPortn = _PmroadmCCtrlWaveItuRefreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 6, 1, 65, 1, 7),
    _PmroadmCCtrlWaveItuRefreshPortn_Type()
)
pmroadmCCtrlWaveItuRefreshPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmroadmCCtrlWaveItuRefreshPortn.setStatus("current")
_PmroadmCCtrlWaveDegreeRefreshPortn_Type = Integer32
_PmroadmCCtrlWaveDegreeRefreshPortn_Object = MibTableColumn
pmroadmCCtrlWaveDegreeRefreshPortn = _PmroadmCCtrlWaveDegreeRefreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 6, 1, 65, 1, 8),
    _PmroadmCCtrlWaveDegreeRefreshPortn_Type()
)
pmroadmCCtrlWaveDegreeRefreshPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmroadmCCtrlWaveDegreeRefreshPortn.setStatus("current")
_PmroadmCCtrlUsageRefreshPortn_Type = EkiOnOff
_PmroadmCCtrlUsageRefreshPortn_Object = MibTableColumn
pmroadmCCtrlUsageRefreshPortn = _PmroadmCCtrlUsageRefreshPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 6, 1, 65, 1, 16),
    _PmroadmCCtrlUsageRefreshPortn_Type()
)
pmroadmCCtrlUsageRefreshPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmroadmCCtrlUsageRefreshPortn.setStatus("current")
_PmroadmCCtrlwavePlanAssignmentsWorkTable_Object = MibTable
pmroadmCCtrlwavePlanAssignmentsWorkTable = _PmroadmCCtrlwavePlanAssignmentsWorkTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 6, 1, 66)
)
if mibBuilder.loadTexts:
    pmroadmCCtrlwavePlanAssignmentsWorkTable.setStatus("current")
_PmroadmCCtrlwavePlanAssignmentsWorkEntry_Object = MibTableRow
pmroadmCCtrlwavePlanAssignmentsWorkEntry = _PmroadmCCtrlwavePlanAssignmentsWorkEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 6, 1, 66, 1)
)
pmroadmCCtrlwavePlanAssignmentsWorkEntry.setIndexNames(
    (0, "EKINOPS-PmroadmC-MIB", "pmroadmCCtrlwavePlanAssignmentsWorkIndex"),
)
if mibBuilder.loadTexts:
    pmroadmCCtrlwavePlanAssignmentsWorkEntry.setStatus("current")


class _PmroadmCCtrlwavePlanAssignmentsWorkIndex_Type(Integer32):
    """Custom type pmroadmCCtrlwavePlanAssignmentsWorkIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_PmroadmCCtrlwavePlanAssignmentsWorkIndex_Type.__name__ = "Integer32"
_PmroadmCCtrlwavePlanAssignmentsWorkIndex_Object = MibTableColumn
pmroadmCCtrlwavePlanAssignmentsWorkIndex = _PmroadmCCtrlwavePlanAssignmentsWorkIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 6, 1, 66, 1, 1),
    _PmroadmCCtrlwavePlanAssignmentsWorkIndex_Type()
)
pmroadmCCtrlwavePlanAssignmentsWorkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmroadmCCtrlwavePlanAssignmentsWorkIndex.setStatus("current")
_PmroadmCCtrlWaveStatusWorkPortn_Type = EkiOnOff
_PmroadmCCtrlWaveStatusWorkPortn_Object = MibTableColumn
pmroadmCCtrlWaveStatusWorkPortn = _PmroadmCCtrlWaveStatusWorkPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 6, 1, 66, 1, 2),
    _PmroadmCCtrlWaveStatusWorkPortn_Type()
)
pmroadmCCtrlWaveStatusWorkPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmroadmCCtrlWaveStatusWorkPortn.setStatus("current")
_PmroadmCCtrlWaveNarrowingWorkPortn_Type = Integer32
_PmroadmCCtrlWaveNarrowingWorkPortn_Object = MibTableColumn
pmroadmCCtrlWaveNarrowingWorkPortn = _PmroadmCCtrlWaveNarrowingWorkPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 6, 1, 66, 1, 3),
    _PmroadmCCtrlWaveNarrowingWorkPortn_Type()
)
pmroadmCCtrlWaveNarrowingWorkPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmroadmCCtrlWaveNarrowingWorkPortn.setStatus("current")
_PmroadmCCtrlWaveCenterFrequencyWorkPortn_Type = Integer32
_PmroadmCCtrlWaveCenterFrequencyWorkPortn_Object = MibTableColumn
pmroadmCCtrlWaveCenterFrequencyWorkPortn = _PmroadmCCtrlWaveCenterFrequencyWorkPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 6, 1, 66, 1, 4),
    _PmroadmCCtrlWaveCenterFrequencyWorkPortn_Type()
)
pmroadmCCtrlWaveCenterFrequencyWorkPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmroadmCCtrlWaveCenterFrequencyWorkPortn.setStatus("current")
_PmroadmCCtrlWaveOOSWorkPortn_Type = EkiOnOff
_PmroadmCCtrlWaveOOSWorkPortn_Object = MibTableColumn
pmroadmCCtrlWaveOOSWorkPortn = _PmroadmCCtrlWaveOOSWorkPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 6, 1, 66, 1, 5),
    _PmroadmCCtrlWaveOOSWorkPortn_Type()
)
pmroadmCCtrlWaveOOSWorkPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmroadmCCtrlWaveOOSWorkPortn.setStatus("current")
_PmroadmCCtrlWaveAttenuationWorkPortn_Type = Integer32
_PmroadmCCtrlWaveAttenuationWorkPortn_Object = MibTableColumn
pmroadmCCtrlWaveAttenuationWorkPortn = _PmroadmCCtrlWaveAttenuationWorkPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 6, 1, 66, 1, 6),
    _PmroadmCCtrlWaveAttenuationWorkPortn_Type()
)
pmroadmCCtrlWaveAttenuationWorkPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmroadmCCtrlWaveAttenuationWorkPortn.setStatus("current")
_PmroadmCCtrlWaveItuWorkPortn_Type = DisplayString
_PmroadmCCtrlWaveItuWorkPortn_Object = MibTableColumn
pmroadmCCtrlWaveItuWorkPortn = _PmroadmCCtrlWaveItuWorkPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 6, 1, 66, 1, 7),
    _PmroadmCCtrlWaveItuWorkPortn_Type()
)
pmroadmCCtrlWaveItuWorkPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmroadmCCtrlWaveItuWorkPortn.setStatus("current")
_PmroadmCCtrlWaveDegreeWorkPortn_Type = Integer32
_PmroadmCCtrlWaveDegreeWorkPortn_Object = MibTableColumn
pmroadmCCtrlWaveDegreeWorkPortn = _PmroadmCCtrlWaveDegreeWorkPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 6, 1, 66, 1, 8),
    _PmroadmCCtrlWaveDegreeWorkPortn_Type()
)
pmroadmCCtrlWaveDegreeWorkPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmroadmCCtrlWaveDegreeWorkPortn.setStatus("current")
_PmroadmCCtrlUsageWorkPortn_Type = EkiOnOff
_PmroadmCCtrlUsageWorkPortn_Object = MibTableColumn
pmroadmCCtrlUsageWorkPortn = _PmroadmCCtrlUsageWorkPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 6, 1, 66, 1, 16),
    _PmroadmCCtrlUsageWorkPortn_Type()
)
pmroadmCCtrlUsageWorkPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmroadmCCtrlUsageWorkPortn.setStatus("current")
_PmroadmCCtrlbuildFromMgntPlan_Type = DisplayString
_PmroadmCCtrlbuildFromMgntPlan_Object = MibScalar
pmroadmCCtrlbuildFromMgntPlan = _PmroadmCCtrlbuildFromMgntPlan_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 6, 1, 67),
    _PmroadmCCtrlbuildFromMgntPlan_Type()
)
pmroadmCCtrlbuildFromMgntPlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmroadmCCtrlbuildFromMgntPlan.setStatus("current")
_PmroadmCCtrlloadToWorkplan_Type = PmroadmCPlanNumber
_PmroadmCCtrlloadToWorkplan_Object = MibScalar
pmroadmCCtrlloadToWorkplan = _PmroadmCCtrlloadToWorkplan_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 6, 1, 68),
    _PmroadmCCtrlloadToWorkplan_Type()
)
pmroadmCCtrlloadToWorkplan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmroadmCCtrlloadToWorkplan.setStatus("current")
_PmroadmCCtrlsaveWorkPlanTo_Type = PmroadmCPlanNumber
_PmroadmCCtrlsaveWorkPlanTo_Object = MibScalar
pmroadmCCtrlsaveWorkPlanTo = _PmroadmCCtrlsaveWorkPlanTo_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 6, 1, 69),
    _PmroadmCCtrlsaveWorkPlanTo_Type()
)
pmroadmCCtrlsaveWorkPlanTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmroadmCCtrlsaveWorkPlanTo.setStatus("current")
_PmroadmCCtrlloadPlanToUse_Type = PmroadmCPlanNumber
_PmroadmCCtrlloadPlanToUse_Object = MibScalar
pmroadmCCtrlloadPlanToUse = _PmroadmCCtrlloadPlanToUse_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 6, 1, 70),
    _PmroadmCCtrlloadPlanToUse_Type()
)
pmroadmCCtrlloadPlanToUse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmroadmCCtrlloadPlanToUse.setStatus("current")
_PmroadmCCtrlrefreshWithPlan_Type = PmroadmCPlanNumber
_PmroadmCCtrlrefreshWithPlan_Object = MibScalar
pmroadmCCtrlrefreshWithPlan = _PmroadmCCtrlrefreshWithPlan_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 6, 1, 71),
    _PmroadmCCtrlrefreshWithPlan_Type()
)
pmroadmCCtrlrefreshWithPlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmroadmCCtrlrefreshWithPlan.setStatus("current")
_PmroadmCCtrlsavePlanToFile_Type = PmroadmCPlanNumber
_PmroadmCCtrlsavePlanToFile_Object = MibScalar
pmroadmCCtrlsavePlanToFile = _PmroadmCCtrlsavePlanToFile_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 6, 1, 72),
    _PmroadmCCtrlsavePlanToFile_Type()
)
pmroadmCCtrlsavePlanToFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmroadmCCtrlsavePlanToFile.setStatus("current")
_PmroadmCCtrlloadPlanFromFile_Type = PmroadmCPlanNumber
_PmroadmCCtrlloadPlanFromFile_Object = MibScalar
pmroadmCCtrlloadPlanFromFile = _PmroadmCCtrlloadPlanFromFile_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 6, 1, 73),
    _PmroadmCCtrlloadPlanFromFile_Type()
)
pmroadmCCtrlloadPlanFromFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmroadmCCtrlloadPlanFromFile.setStatus("current")
_PmroadmCCtrlExpress_ObjectIdentity = ObjectIdentity
pmroadmCCtrlExpress = _PmroadmCCtrlExpress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 35, 6, 2)
)
_PmroadmCCtrlexpTxCommonAttDegTable_Object = MibTable
pmroadmCCtrlexpTxCommonAttDegTable = _PmroadmCCtrlexpTxCommonAttDegTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 6, 2, 19)
)
if mibBuilder.loadTexts:
    pmroadmCCtrlexpTxCommonAttDegTable.setStatus("current")
_PmroadmCCtrlexpTxCommonAttDegEntry_Object = MibTableRow
pmroadmCCtrlexpTxCommonAttDegEntry = _PmroadmCCtrlexpTxCommonAttDegEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 6, 2, 19, 1)
)
pmroadmCCtrlexpTxCommonAttDegEntry.setIndexNames(
    (0, "EKINOPS-PmroadmC-MIB", "pmroadmCCtrlexpTxCommonAttDegIndex"),
)
if mibBuilder.loadTexts:
    pmroadmCCtrlexpTxCommonAttDegEntry.setStatus("current")


class _PmroadmCCtrlexpTxCommonAttDegIndex_Type(Integer32):
    """Custom type pmroadmCCtrlexpTxCommonAttDegIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_PmroadmCCtrlexpTxCommonAttDegIndex_Type.__name__ = "Integer32"
_PmroadmCCtrlexpTxCommonAttDegIndex_Object = MibTableColumn
pmroadmCCtrlexpTxCommonAttDegIndex = _PmroadmCCtrlexpTxCommonAttDegIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 6, 2, 19, 1, 1),
    _PmroadmCCtrlexpTxCommonAttDegIndex_Type()
)
pmroadmCCtrlexpTxCommonAttDegIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmroadmCCtrlexpTxCommonAttDegIndex.setStatus("current")


class _PmroadmCCtrlexpTxCommonAttDegPortn_Type(Integer32):
    """Custom type pmroadmCCtrlexpTxCommonAttDegPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmroadmCCtrlexpTxCommonAttDegPortn_Type.__name__ = "Integer32"
_PmroadmCCtrlexpTxCommonAttDegPortn_Object = MibTableColumn
pmroadmCCtrlexpTxCommonAttDegPortn = _PmroadmCCtrlexpTxCommonAttDegPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 6, 2, 19, 1, 2),
    _PmroadmCCtrlexpTxCommonAttDegPortn_Type()
)
pmroadmCCtrlexpTxCommonAttDegPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmroadmCCtrlexpTxCommonAttDegPortn.setStatus("current")
_PmroadmCCtrlexpRxCommonAttDegTable_Object = MibTable
pmroadmCCtrlexpRxCommonAttDegTable = _PmroadmCCtrlexpRxCommonAttDegTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 6, 2, 43)
)
if mibBuilder.loadTexts:
    pmroadmCCtrlexpRxCommonAttDegTable.setStatus("current")
_PmroadmCCtrlexpRxCommonAttDegEntry_Object = MibTableRow
pmroadmCCtrlexpRxCommonAttDegEntry = _PmroadmCCtrlexpRxCommonAttDegEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 6, 2, 43, 1)
)
pmroadmCCtrlexpRxCommonAttDegEntry.setIndexNames(
    (0, "EKINOPS-PmroadmC-MIB", "pmroadmCCtrlexpRxCommonAttDegIndex"),
)
if mibBuilder.loadTexts:
    pmroadmCCtrlexpRxCommonAttDegEntry.setStatus("current")


class _PmroadmCCtrlexpRxCommonAttDegIndex_Type(Integer32):
    """Custom type pmroadmCCtrlexpRxCommonAttDegIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_PmroadmCCtrlexpRxCommonAttDegIndex_Type.__name__ = "Integer32"
_PmroadmCCtrlexpRxCommonAttDegIndex_Object = MibTableColumn
pmroadmCCtrlexpRxCommonAttDegIndex = _PmroadmCCtrlexpRxCommonAttDegIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 6, 2, 43, 1, 1),
    _PmroadmCCtrlexpRxCommonAttDegIndex_Type()
)
pmroadmCCtrlexpRxCommonAttDegIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmroadmCCtrlexpRxCommonAttDegIndex.setStatus("current")


class _PmroadmCCtrlexpRxCommonAttDegPortn_Type(Integer32):
    """Custom type pmroadmCCtrlexpRxCommonAttDegPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PmroadmCCtrlexpRxCommonAttDegPortn_Type.__name__ = "Integer32"
_PmroadmCCtrlexpRxCommonAttDegPortn_Object = MibTableColumn
pmroadmCCtrlexpRxCommonAttDegPortn = _PmroadmCCtrlexpRxCommonAttDegPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 6, 2, 43, 1, 2),
    _PmroadmCCtrlexpRxCommonAttDegPortn_Type()
)
pmroadmCCtrlexpRxCommonAttDegPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmroadmCCtrlexpRxCommonAttDegPortn.setStatus("current")
_PmroadmCCtrlapplyPlanUpdate_ObjectIdentity = ObjectIdentity
pmroadmCCtrlapplyPlanUpdate = _PmroadmCCtrlapplyPlanUpdate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 35, 6, 2, 44)
)
_PmroadmCCtrlApply_Type = EkiOnOff
_PmroadmCCtrlApply_Object = MibScalar
pmroadmCCtrlApply = _PmroadmCCtrlApply_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 6, 2, 44, 1),
    _PmroadmCCtrlApply_Type()
)
pmroadmCCtrlApply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmroadmCCtrlApply.setStatus("current")
_PmroadmCCtrlLine_ObjectIdentity = ObjectIdentity
pmroadmCCtrlLine = _PmroadmCCtrlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 35, 6, 3)
)
_PmroadmCri_ObjectIdentity = ObjectIdentity
pmroadmCri = _PmroadmCri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 35, 7)
)
_PmroadmCriTable_ObjectIdentity = ObjectIdentity
pmroadmCriTable = _PmroadmCriTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 35, 7, 1)
)
_PmroadmCRinvPortTable_Object = MibTable
pmroadmCRinvPortTable = _PmroadmCRinvPortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 7, 1, 1)
)
if mibBuilder.loadTexts:
    pmroadmCRinvPortTable.setStatus("current")
_PmroadmCRinvPortEntry_Object = MibTableRow
pmroadmCRinvPortEntry = _PmroadmCRinvPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 7, 1, 1, 1)
)
pmroadmCRinvPortEntry.setIndexNames(
    (0, "EKINOPS-PmroadmC-MIB", "pmroadmCRinvPortIndex"),
)
if mibBuilder.loadTexts:
    pmroadmCRinvPortEntry.setStatus("current")


class _PmroadmCRinvPortIndex_Type(Integer32):
    """Custom type pmroadmCRinvPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_PmroadmCRinvPortIndex_Type.__name__ = "Integer32"
_PmroadmCRinvPortIndex_Object = MibTableColumn
pmroadmCRinvPortIndex = _PmroadmCRinvPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 7, 1, 1, 1, 1),
    _PmroadmCRinvPortIndex_Type()
)
pmroadmCRinvPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmroadmCRinvPortIndex.setStatus("current")
_PmroadmCRinvPort_Type = DisplayString
_PmroadmCRinvPort_Object = MibTableColumn
pmroadmCRinvPort = _PmroadmCRinvPort_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 7, 1, 1, 1, 2),
    _PmroadmCRinvPort_Type()
)
pmroadmCRinvPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmroadmCRinvPort.setStatus("current")
_PmroadmCRinvLineTable_Object = MibTable
pmroadmCRinvLineTable = _PmroadmCRinvLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 7, 1, 2)
)
if mibBuilder.loadTexts:
    pmroadmCRinvLineTable.setStatus("current")
_PmroadmCRinvLineEntry_Object = MibTableRow
pmroadmCRinvLineEntry = _PmroadmCRinvLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 7, 1, 2, 1)
)
pmroadmCRinvLineEntry.setIndexNames(
    (0, "EKINOPS-PmroadmC-MIB", "pmroadmCRinvLineIndex"),
)
if mibBuilder.loadTexts:
    pmroadmCRinvLineEntry.setStatus("current")


class _PmroadmCRinvLineIndex_Type(Integer32):
    """Custom type pmroadmCRinvLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_PmroadmCRinvLineIndex_Type.__name__ = "Integer32"
_PmroadmCRinvLineIndex_Object = MibTableColumn
pmroadmCRinvLineIndex = _PmroadmCRinvLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 7, 1, 2, 1, 1),
    _PmroadmCRinvLineIndex_Type()
)
pmroadmCRinvLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmroadmCRinvLineIndex.setStatus("current")
_PmroadmCRinvxfpLine_Type = DisplayString
_PmroadmCRinvxfpLine_Object = MibTableColumn
pmroadmCRinvxfpLine = _PmroadmCRinvxfpLine_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 7, 1, 2, 1, 2),
    _PmroadmCRinvxfpLine_Type()
)
pmroadmCRinvxfpLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmroadmCRinvxfpLine.setStatus("current")
_PmroadmCRinvReloadInventory_Type = EkiOnOff
_PmroadmCRinvReloadInventory_Object = MibScalar
pmroadmCRinvReloadInventory = _PmroadmCRinvReloadInventory_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 7, 2),
    _PmroadmCRinvReloadInventory_Type()
)
pmroadmCRinvReloadInventory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmroadmCRinvReloadInventory.setStatus("current")
_PmroadmCRinvHwPlatform_Type = DisplayString
_PmroadmCRinvHwPlatform_Object = MibScalar
pmroadmCRinvHwPlatform = _PmroadmCRinvHwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 7, 4),
    _PmroadmCRinvHwPlatform_Type()
)
pmroadmCRinvHwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmroadmCRinvHwPlatform.setStatus("current")
_PmroadmCRinvSwPlatform_Type = DisplayString
_PmroadmCRinvSwPlatform_Object = MibScalar
pmroadmCRinvSwPlatform = _PmroadmCRinvSwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 7, 5),
    _PmroadmCRinvSwPlatform_Type()
)
pmroadmCRinvSwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmroadmCRinvSwPlatform.setStatus("current")
_PmroadmCConfig_ObjectIdentity = ObjectIdentity
pmroadmCConfig = _PmroadmCConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 35, 9)
)
_PmroadmCCfgLsd_ObjectIdentity = ObjectIdentity
pmroadmCCfgLsd = _PmroadmCCfgLsd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 35, 9, 1)
)
_PmroadmCtableclientLsd_ObjectIdentity = ObjectIdentity
pmroadmCtableclientLsd = _PmroadmCtableclientLsd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 35, 9, 1, 1)
)
_PmroadmCCfgStartup_ObjectIdentity = ObjectIdentity
pmroadmCCfgStartup = _PmroadmCCfgStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 35, 9, 2)
)
_PmroadmCCfgClientStartupTable_Object = MibTable
pmroadmCCfgClientStartupTable = _PmroadmCCfgClientStartupTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 9, 2, 1)
)
if mibBuilder.loadTexts:
    pmroadmCCfgClientStartupTable.setStatus("current")
_PmroadmCCfgClientStartupEntry_Object = MibTableRow
pmroadmCCfgClientStartupEntry = _PmroadmCCfgClientStartupEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 9, 2, 1, 1)
)
pmroadmCCfgClientStartupEntry.setIndexNames(
    (0, "EKINOPS-PmroadmC-MIB", "pmroadmCCfgClientStartupIndex"),
)
if mibBuilder.loadTexts:
    pmroadmCCfgClientStartupEntry.setStatus("current")


class _PmroadmCCfgClientStartupIndex_Type(Integer32):
    """Custom type pmroadmCCfgClientStartupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_PmroadmCCfgClientStartupIndex_Type.__name__ = "Integer32"
_PmroadmCCfgClientStartupIndex_Object = MibTableColumn
pmroadmCCfgClientStartupIndex = _PmroadmCCfgClientStartupIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 9, 2, 1, 1, 1),
    _PmroadmCCfgClientStartupIndex_Type()
)
pmroadmCCfgClientStartupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmroadmCCfgClientStartupIndex.setStatus("current")


class _PmroadmCCfgLineaRxCommonAttDegPortn_Type(Unsigned32):
    """Custom type pmroadmCCfgLineaRxCommonAttDegPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmroadmCCfgLineaRxCommonAttDegPortn_Type.__name__ = "Unsigned32"
_PmroadmCCfgLineaRxCommonAttDegPortn_Object = MibTableColumn
pmroadmCCfgLineaRxCommonAttDegPortn = _PmroadmCCfgLineaRxCommonAttDegPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 9, 2, 1, 1, 3),
    _PmroadmCCfgLineaRxCommonAttDegPortn_Type()
)
pmroadmCCfgLineaRxCommonAttDegPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmroadmCCfgLineaRxCommonAttDegPortn.setStatus("current")
_PmroadmCtablelineStartup_ObjectIdentity = ObjectIdentity
pmroadmCtablelineStartup = _PmroadmCtablelineStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 35, 9, 2, 2)
)
_PmroadmCtableclientsRoadm_ObjectIdentity = ObjectIdentity
pmroadmCtableclientsRoadm = _PmroadmCtableclientsRoadm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 35, 9, 2, 3)
)
_PmroadmCtablelinesRoadm_ObjectIdentity = ObjectIdentity
pmroadmCtablelinesRoadm = _PmroadmCtablelinesRoadm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 35, 9, 2, 4)
)


class _PmroadmCCfgexpGridCurrent_Type(Unsigned32):
    """Custom type pmroadmCCfgexpGridCurrent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmroadmCCfgexpGridCurrent_Type.__name__ = "Unsigned32"
_PmroadmCCfgexpGridCurrent_Object = MibScalar
pmroadmCCfgexpGridCurrent = _PmroadmCCfgexpGridCurrent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 9, 2, 4, 2),
    _PmroadmCCfgexpGridCurrent_Type()
)
pmroadmCCfgexpGridCurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmroadmCCfgexpGridCurrent.setStatus("current")
_PmroadmCtableother_ObjectIdentity = ObjectIdentity
pmroadmCtableother = _PmroadmCtableother_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 35, 9, 2, 5)
)


class _PmroadmCCfgcomponentType_Type(Unsigned32):
    """Custom type pmroadmCCfgcomponentType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmroadmCCfgcomponentType_Type.__name__ = "Unsigned32"
_PmroadmCCfgcomponentType_Object = MibScalar
pmroadmCCfgcomponentType = _PmroadmCCfgcomponentType_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 9, 2, 5, 2),
    _PmroadmCCfgcomponentType_Type()
)
pmroadmCCfgcomponentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmroadmCCfgcomponentType.setStatus("current")


class _PmroadmCCfgmiscellaneous_Type(Unsigned32):
    """Custom type pmroadmCCfgmiscellaneous based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmroadmCCfgmiscellaneous_Type.__name__ = "Unsigned32"
_PmroadmCCfgmiscellaneous_Object = MibScalar
pmroadmCCfgmiscellaneous = _PmroadmCCfgmiscellaneous_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 9, 2, 5, 3),
    _PmroadmCCfgmiscellaneous_Type()
)
pmroadmCCfgmiscellaneous.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmroadmCCfgmiscellaneous.setStatus("current")


class _PmroadmCCfgfirstChannel_Type(Unsigned32):
    """Custom type pmroadmCCfgfirstChannel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmroadmCCfgfirstChannel_Type.__name__ = "Unsigned32"
_PmroadmCCfgfirstChannel_Object = MibScalar
pmroadmCCfgfirstChannel = _PmroadmCCfgfirstChannel_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 9, 2, 5, 4),
    _PmroadmCCfgfirstChannel_Type()
)
pmroadmCCfgfirstChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmroadmCCfgfirstChannel.setStatus("current")


class _PmroadmCCfglastChannel_Type(Unsigned32):
    """Custom type pmroadmCCfglastChannel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmroadmCCfglastChannel_Type.__name__ = "Unsigned32"
_PmroadmCCfglastChannel_Object = MibScalar
pmroadmCCfglastChannel = _PmroadmCCfglastChannel_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 9, 2, 5, 5),
    _PmroadmCCfglastChannel_Type()
)
pmroadmCCfglastChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmroadmCCfglastChannel.setStatus("current")


class _PmroadmCCfggrid_Type(Unsigned32):
    """Custom type pmroadmCCfggrid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_PmroadmCCfggrid_Type.__name__ = "Unsigned32"
_PmroadmCCfggrid_Object = MibScalar
pmroadmCCfggrid = _PmroadmCCfggrid_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 9, 2, 5, 6),
    _PmroadmCCfggrid_Type()
)
pmroadmCCfggrid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmroadmCCfggrid.setStatus("current")
_PmroadmCCfgLabels_ObjectIdentity = ObjectIdentity
pmroadmCCfgLabels = _PmroadmCCfgLabels_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 35, 9, 3)
)
_PmroadmCCfgLabelclientTable_Object = MibTable
pmroadmCCfgLabelclientTable = _PmroadmCCfgLabelclientTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 9, 3, 1)
)
if mibBuilder.loadTexts:
    pmroadmCCfgLabelclientTable.setStatus("current")
_PmroadmCCfgLabelclientEntry_Object = MibTableRow
pmroadmCCfgLabelclientEntry = _PmroadmCCfgLabelclientEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 9, 3, 1, 1)
)
pmroadmCCfgLabelclientEntry.setIndexNames(
    (0, "EKINOPS-PmroadmC-MIB", "pmroadmCCfgLabelclientIndex"),
)
if mibBuilder.loadTexts:
    pmroadmCCfgLabelclientEntry.setStatus("current")


class _PmroadmCCfgLabelclientIndex_Type(Integer32):
    """Custom type pmroadmCCfgLabelclientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_PmroadmCCfgLabelclientIndex_Type.__name__ = "Integer32"
_PmroadmCCfgLabelclientIndex_Object = MibTableColumn
pmroadmCCfgLabelclientIndex = _PmroadmCCfgLabelclientIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 9, 3, 1, 1, 1),
    _PmroadmCCfgLabelclientIndex_Type()
)
pmroadmCCfgLabelclientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmroadmCCfgLabelclientIndex.setStatus("current")


class _PmroadmCCfgLabelclientPortn_Type(DisplayString):
    """Custom type pmroadmCCfgLabelclientPortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_PmroadmCCfgLabelclientPortn_Type.__name__ = "DisplayString"
_PmroadmCCfgLabelclientPortn_Object = MibTableColumn
pmroadmCCfgLabelclientPortn = _PmroadmCCfgLabelclientPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 9, 3, 1, 1, 3),
    _PmroadmCCfgLabelclientPortn_Type()
)
pmroadmCCfgLabelclientPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmroadmCCfgLabelclientPortn.setStatus("current")
_PmroadmCCfgLabellineTable_Object = MibTable
pmroadmCCfgLabellineTable = _PmroadmCCfgLabellineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 9, 3, 2)
)
if mibBuilder.loadTexts:
    pmroadmCCfgLabellineTable.setStatus("current")
_PmroadmCCfgLabellineEntry_Object = MibTableRow
pmroadmCCfgLabellineEntry = _PmroadmCCfgLabellineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 9, 3, 2, 1)
)
pmroadmCCfgLabellineEntry.setIndexNames(
    (0, "EKINOPS-PmroadmC-MIB", "pmroadmCCfgLabellineIndex"),
)
if mibBuilder.loadTexts:
    pmroadmCCfgLabellineEntry.setStatus("current")


class _PmroadmCCfgLabellineIndex_Type(Integer32):
    """Custom type pmroadmCCfgLabellineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_PmroadmCCfgLabellineIndex_Type.__name__ = "Integer32"
_PmroadmCCfgLabellineIndex_Object = MibTableColumn
pmroadmCCfgLabellineIndex = _PmroadmCCfgLabellineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 9, 3, 2, 1, 1),
    _PmroadmCCfgLabellineIndex_Type()
)
pmroadmCCfgLabellineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmroadmCCfgLabellineIndex.setStatus("current")


class _PmroadmCCfgLabellinePortn_Type(DisplayString):
    """Custom type pmroadmCCfgLabellinePortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_PmroadmCCfgLabellinePortn_Type.__name__ = "DisplayString"
_PmroadmCCfgLabellinePortn_Object = MibTableColumn
pmroadmCCfgLabellinePortn = _PmroadmCCfgLabellinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 9, 3, 2, 1, 3),
    _PmroadmCCfgLabellinePortn_Type()
)
pmroadmCCfgLabellinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmroadmCCfgLabellinePortn.setStatus("current")
_PmroadmCCfgWriteConfiguration_Type = EkiOnOff
_PmroadmCCfgWriteConfiguration_Object = MibScalar
pmroadmCCfgWriteConfiguration = _PmroadmCCfgWriteConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 9, 257),
    _PmroadmCCfgWriteConfiguration_Type()
)
pmroadmCCfgWriteConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmroadmCCfgWriteConfiguration.setStatus("current")
_PmroadmCtraps_ObjectIdentity = ObjectIdentity
pmroadmCtraps = _PmroadmCtraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 35, 10)
)


class _PmroadmCtrapBoardNumber_Type(Integer32):
    """Custom type pmroadmCtrapBoardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_PmroadmCtrapBoardNumber_Type.__name__ = "Integer32"
_PmroadmCtrapBoardNumber_Object = MibScalar
pmroadmCtrapBoardNumber = _PmroadmCtrapBoardNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 35, 10, 4),
    _PmroadmCtrapBoardNumber_Type()
)
pmroadmCtrapBoardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmroadmCtrapBoardNumber.setStatus("current")

# Managed Objects groups


# Notification objects

pmroadmCPowerTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 35, 10, 50)
)
pmroadmCPowerTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-PmroadmC-MIB", "pmroadmCAlmDefFuseB"),
        ("EKINOPS-PmroadmC-MIB", "pmroadmCAlmDefFuseA"),
        ("EKINOPS-PmroadmC-MIB", "pmroadmCtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmroadmCPowerTrapUrgentGoesOn.setStatus(
        "current"
    )

pmroadmCPowerTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 35, 10, 51)
)
pmroadmCPowerTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-PmroadmC-MIB", "pmroadmCAlmDefFuseB"),
        ("EKINOPS-PmroadmC-MIB", "pmroadmCAlmDefFuseA"),
        ("EKINOPS-PmroadmC-MIB", "pmroadmCtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmroadmCPowerTrapUrgentGoesOff.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EKINOPS-PmroadmC-MIB",
    **{"PmroadmCGrid": PmroadmCGrid,
       "PmroadmCPlanNumber": PmroadmCPlanNumber,
       "PmroadmCChannel": PmroadmCChannel,
       "modulepmroadmC": modulepmroadmC,
       "pmroadmCalarms": pmroadmCalarms,
       "pmroadmCAlmOther": pmroadmCAlmOther,
       "pmroadmCAlmOtherNurg": pmroadmCAlmOtherNurg,
       "pmroadmCAlmswitchDegrade": pmroadmCAlmswitchDegrade,
       "pmroadmCAlmSwitchTempHighDeg": pmroadmCAlmSwitchTempHighDeg,
       "pmroadmCAlmOtherUrg": pmroadmCAlmOtherUrg,
       "pmroadmCAlmswitchAlarms": pmroadmCAlmswitchAlarms,
       "pmroadmCAlmSwitchTempHighAla": pmroadmCAlmSwitchTempHighAla,
       "pmroadmCAlmmoduleStatus": pmroadmCAlmmoduleStatus,
       "pmroadmCAlmColdReset": pmroadmCAlmColdReset,
       "pmroadmCAlmWarmReset": pmroadmCAlmWarmReset,
       "pmroadmCAlmHotReset": pmroadmCAlmHotReset,
       "pmroadmCAlmSwitchNotReady": pmroadmCAlmSwitchNotReady,
       "pmroadmCAlmmoduleAlarms": pmroadmCAlmmoduleAlarms,
       "pmroadmCAlmModuleTempHighAla": pmroadmCAlmModuleTempHighAla,
       "pmroadmCAlmCaseTempHighAla": pmroadmCAlmCaseTempHighAla,
       "pmroadmCAlmmoduleDegrad": pmroadmCAlmmoduleDegrad,
       "pmroadmCAlmModuleTempHighDeg": pmroadmCAlmModuleTempHighDeg,
       "pmroadmCAlmCaseTempHighDeg": pmroadmCAlmCaseTempHighDeg,
       "pmroadmCAlmOtherCrit": pmroadmCAlmOtherCrit,
       "pmroadmCAlmsynthAlm0": pmroadmCAlmsynthAlm0,
       "pmroadmCAlmInServiceNotReady": pmroadmCAlmInServiceNotReady,
       "pmroadmCAlmModuleGlobFailure": pmroadmCAlmModuleGlobFailure,
       "pmroadmCAlmDefFuseA": pmroadmCAlmDefFuseA,
       "pmroadmCAlmDefFuseB": pmroadmCAlmDefFuseB,
       "pmroadmCAlmsynthAlm7": pmroadmCAlmsynthAlm7,
       "pmroadmCAlmInitNotCompl": pmroadmCAlmInitNotCompl,
       "pmroadmCAlmSwitchDegrade": pmroadmCAlmSwitchDegrade,
       "pmroadmCAlmSwitchAlm": pmroadmCAlmSwitchAlm,
       "pmroadmCmeasures": pmroadmCmeasures,
       "pmroadmCMesrOther": pmroadmCMesrOther,
       "pmroadmCMesrswitchTemp": pmroadmCMesrswitchTemp,
       "pmroadmCMesrmoduleTemp": pmroadmCMesrmoduleTemp,
       "pmroadmCMesrcaseTemp": pmroadmCMesrcaseTemp,
       "pmroadmCcontrolsWrite": pmroadmCcontrolsWrite,
       "pmroadmCCtrlOther": pmroadmCCtrlOther,
       "pmroadmCCtrlsynth0": pmroadmCCtrlsynth0,
       "pmroadmCCtrlConfLoad": pmroadmCCtrlConfLoad,
       "pmroadmCCtrlConfFlash": pmroadmCCtrlConfFlash,
       "pmroadmCCtrlConfClear": pmroadmCCtrlConfClear,
       "pmroadmCCtrlsynth4": pmroadmCCtrlsynth4,
       "pmroadmCCtrlCorrelatOn": pmroadmCCtrlCorrelatOn,
       "pmroadmCCtrlCorrelatOff": pmroadmCCtrlCorrelatOff,
       "pmroadmCCtrlswMgnt": pmroadmCCtrlswMgnt,
       "pmroadmCCtrlColdReset": pmroadmCCtrlColdReset,
       "pmroadmCCtrlWarmReset": pmroadmCCtrlWarmReset,
       "pmroadmCCtrlswitchCtrl": pmroadmCCtrlswitchCtrl,
       "pmroadmCCtrlAllChannelsHighLoss": pmroadmCCtrlAllChannelsHighLoss,
       "pmroadmCCtrlcraftSynch": pmroadmCCtrlcraftSynch,
       "pmroadmCCtrlledTest": pmroadmCCtrlledTest,
       "pmroadmCCtrlGreenLed": pmroadmCCtrlGreenLed,
       "pmroadmCCtrlRedLed": pmroadmCCtrlRedLed,
       "pmroadmCCtrlLedOff": pmroadmCCtrlLedOff,
       "pmroadmCCtrlwavePlanAssignmentsRefreshTable": pmroadmCCtrlwavePlanAssignmentsRefreshTable,
       "pmroadmCCtrlwavePlanAssignmentsRefreshEntry": pmroadmCCtrlwavePlanAssignmentsRefreshEntry,
       "pmroadmCCtrlwavePlanAssignmentsRefreshIndex": pmroadmCCtrlwavePlanAssignmentsRefreshIndex,
       "pmroadmCCtrlWaveStatusRefreshPortn": pmroadmCCtrlWaveStatusRefreshPortn,
       "pmroadmCCtrlWaveNarrowingRefreshPortn": pmroadmCCtrlWaveNarrowingRefreshPortn,
       "pmroadmCCtrlWaveCenterFrequencyRefreshPortn": pmroadmCCtrlWaveCenterFrequencyRefreshPortn,
       "pmroadmCCtrlWaveOOSRefreshPortn": pmroadmCCtrlWaveOOSRefreshPortn,
       "pmroadmCCtrlWaveAttenuationRefreshPortn": pmroadmCCtrlWaveAttenuationRefreshPortn,
       "pmroadmCCtrlWaveItuRefreshPortn": pmroadmCCtrlWaveItuRefreshPortn,
       "pmroadmCCtrlWaveDegreeRefreshPortn": pmroadmCCtrlWaveDegreeRefreshPortn,
       "pmroadmCCtrlUsageRefreshPortn": pmroadmCCtrlUsageRefreshPortn,
       "pmroadmCCtrlwavePlanAssignmentsWorkTable": pmroadmCCtrlwavePlanAssignmentsWorkTable,
       "pmroadmCCtrlwavePlanAssignmentsWorkEntry": pmroadmCCtrlwavePlanAssignmentsWorkEntry,
       "pmroadmCCtrlwavePlanAssignmentsWorkIndex": pmroadmCCtrlwavePlanAssignmentsWorkIndex,
       "pmroadmCCtrlWaveStatusWorkPortn": pmroadmCCtrlWaveStatusWorkPortn,
       "pmroadmCCtrlWaveNarrowingWorkPortn": pmroadmCCtrlWaveNarrowingWorkPortn,
       "pmroadmCCtrlWaveCenterFrequencyWorkPortn": pmroadmCCtrlWaveCenterFrequencyWorkPortn,
       "pmroadmCCtrlWaveOOSWorkPortn": pmroadmCCtrlWaveOOSWorkPortn,
       "pmroadmCCtrlWaveAttenuationWorkPortn": pmroadmCCtrlWaveAttenuationWorkPortn,
       "pmroadmCCtrlWaveItuWorkPortn": pmroadmCCtrlWaveItuWorkPortn,
       "pmroadmCCtrlWaveDegreeWorkPortn": pmroadmCCtrlWaveDegreeWorkPortn,
       "pmroadmCCtrlUsageWorkPortn": pmroadmCCtrlUsageWorkPortn,
       "pmroadmCCtrlbuildFromMgntPlan": pmroadmCCtrlbuildFromMgntPlan,
       "pmroadmCCtrlloadToWorkplan": pmroadmCCtrlloadToWorkplan,
       "pmroadmCCtrlsaveWorkPlanTo": pmroadmCCtrlsaveWorkPlanTo,
       "pmroadmCCtrlloadPlanToUse": pmroadmCCtrlloadPlanToUse,
       "pmroadmCCtrlrefreshWithPlan": pmroadmCCtrlrefreshWithPlan,
       "pmroadmCCtrlsavePlanToFile": pmroadmCCtrlsavePlanToFile,
       "pmroadmCCtrlloadPlanFromFile": pmroadmCCtrlloadPlanFromFile,
       "pmroadmCCtrlExpress": pmroadmCCtrlExpress,
       "pmroadmCCtrlexpTxCommonAttDegTable": pmroadmCCtrlexpTxCommonAttDegTable,
       "pmroadmCCtrlexpTxCommonAttDegEntry": pmroadmCCtrlexpTxCommonAttDegEntry,
       "pmroadmCCtrlexpTxCommonAttDegIndex": pmroadmCCtrlexpTxCommonAttDegIndex,
       "pmroadmCCtrlexpTxCommonAttDegPortn": pmroadmCCtrlexpTxCommonAttDegPortn,
       "pmroadmCCtrlexpRxCommonAttDegTable": pmroadmCCtrlexpRxCommonAttDegTable,
       "pmroadmCCtrlexpRxCommonAttDegEntry": pmroadmCCtrlexpRxCommonAttDegEntry,
       "pmroadmCCtrlexpRxCommonAttDegIndex": pmroadmCCtrlexpRxCommonAttDegIndex,
       "pmroadmCCtrlexpRxCommonAttDegPortn": pmroadmCCtrlexpRxCommonAttDegPortn,
       "pmroadmCCtrlapplyPlanUpdate": pmroadmCCtrlapplyPlanUpdate,
       "pmroadmCCtrlApply": pmroadmCCtrlApply,
       "pmroadmCCtrlLine": pmroadmCCtrlLine,
       "pmroadmCri": pmroadmCri,
       "pmroadmCriTable": pmroadmCriTable,
       "pmroadmCRinvPortTable": pmroadmCRinvPortTable,
       "pmroadmCRinvPortEntry": pmroadmCRinvPortEntry,
       "pmroadmCRinvPortIndex": pmroadmCRinvPortIndex,
       "pmroadmCRinvPort": pmroadmCRinvPort,
       "pmroadmCRinvLineTable": pmroadmCRinvLineTable,
       "pmroadmCRinvLineEntry": pmroadmCRinvLineEntry,
       "pmroadmCRinvLineIndex": pmroadmCRinvLineIndex,
       "pmroadmCRinvxfpLine": pmroadmCRinvxfpLine,
       "pmroadmCRinvReloadInventory": pmroadmCRinvReloadInventory,
       "pmroadmCRinvHwPlatform": pmroadmCRinvHwPlatform,
       "pmroadmCRinvSwPlatform": pmroadmCRinvSwPlatform,
       "pmroadmCConfig": pmroadmCConfig,
       "pmroadmCCfgLsd": pmroadmCCfgLsd,
       "pmroadmCtableclientLsd": pmroadmCtableclientLsd,
       "pmroadmCCfgStartup": pmroadmCCfgStartup,
       "pmroadmCCfgClientStartupTable": pmroadmCCfgClientStartupTable,
       "pmroadmCCfgClientStartupEntry": pmroadmCCfgClientStartupEntry,
       "pmroadmCCfgClientStartupIndex": pmroadmCCfgClientStartupIndex,
       "pmroadmCCfgLineaRxCommonAttDegPortn": pmroadmCCfgLineaRxCommonAttDegPortn,
       "pmroadmCtablelineStartup": pmroadmCtablelineStartup,
       "pmroadmCtableclientsRoadm": pmroadmCtableclientsRoadm,
       "pmroadmCtablelinesRoadm": pmroadmCtablelinesRoadm,
       "pmroadmCCfgexpGridCurrent": pmroadmCCfgexpGridCurrent,
       "pmroadmCtableother": pmroadmCtableother,
       "pmroadmCCfgcomponentType": pmroadmCCfgcomponentType,
       "pmroadmCCfgmiscellaneous": pmroadmCCfgmiscellaneous,
       "pmroadmCCfgfirstChannel": pmroadmCCfgfirstChannel,
       "pmroadmCCfglastChannel": pmroadmCCfglastChannel,
       "pmroadmCCfggrid": pmroadmCCfggrid,
       "pmroadmCCfgLabels": pmroadmCCfgLabels,
       "pmroadmCCfgLabelclientTable": pmroadmCCfgLabelclientTable,
       "pmroadmCCfgLabelclientEntry": pmroadmCCfgLabelclientEntry,
       "pmroadmCCfgLabelclientIndex": pmroadmCCfgLabelclientIndex,
       "pmroadmCCfgLabelclientPortn": pmroadmCCfgLabelclientPortn,
       "pmroadmCCfgLabellineTable": pmroadmCCfgLabellineTable,
       "pmroadmCCfgLabellineEntry": pmroadmCCfgLabellineEntry,
       "pmroadmCCfgLabellineIndex": pmroadmCCfgLabellineIndex,
       "pmroadmCCfgLabellinePortn": pmroadmCCfgLabellinePortn,
       "pmroadmCCfgWriteConfiguration": pmroadmCCfgWriteConfiguration,
       "pmroadmCtraps": pmroadmCtraps,
       "pmroadmCtrapBoardNumber": pmroadmCtrapBoardNumber,
       "pmroadmCPowerTrapUrgentGoesOn": pmroadmCPowerTrapUrgentGoesOn,
       "pmroadmCPowerTrapUrgentGoesOff": pmroadmCPowerTrapUrgentGoesOff}
)
