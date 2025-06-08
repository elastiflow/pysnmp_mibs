# SNMP MIB module (EKINOPS-Trfan-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ekinops_20044/EKINOPS-Trfan-MIB.mib
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
 ekinops) = mibBuilder.importSymbols(
    "EKINOPS-MIB",
    "EkiApiState",
    "EkiMeasureType",
    "EkiMode",
    "EkiOnOff",
    "EkiProtocol",
    "EkiState",
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

moduletrfan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 45)
)
if mibBuilder.loadTexts:
    moduletrfan.setRevisions(
        ("2010-01-04 00:00",
         "2010-10-28 00:00",
         "2012-07-04 00:00",
         "2013-09-02 00:00",
         "2014-03-26 00:00",
         "2014-11-25 00:00",
         "2016-05-23 00:00",
         "2017-06-09 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Trfanalarms_ObjectIdentity = ObjectIdentity
trfanalarms = _Trfanalarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 45, 2)
)
_TrfanAlmOther_ObjectIdentity = ObjectIdentity
trfanAlmOther = _TrfanAlmOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 45, 2, 1)
)
_TrfanAlmOtherNurg_ObjectIdentity = ObjectIdentity
trfanAlmOtherNurg = _TrfanAlmOtherNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 45, 2, 1, 1)
)
_TrfanAlmsynthAlm2_ObjectIdentity = ObjectIdentity
trfanAlmsynthAlm2 = _TrfanAlmsynthAlm2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 45, 2, 1, 1, 2)
)
_TrfanAlmConfTableSave_Type = EkiOnOff
_TrfanAlmConfTableSave_Object = MibScalar
trfanAlmConfTableSave = _TrfanAlmConfTableSave_Object(
    (1, 3, 6, 1, 4, 1, 20044, 45, 2, 1, 1, 2, 1),
    _TrfanAlmConfTableSave_Type()
)
trfanAlmConfTableSave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trfanAlmConfTableSave.setStatus("current")
_TrfanAlmInvUpload_Type = EkiOnOff
_TrfanAlmInvUpload_Object = MibScalar
trfanAlmInvUpload = _TrfanAlmInvUpload_Object(
    (1, 3, 6, 1, 4, 1, 20044, 45, 2, 1, 1, 2, 2),
    _TrfanAlmInvUpload_Type()
)
trfanAlmInvUpload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trfanAlmInvUpload.setStatus("current")
_TrfanAlmConfTableLoad_Type = EkiOnOff
_TrfanAlmConfTableLoad_Object = MibScalar
trfanAlmConfTableLoad = _TrfanAlmConfTableLoad_Object(
    (1, 3, 6, 1, 4, 1, 20044, 45, 2, 1, 1, 2, 3),
    _TrfanAlmConfTableLoad_Type()
)
trfanAlmConfTableLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trfanAlmConfTableLoad.setStatus("current")
_TrfanAlmCorrelatOff_Type = EkiOnOff
_TrfanAlmCorrelatOff_Object = MibScalar
trfanAlmCorrelatOff = _TrfanAlmCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 45, 2, 1, 1, 2, 4),
    _TrfanAlmCorrelatOff_Type()
)
trfanAlmCorrelatOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trfanAlmCorrelatOff.setStatus("current")
_TrfanAlmOtherUrg_ObjectIdentity = ObjectIdentity
trfanAlmOtherUrg = _TrfanAlmOtherUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 45, 2, 1, 2)
)
_TrfanAlmfilterAlm_ObjectIdentity = ObjectIdentity
trfanAlmfilterAlm = _TrfanAlmfilterAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 45, 2, 1, 2, 16)
)
_TrfanAlmFilterNotPresent_Type = EkiOnOff
_TrfanAlmFilterNotPresent_Object = MibScalar
trfanAlmFilterNotPresent = _TrfanAlmFilterNotPresent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 45, 2, 1, 2, 16, 15),
    _TrfanAlmFilterNotPresent_Type()
)
trfanAlmFilterNotPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trfanAlmFilterNotPresent.setStatus("current")
_TrfanAlmfansMgnt_ObjectIdentity = ObjectIdentity
trfanAlmfansMgnt = _TrfanAlmfansMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 45, 2, 1, 2, 20)
)
_TrfanAlmFan1Fail_Type = EkiOnOff
_TrfanAlmFan1Fail_Object = MibScalar
trfanAlmFan1Fail = _TrfanAlmFan1Fail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 45, 2, 1, 2, 20, 2),
    _TrfanAlmFan1Fail_Type()
)
trfanAlmFan1Fail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trfanAlmFan1Fail.setStatus("current")
_TrfanAlmFan2Fail_Type = EkiOnOff
_TrfanAlmFan2Fail_Object = MibScalar
trfanAlmFan2Fail = _TrfanAlmFan2Fail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 45, 2, 1, 2, 20, 3),
    _TrfanAlmFan2Fail_Type()
)
trfanAlmFan2Fail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trfanAlmFan2Fail.setStatus("current")
_TrfanAlmFan3Fail_Type = EkiOnOff
_TrfanAlmFan3Fail_Object = MibScalar
trfanAlmFan3Fail = _TrfanAlmFan3Fail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 45, 2, 1, 2, 20, 4),
    _TrfanAlmFan3Fail_Type()
)
trfanAlmFan3Fail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trfanAlmFan3Fail.setStatus("current")
_TrfanAlmFan4Fail_Type = EkiOnOff
_TrfanAlmFan4Fail_Object = MibScalar
trfanAlmFan4Fail = _TrfanAlmFan4Fail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 45, 2, 1, 2, 20, 5),
    _TrfanAlmFan4Fail_Type()
)
trfanAlmFan4Fail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trfanAlmFan4Fail.setStatus("current")
_TrfanAlmFan5Fail_Type = EkiOnOff
_TrfanAlmFan5Fail_Object = MibScalar
trfanAlmFan5Fail = _TrfanAlmFan5Fail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 45, 2, 1, 2, 20, 6),
    _TrfanAlmFan5Fail_Type()
)
trfanAlmFan5Fail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trfanAlmFan5Fail.setStatus("current")
_TrfanAlmFan6Fail_Type = EkiOnOff
_TrfanAlmFan6Fail_Object = MibScalar
trfanAlmFan6Fail = _TrfanAlmFan6Fail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 45, 2, 1, 2, 20, 7),
    _TrfanAlmFan6Fail_Type()
)
trfanAlmFan6Fail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trfanAlmFan6Fail.setStatus("current")
_TrfanAlmFansOff_Type = EkiOnOff
_TrfanAlmFansOff_Object = MibScalar
trfanAlmFansOff = _TrfanAlmFansOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 45, 2, 1, 2, 20, 13),
    _TrfanAlmFansOff_Type()
)
trfanAlmFansOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trfanAlmFansOff.setStatus("current")
_TrfanAlmFanLowSpeed_Type = EkiOnOff
_TrfanAlmFanLowSpeed_Object = MibScalar
trfanAlmFanLowSpeed = _TrfanAlmFanLowSpeed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 45, 2, 1, 2, 20, 14),
    _TrfanAlmFanLowSpeed_Type()
)
trfanAlmFanLowSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trfanAlmFanLowSpeed.setStatus("current")
_TrfanAlmpwrMgnt_ObjectIdentity = ObjectIdentity
trfanAlmpwrMgnt = _TrfanAlmpwrMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 45, 2, 1, 2, 24)
)
_TrfanAlmPwr12v1Fail_Type = EkiOnOff
_TrfanAlmPwr12v1Fail_Object = MibScalar
trfanAlmPwr12v1Fail = _TrfanAlmPwr12v1Fail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 45, 2, 1, 2, 24, 13),
    _TrfanAlmPwr12v1Fail_Type()
)
trfanAlmPwr12v1Fail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trfanAlmPwr12v1Fail.setStatus("current")
_TrfanAlmPwr12v2Fail_Type = EkiOnOff
_TrfanAlmPwr12v2Fail_Object = MibScalar
trfanAlmPwr12v2Fail = _TrfanAlmPwr12v2Fail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 45, 2, 1, 2, 24, 14),
    _TrfanAlmPwr12v2Fail_Type()
)
trfanAlmPwr12v2Fail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trfanAlmPwr12v2Fail.setStatus("current")
_TrfanAlmmodInitFailLevel2_ObjectIdentity = ObjectIdentity
trfanAlmmodInitFailLevel2 = _TrfanAlmmodInitFailLevel2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 45, 2, 1, 2, 70)
)
_TrfanAlmRegReadFail_Type = EkiOnOff
_TrfanAlmRegReadFail_Object = MibScalar
trfanAlmRegReadFail = _TrfanAlmRegReadFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 45, 2, 1, 2, 70, 1),
    _TrfanAlmRegReadFail_Type()
)
trfanAlmRegReadFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trfanAlmRegReadFail.setStatus("current")
_TrfanAlmResetHwInitFail_Type = EkiOnOff
_TrfanAlmResetHwInitFail_Object = MibScalar
trfanAlmResetHwInitFail = _TrfanAlmResetHwInitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 45, 2, 1, 2, 70, 2),
    _TrfanAlmResetHwInitFail_Type()
)
trfanAlmResetHwInitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trfanAlmResetHwInitFail.setStatus("current")
_TrfanAlmConfReadFail_Type = EkiOnOff
_TrfanAlmConfReadFail_Object = MibScalar
trfanAlmConfReadFail = _TrfanAlmConfReadFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 45, 2, 1, 2, 70, 3),
    _TrfanAlmConfReadFail_Type()
)
trfanAlmConfReadFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trfanAlmConfReadFail.setStatus("current")
_TrfanAlmInvReadFail_Type = EkiOnOff
_TrfanAlmInvReadFail_Object = MibScalar
trfanAlmInvReadFail = _TrfanAlmInvReadFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 45, 2, 1, 2, 70, 4),
    _TrfanAlmInvReadFail_Type()
)
trfanAlmInvReadFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trfanAlmInvReadFail.setStatus("current")
_TrfanAlmOtherCrit_ObjectIdentity = ObjectIdentity
trfanAlmOtherCrit = _TrfanAlmOtherCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 45, 2, 1, 3)
)
_TrfanAlmsynthAlm0_ObjectIdentity = ObjectIdentity
trfanAlmsynthAlm0 = _TrfanAlmsynthAlm0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 45, 2, 1, 3, 0)
)
_TrfanAlmModuleGlobFailure_Type = EkiOnOff
_TrfanAlmModuleGlobFailure_Object = MibScalar
trfanAlmModuleGlobFailure = _TrfanAlmModuleGlobFailure_Object(
    (1, 3, 6, 1, 4, 1, 20044, 45, 2, 1, 3, 0, 9),
    _TrfanAlmModuleGlobFailure_Type()
)
trfanAlmModuleGlobFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trfanAlmModuleGlobFailure.setStatus("current")
_TrfanAlmDefPowerA_Type = EkiOnOff
_TrfanAlmDefPowerA_Object = MibScalar
trfanAlmDefPowerA = _TrfanAlmDefPowerA_Object(
    (1, 3, 6, 1, 4, 1, 20044, 45, 2, 1, 3, 0, 11),
    _TrfanAlmDefPowerA_Type()
)
trfanAlmDefPowerA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trfanAlmDefPowerA.setStatus("current")
_TrfanAlmDefPowerB_Type = EkiOnOff
_TrfanAlmDefPowerB_Object = MibScalar
trfanAlmDefPowerB = _TrfanAlmDefPowerB_Object(
    (1, 3, 6, 1, 4, 1, 20044, 45, 2, 1, 3, 0, 12),
    _TrfanAlmDefPowerB_Type()
)
trfanAlmDefPowerB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trfanAlmDefPowerB.setStatus("current")
_TrfanAlmAcknowledge_Type = EkiOnOff
_TrfanAlmAcknowledge_Object = MibScalar
trfanAlmAcknowledge = _TrfanAlmAcknowledge_Object(
    (1, 3, 6, 1, 4, 1, 20044, 45, 2, 1, 3, 0, 13),
    _TrfanAlmAcknowledge_Type()
)
trfanAlmAcknowledge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trfanAlmAcknowledge.setStatus("current")
_TrfanAlmDefFuse_Type = EkiOnOff
_TrfanAlmDefFuse_Object = MibScalar
trfanAlmDefFuse = _TrfanAlmDefFuse_Object(
    (1, 3, 6, 1, 4, 1, 20044, 45, 2, 1, 3, 0, 15),
    _TrfanAlmDefFuse_Type()
)
trfanAlmDefFuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trfanAlmDefFuse.setStatus("current")
_TrfanAlmsynthAlm1_ObjectIdentity = ObjectIdentity
trfanAlmsynthAlm1 = _TrfanAlmsynthAlm1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 45, 2, 1, 3, 1)
)
_TrfanAlmFansFailure_Type = EkiOnOff
_TrfanAlmFansFailure_Object = MibScalar
trfanAlmFansFailure = _TrfanAlmFansFailure_Object(
    (1, 3, 6, 1, 4, 1, 20044, 45, 2, 1, 3, 1, 10),
    _TrfanAlmFansFailure_Type()
)
trfanAlmFansFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trfanAlmFansFailure.setStatus("current")
_Trfanmeasures_ObjectIdentity = ObjectIdentity
trfanmeasures = _Trfanmeasures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 45, 3)
)
_TrfanMesrOther_ObjectIdentity = ObjectIdentity
trfanMesrOther = _TrfanMesrOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 45, 3, 1)
)


class _TrfanMesrvoltMeas12v1_Type(Unsigned32):
    """Custom type trfanMesrvoltMeas12v1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TrfanMesrvoltMeas12v1_Type.__name__ = "Unsigned32"
_TrfanMesrvoltMeas12v1_Object = MibScalar
trfanMesrvoltMeas12v1 = _TrfanMesrvoltMeas12v1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 45, 3, 1, 16),
    _TrfanMesrvoltMeas12v1_Type()
)
trfanMesrvoltMeas12v1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trfanMesrvoltMeas12v1.setStatus("current")


class _TrfanMesrvoltMeas12v2_Type(Unsigned32):
    """Custom type trfanMesrvoltMeas12v2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TrfanMesrvoltMeas12v2_Type.__name__ = "Unsigned32"
_TrfanMesrvoltMeas12v2_Object = MibScalar
trfanMesrvoltMeas12v2 = _TrfanMesrvoltMeas12v2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 45, 3, 1, 17),
    _TrfanMesrvoltMeas12v2_Type()
)
trfanMesrvoltMeas12v2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trfanMesrvoltMeas12v2.setStatus("current")


class _TrfanMesrtempChassis_Type(Unsigned32):
    """Custom type trfanMesrtempChassis based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TrfanMesrtempChassis_Type.__name__ = "Unsigned32"
_TrfanMesrtempChassis_Object = MibScalar
trfanMesrtempChassis = _TrfanMesrtempChassis_Object(
    (1, 3, 6, 1, 4, 1, 20044, 45, 3, 1, 64),
    _TrfanMesrtempChassis_Type()
)
trfanMesrtempChassis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trfanMesrtempChassis.setStatus("current")
_TrfancontrolsWrite_ObjectIdentity = ObjectIdentity
trfancontrolsWrite = _TrfancontrolsWrite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 45, 6)
)
_TrfanCtrlOther_ObjectIdentity = ObjectIdentity
trfanCtrlOther = _TrfanCtrlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 45, 6, 1)
)
_TrfanCtrlsynth0_ObjectIdentity = ObjectIdentity
trfanCtrlsynth0 = _TrfanCtrlsynth0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 45, 6, 1, 0)
)
_TrfanCtrlConfLoad_Type = EkiOnOff
_TrfanCtrlConfLoad_Object = MibScalar
trfanCtrlConfLoad = _TrfanCtrlConfLoad_Object(
    (1, 3, 6, 1, 4, 1, 20044, 45, 6, 1, 0, 1),
    _TrfanCtrlConfLoad_Type()
)
trfanCtrlConfLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trfanCtrlConfLoad.setStatus("current")
_TrfanCtrlConfFlash_Type = EkiOnOff
_TrfanCtrlConfFlash_Object = MibScalar
trfanCtrlConfFlash = _TrfanCtrlConfFlash_Object(
    (1, 3, 6, 1, 4, 1, 20044, 45, 6, 1, 0, 9),
    _TrfanCtrlConfFlash_Type()
)
trfanCtrlConfFlash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trfanCtrlConfFlash.setStatus("current")
_TrfanCtrlConfClear_Type = EkiOnOff
_TrfanCtrlConfClear_Object = MibScalar
trfanCtrlConfClear = _TrfanCtrlConfClear_Object(
    (1, 3, 6, 1, 4, 1, 20044, 45, 6, 1, 0, 13),
    _TrfanCtrlConfClear_Type()
)
trfanCtrlConfClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trfanCtrlConfClear.setStatus("current")
_TrfanCtrlsynth4_ObjectIdentity = ObjectIdentity
trfanCtrlsynth4 = _TrfanCtrlsynth4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 45, 6, 1, 4)
)
_TrfanCtrlCorrelatOn_Type = EkiOnOff
_TrfanCtrlCorrelatOn_Object = MibScalar
trfanCtrlCorrelatOn = _TrfanCtrlCorrelatOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 45, 6, 1, 4, 1),
    _TrfanCtrlCorrelatOn_Type()
)
trfanCtrlCorrelatOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trfanCtrlCorrelatOn.setStatus("current")
_TrfanCtrlCorrelatOff_Type = EkiOnOff
_TrfanCtrlCorrelatOff_Object = MibScalar
trfanCtrlCorrelatOff = _TrfanCtrlCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 45, 6, 1, 4, 2),
    _TrfanCtrlCorrelatOff_Type()
)
trfanCtrlCorrelatOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trfanCtrlCorrelatOff.setStatus("current")
_TrfanCtrlswMgnt_ObjectIdentity = ObjectIdentity
trfanCtrlswMgnt = _TrfanCtrlswMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 45, 6, 1, 5)
)
_TrfanCtrlColdReset_Type = EkiOnOff
_TrfanCtrlColdReset_Object = MibScalar
trfanCtrlColdReset = _TrfanCtrlColdReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 45, 6, 1, 5, 2),
    _TrfanCtrlColdReset_Type()
)
trfanCtrlColdReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trfanCtrlColdReset.setStatus("current")
_TrfanCtrlWarmReset_Type = EkiOnOff
_TrfanCtrlWarmReset_Object = MibScalar
trfanCtrlWarmReset = _TrfanCtrlWarmReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 45, 6, 1, 5, 3),
    _TrfanCtrlWarmReset_Type()
)
trfanCtrlWarmReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trfanCtrlWarmReset.setStatus("current")
_TrfanCtrlledTest_ObjectIdentity = ObjectIdentity
trfanCtrlledTest = _TrfanCtrlledTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 45, 6, 1, 64)
)
_TrfanCtrlGreenLed_Type = EkiOnOff
_TrfanCtrlGreenLed_Object = MibScalar
trfanCtrlGreenLed = _TrfanCtrlGreenLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 45, 6, 1, 64, 1),
    _TrfanCtrlGreenLed_Type()
)
trfanCtrlGreenLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trfanCtrlGreenLed.setStatus("current")
_TrfanCtrlRedLed_Type = EkiOnOff
_TrfanCtrlRedLed_Object = MibScalar
trfanCtrlRedLed = _TrfanCtrlRedLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 45, 6, 1, 64, 2),
    _TrfanCtrlRedLed_Type()
)
trfanCtrlRedLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trfanCtrlRedLed.setStatus("current")
_TrfanCtrlLedOff_Type = EkiOnOff
_TrfanCtrlLedOff_Object = MibScalar
trfanCtrlLedOff = _TrfanCtrlLedOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 45, 6, 1, 64, 3),
    _TrfanCtrlLedOff_Type()
)
trfanCtrlLedOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trfanCtrlLedOff.setStatus("current")
_TrfanCtrlacknowledgeActiv_ObjectIdentity = ObjectIdentity
trfanCtrlacknowledgeActiv = _TrfanCtrlacknowledgeActiv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 45, 6, 1, 65)
)
_TrfanCtrlAckActiv_Type = EkiOnOff
_TrfanCtrlAckActiv_Object = MibScalar
trfanCtrlAckActiv = _TrfanCtrlAckActiv_Object(
    (1, 3, 6, 1, 4, 1, 20044, 45, 6, 1, 65, 1),
    _TrfanCtrlAckActiv_Type()
)
trfanCtrlAckActiv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trfanCtrlAckActiv.setStatus("current")
_Trfanri_ObjectIdentity = ObjectIdentity
trfanri = _Trfanri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 45, 7)
)
_TrfanriTable_ObjectIdentity = ObjectIdentity
trfanriTable = _TrfanriTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 45, 7, 1)
)
_TrfanRinvReloadInventory_Type = EkiOnOff
_TrfanRinvReloadInventory_Object = MibScalar
trfanRinvReloadInventory = _TrfanRinvReloadInventory_Object(
    (1, 3, 6, 1, 4, 1, 20044, 45, 7, 2),
    _TrfanRinvReloadInventory_Type()
)
trfanRinvReloadInventory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trfanRinvReloadInventory.setStatus("current")
_TrfanRinvHwPlatform_Type = DisplayString
_TrfanRinvHwPlatform_Object = MibScalar
trfanRinvHwPlatform = _TrfanRinvHwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 45, 7, 3),
    _TrfanRinvHwPlatform_Type()
)
trfanRinvHwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trfanRinvHwPlatform.setStatus("current")
_TrfanRinvModulePlatform_Type = DisplayString
_TrfanRinvModulePlatform_Object = MibScalar
trfanRinvModulePlatform = _TrfanRinvModulePlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 45, 7, 4),
    _TrfanRinvModulePlatform_Type()
)
trfanRinvModulePlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trfanRinvModulePlatform.setStatus("current")
_TrfanRinvSwPlatform_Type = DisplayString
_TrfanRinvSwPlatform_Object = MibScalar
trfanRinvSwPlatform = _TrfanRinvSwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 45, 7, 5),
    _TrfanRinvSwPlatform_Type()
)
trfanRinvSwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trfanRinvSwPlatform.setStatus("current")
_TrfanConfig_ObjectIdentity = ObjectIdentity
trfanConfig = _TrfanConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 45, 9)
)
_TrfanCfgLsd_ObjectIdentity = ObjectIdentity
trfanCfgLsd = _TrfanCfgLsd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 45, 9, 1)
)
_TrfanCfgStartUp_ObjectIdentity = ObjectIdentity
trfanCfgStartUp = _TrfanCfgStartUp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 45, 9, 2)
)
_Trfantableother_ObjectIdentity = ObjectIdentity
trfantableother = _Trfantableother_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 45, 9, 2, 1)
)


class _TrfanCfglowspeedThresh_Type(Unsigned32):
    """Custom type trfanCfglowspeedThresh based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_TrfanCfglowspeedThresh_Type.__name__ = "Unsigned32"
_TrfanCfglowspeedThresh_Object = MibScalar
trfanCfglowspeedThresh = _TrfanCfglowspeedThresh_Object(
    (1, 3, 6, 1, 4, 1, 20044, 45, 9, 2, 1, 2),
    _TrfanCfglowspeedThresh_Type()
)
trfanCfglowspeedThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trfanCfglowspeedThresh.setStatus("current")


class _TrfanCfghighspeedThresh_Type(Unsigned32):
    """Custom type trfanCfghighspeedThresh based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_TrfanCfghighspeedThresh_Type.__name__ = "Unsigned32"
_TrfanCfghighspeedThresh_Object = MibScalar
trfanCfghighspeedThresh = _TrfanCfghighspeedThresh_Object(
    (1, 3, 6, 1, 4, 1, 20044, 45, 9, 2, 1, 3),
    _TrfanCfghighspeedThresh_Type()
)
trfanCfghighspeedThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trfanCfghighspeedThresh.setStatus("current")


class _TrfanCfgtrfanMgnt_Type(Unsigned32):
    """Custom type trfanCfgtrfanMgnt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_TrfanCfgtrfanMgnt_Type.__name__ = "Unsigned32"
_TrfanCfgtrfanMgnt_Object = MibScalar
trfanCfgtrfanMgnt = _TrfanCfgtrfanMgnt_Object(
    (1, 3, 6, 1, 4, 1, 20044, 45, 9, 2, 1, 10),
    _TrfanCfgtrfanMgnt_Type()
)
trfanCfgtrfanMgnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trfanCfgtrfanMgnt.setStatus("current")
_TrfanCfgLabels_ObjectIdentity = ObjectIdentity
trfanCfgLabels = _TrfanCfgLabels_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 45, 9, 3)
)
_TrfanCfgWriteConfiguration_Type = EkiOnOff
_TrfanCfgWriteConfiguration_Object = MibScalar
trfanCfgWriteConfiguration = _TrfanCfgWriteConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 20044, 45, 9, 257),
    _TrfanCfgWriteConfiguration_Type()
)
trfanCfgWriteConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trfanCfgWriteConfiguration.setStatus("current")
_Trfantraps_ObjectIdentity = ObjectIdentity
trfantraps = _Trfantraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 45, 10)
)


class _TrfantrapBoardNumber_Type(Integer32):
    """Custom type trfantrapBoardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_TrfantrapBoardNumber_Type.__name__ = "Integer32"
_TrfantrapBoardNumber_Object = MibScalar
trfantrapBoardNumber = _TrfantrapBoardNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 45, 10, 2),
    _TrfantrapBoardNumber_Type()
)
trfantrapBoardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trfantrapBoardNumber.setStatus("current")

# Managed Objects groups


# Notification objects

trfanPowerTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 45, 10, 32)
)
trfanPowerTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Trfan-MIB", "trfanAlmDefPowerA"),
        ("EKINOPS-Trfan-MIB", "trfanAlmDefPowerB"),
        ("EKINOPS-Trfan-MIB", "trfanAlmPwr12v1Fail"),
        ("EKINOPS-Trfan-MIB", "trfanAlmPwr12v2Fail"))
)
if mibBuilder.loadTexts:
    trfanPowerTrapUrgentGoesOn.setStatus(
        "current"
    )

trfanPowerTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 45, 10, 33)
)
trfanPowerTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Trfan-MIB", "trfanAlmDefPowerA"),
        ("EKINOPS-Trfan-MIB", "trfanAlmDefPowerB"),
        ("EKINOPS-Trfan-MIB", "trfanAlmPwr12v1Fail"),
        ("EKINOPS-Trfan-MIB", "trfanAlmPwr12v2Fail"))
)
if mibBuilder.loadTexts:
    trfanPowerTrapUrgentGoesOff.setStatus(
        "current"
    )

trfanPowerTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 45, 10, 34)
)
trfanPowerTrapCritGoesOn.setObjects(
    ("EKINOPS-Trfan-MIB", "trfanAlmDefFuse")
)
if mibBuilder.loadTexts:
    trfanPowerTrapCritGoesOn.setStatus(
        "current"
    )

trfanPowerTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 45, 10, 35)
)
trfanPowerTrapCritGoesOff.setObjects(
    ("EKINOPS-Trfan-MIB", "trfanAlmDefFuse")
)
if mibBuilder.loadTexts:
    trfanPowerTrapCritGoesOff.setStatus(
        "current"
    )

trfanFanTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 45, 10, 44)
)
trfanFanTrapCritGoesOn.setObjects(
    ("EKINOPS-Trfan-MIB", "trfanAlmFansFailure")
)
if mibBuilder.loadTexts:
    trfanFanTrapCritGoesOn.setStatus(
        "current"
    )

trfanFanTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 45, 10, 45)
)
trfanFanTrapCritGoesOff.setObjects(
    ("EKINOPS-Trfan-MIB", "trfanAlmFansFailure")
)
if mibBuilder.loadTexts:
    trfanFanTrapCritGoesOff.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EKINOPS-Trfan-MIB",
    **{"moduletrfan": moduletrfan,
       "trfanalarms": trfanalarms,
       "trfanAlmOther": trfanAlmOther,
       "trfanAlmOtherNurg": trfanAlmOtherNurg,
       "trfanAlmsynthAlm2": trfanAlmsynthAlm2,
       "trfanAlmConfTableSave": trfanAlmConfTableSave,
       "trfanAlmInvUpload": trfanAlmInvUpload,
       "trfanAlmConfTableLoad": trfanAlmConfTableLoad,
       "trfanAlmCorrelatOff": trfanAlmCorrelatOff,
       "trfanAlmOtherUrg": trfanAlmOtherUrg,
       "trfanAlmfilterAlm": trfanAlmfilterAlm,
       "trfanAlmFilterNotPresent": trfanAlmFilterNotPresent,
       "trfanAlmfansMgnt": trfanAlmfansMgnt,
       "trfanAlmFan1Fail": trfanAlmFan1Fail,
       "trfanAlmFan2Fail": trfanAlmFan2Fail,
       "trfanAlmFan3Fail": trfanAlmFan3Fail,
       "trfanAlmFan4Fail": trfanAlmFan4Fail,
       "trfanAlmFan5Fail": trfanAlmFan5Fail,
       "trfanAlmFan6Fail": trfanAlmFan6Fail,
       "trfanAlmFansOff": trfanAlmFansOff,
       "trfanAlmFanLowSpeed": trfanAlmFanLowSpeed,
       "trfanAlmpwrMgnt": trfanAlmpwrMgnt,
       "trfanAlmPwr12v1Fail": trfanAlmPwr12v1Fail,
       "trfanAlmPwr12v2Fail": trfanAlmPwr12v2Fail,
       "trfanAlmmodInitFailLevel2": trfanAlmmodInitFailLevel2,
       "trfanAlmRegReadFail": trfanAlmRegReadFail,
       "trfanAlmResetHwInitFail": trfanAlmResetHwInitFail,
       "trfanAlmConfReadFail": trfanAlmConfReadFail,
       "trfanAlmInvReadFail": trfanAlmInvReadFail,
       "trfanAlmOtherCrit": trfanAlmOtherCrit,
       "trfanAlmsynthAlm0": trfanAlmsynthAlm0,
       "trfanAlmModuleGlobFailure": trfanAlmModuleGlobFailure,
       "trfanAlmDefPowerA": trfanAlmDefPowerA,
       "trfanAlmDefPowerB": trfanAlmDefPowerB,
       "trfanAlmAcknowledge": trfanAlmAcknowledge,
       "trfanAlmDefFuse": trfanAlmDefFuse,
       "trfanAlmsynthAlm1": trfanAlmsynthAlm1,
       "trfanAlmFansFailure": trfanAlmFansFailure,
       "trfanmeasures": trfanmeasures,
       "trfanMesrOther": trfanMesrOther,
       "trfanMesrvoltMeas12v1": trfanMesrvoltMeas12v1,
       "trfanMesrvoltMeas12v2": trfanMesrvoltMeas12v2,
       "trfanMesrtempChassis": trfanMesrtempChassis,
       "trfancontrolsWrite": trfancontrolsWrite,
       "trfanCtrlOther": trfanCtrlOther,
       "trfanCtrlsynth0": trfanCtrlsynth0,
       "trfanCtrlConfLoad": trfanCtrlConfLoad,
       "trfanCtrlConfFlash": trfanCtrlConfFlash,
       "trfanCtrlConfClear": trfanCtrlConfClear,
       "trfanCtrlsynth4": trfanCtrlsynth4,
       "trfanCtrlCorrelatOn": trfanCtrlCorrelatOn,
       "trfanCtrlCorrelatOff": trfanCtrlCorrelatOff,
       "trfanCtrlswMgnt": trfanCtrlswMgnt,
       "trfanCtrlColdReset": trfanCtrlColdReset,
       "trfanCtrlWarmReset": trfanCtrlWarmReset,
       "trfanCtrlledTest": trfanCtrlledTest,
       "trfanCtrlGreenLed": trfanCtrlGreenLed,
       "trfanCtrlRedLed": trfanCtrlRedLed,
       "trfanCtrlLedOff": trfanCtrlLedOff,
       "trfanCtrlacknowledgeActiv": trfanCtrlacknowledgeActiv,
       "trfanCtrlAckActiv": trfanCtrlAckActiv,
       "trfanri": trfanri,
       "trfanriTable": trfanriTable,
       "trfanRinvReloadInventory": trfanRinvReloadInventory,
       "trfanRinvHwPlatform": trfanRinvHwPlatform,
       "trfanRinvModulePlatform": trfanRinvModulePlatform,
       "trfanRinvSwPlatform": trfanRinvSwPlatform,
       "trfanConfig": trfanConfig,
       "trfanCfgLsd": trfanCfgLsd,
       "trfanCfgStartUp": trfanCfgStartUp,
       "trfantableother": trfantableother,
       "trfanCfglowspeedThresh": trfanCfglowspeedThresh,
       "trfanCfghighspeedThresh": trfanCfghighspeedThresh,
       "trfanCfgtrfanMgnt": trfanCfgtrfanMgnt,
       "trfanCfgLabels": trfanCfgLabels,
       "trfanCfgWriteConfiguration": trfanCfgWriteConfiguration,
       "trfantraps": trfantraps,
       "trfantrapBoardNumber": trfantrapBoardNumber,
       "trfanPowerTrapUrgentGoesOn": trfanPowerTrapUrgentGoesOn,
       "trfanPowerTrapUrgentGoesOff": trfanPowerTrapUrgentGoesOff,
       "trfanPowerTrapCritGoesOn": trfanPowerTrapCritGoesOn,
       "trfanPowerTrapCritGoesOff": trfanPowerTrapCritGoesOff,
       "trfanFanTrapCritGoesOn": trfanFanTrapCritGoesOn,
       "trfanFanTrapCritGoesOff": trfanFanTrapCritGoesOff}
)
