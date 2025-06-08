# SNMP MIB module (ARBITER-ALL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/arbiter_39849/ARBITER-ALL-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 09:28:50 2025
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

sys = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 39849, 1)
)

ntp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 39849, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class MilliUnits(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-3"


class MicroUnits(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-6"


# MIB Managed Objects in the order of their OIDs

_Arbiter_ObjectIdentity = ObjectIdentity
arbiter = _Arbiter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39849)
)
_Device_ObjectIdentity = ObjectIdentity
device = _Device_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39849, 1, 1)
)
_SysDevLabel_Type = OctetString
_SysDevLabel_Object = MibScalar
sysDevLabel = _SysDevLabel_Object(
    (1, 3, 6, 1, 4, 1, 39849, 1, 1, 1),
    _SysDevLabel_Type()
)
sysDevLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDevLabel.setStatus("current")
_SysDevProduct_Type = OctetString
_SysDevProduct_Object = MibScalar
sysDevProduct = _SysDevProduct_Object(
    (1, 3, 6, 1, 4, 1, 39849, 1, 1, 2),
    _SysDevProduct_Type()
)
sysDevProduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDevProduct.setStatus("current")
_SysDevModel_Type = OctetString
_SysDevModel_Object = MibScalar
sysDevModel = _SysDevModel_Object(
    (1, 3, 6, 1, 4, 1, 39849, 1, 1, 3),
    _SysDevModel_Type()
)
sysDevModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDevModel.setStatus("current")
_SysDevSerialNumber_Type = OctetString
_SysDevSerialNumber_Object = MibScalar
sysDevSerialNumber = _SysDevSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 39849, 1, 1, 4),
    _SysDevSerialNumber_Type()
)
sysDevSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDevSerialNumber.setStatus("current")
_Version_ObjectIdentity = ObjectIdentity
version = _Version_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39849, 1, 1, 5)
)
_SysDevVerLabel_Type = OctetString
_SysDevVerLabel_Object = MibScalar
sysDevVerLabel = _SysDevVerLabel_Object(
    (1, 3, 6, 1, 4, 1, 39849, 1, 1, 5, 1),
    _SysDevVerLabel_Type()
)
sysDevVerLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDevVerLabel.setStatus("current")
_SysDevVerCore_Type = OctetString
_SysDevVerCore_Object = MibScalar
sysDevVerCore = _SysDevVerCore_Object(
    (1, 3, 6, 1, 4, 1, 39849, 1, 1, 5, 2),
    _SysDevVerCore_Type()
)
sysDevVerCore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDevVerCore.setStatus("current")
_SysDevVerMonitor_Type = OctetString
_SysDevVerMonitor_Object = MibScalar
sysDevVerMonitor = _SysDevVerMonitor_Object(
    (1, 3, 6, 1, 4, 1, 39849, 1, 1, 5, 3),
    _SysDevVerMonitor_Type()
)
sysDevVerMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDevVerMonitor.setStatus("current")
_SysDevVerCLOI_Type = OctetString
_SysDevVerCLOI_Object = MibScalar
sysDevVerCLOI = _SysDevVerCLOI_Object(
    (1, 3, 6, 1, 4, 1, 39849, 1, 1, 5, 4),
    _SysDevVerCLOI_Type()
)
sysDevVerCLOI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDevVerCLOI.setStatus("current")
_SysDevVerClock_Type = OctetString
_SysDevVerClock_Object = MibScalar
sysDevVerClock = _SysDevVerClock_Object(
    (1, 3, 6, 1, 4, 1, 39849, 1, 1, 5, 5),
    _SysDevVerClock_Type()
)
sysDevVerClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDevVerClock.setStatus("current")
_SysDevVerNTP_Type = OctetString
_SysDevVerNTP_Object = MibScalar
sysDevVerNTP = _SysDevVerNTP_Object(
    (1, 3, 6, 1, 4, 1, 39849, 1, 1, 5, 6),
    _SysDevVerNTP_Type()
)
sysDevVerNTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDevVerNTP.setStatus("current")
_SysDevVerPTP_Type = OctetString
_SysDevVerPTP_Object = MibScalar
sysDevVerPTP = _SysDevVerPTP_Object(
    (1, 3, 6, 1, 4, 1, 39849, 1, 1, 5, 7),
    _SysDevVerPTP_Type()
)
sysDevVerPTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDevVerPTP.setStatus("current")
_SysDevVerSNMP_Type = OctetString
_SysDevVerSNMP_Object = MibScalar
sysDevVerSNMP = _SysDevVerSNMP_Object(
    (1, 3, 6, 1, 4, 1, 39849, 1, 1, 5, 8),
    _SysDevVerSNMP_Type()
)
sysDevVerSNMP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDevVerSNMP.setStatus("current")
_SysDevClockModel_Type = OctetString
_SysDevClockModel_Object = MibScalar
sysDevClockModel = _SysDevClockModel_Object(
    (1, 3, 6, 1, 4, 1, 39849, 1, 1, 6),
    _SysDevClockModel_Type()
)
sysDevClockModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDevClockModel.setStatus("current")
_Diag_ObjectIdentity = ObjectIdentity
diag = _Diag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39849, 1, 2)
)
_SysDiagLabel_Type = OctetString
_SysDiagLabel_Object = MibScalar
sysDiagLabel = _SysDiagLabel_Object(
    (1, 3, 6, 1, 4, 1, 39849, 1, 2, 1),
    _SysDiagLabel_Type()
)
sysDiagLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDiagLabel.setStatus("current")
_SysDiagTemp_Type = MilliUnits
_SysDiagTemp_Object = MibScalar
sysDiagTemp = _SysDiagTemp_Object(
    (1, 3, 6, 1, 4, 1, 39849, 1, 2, 2),
    _SysDiagTemp_Type()
)
sysDiagTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDiagTemp.setStatus("current")
_SysDiagTimeQuality_Type = OctetString
_SysDiagTimeQuality_Object = MibScalar
sysDiagTimeQuality = _SysDiagTimeQuality_Object(
    (1, 3, 6, 1, 4, 1, 39849, 1, 2, 3),
    _SysDiagTimeQuality_Type()
)
sysDiagTimeQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDiagTimeQuality.setStatus("current")
_SysDiagNtpStatus_Type = OctetString
_SysDiagNtpStatus_Object = MibScalar
sysDiagNtpStatus = _SysDiagNtpStatus_Object(
    (1, 3, 6, 1, 4, 1, 39849, 1, 2, 4),
    _SysDiagNtpStatus_Type()
)
sysDiagNtpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDiagNtpStatus.setStatus("current")
_Config_ObjectIdentity = ObjectIdentity
config = _Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39849, 1, 3)
)
_Gnss_ObjectIdentity = ObjectIdentity
gnss = _Gnss_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39849, 1, 4)
)
_Rec1_ObjectIdentity = ObjectIdentity
rec1 = _Rec1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39849, 1, 4, 1)
)
_GnssRec1Label_Type = OctetString
_GnssRec1Label_Object = MibScalar
gnssRec1Label = _GnssRec1Label_Object(
    (1, 3, 6, 1, 4, 1, 39849, 1, 4, 1, 1),
    _GnssRec1Label_Type()
)
gnssRec1Label.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnssRec1Label.setStatus("current")
_GnssRec1Type_Type = OctetString
_GnssRec1Type_Object = MibScalar
gnssRec1Type = _GnssRec1Type_Object(
    (1, 3, 6, 1, 4, 1, 39849, 1, 4, 1, 2),
    _GnssRec1Type_Type()
)
gnssRec1Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnssRec1Type.setStatus("current")
_GnssRec1SatsVisible_Type = Integer32
_GnssRec1SatsVisible_Object = MibScalar
gnssRec1SatsVisible = _GnssRec1SatsVisible_Object(
    (1, 3, 6, 1, 4, 1, 39849, 1, 4, 1, 3),
    _GnssRec1SatsVisible_Type()
)
gnssRec1SatsVisible.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnssRec1SatsVisible.setStatus("current")
_GnssRec1SatsTracked_Type = Integer32
_GnssRec1SatsTracked_Object = MibScalar
gnssRec1SatsTracked = _GnssRec1SatsTracked_Object(
    (1, 3, 6, 1, 4, 1, 39849, 1, 4, 1, 4),
    _GnssRec1SatsTracked_Type()
)
gnssRec1SatsTracked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnssRec1SatsTracked.setStatus("current")
_Systrap_ObjectIdentity = ObjectIdentity
systrap = _Systrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39849, 1, 5)
)
_SystrapPowerUp_Type = OctetString
_SystrapPowerUp_Object = MibScalar
systrapPowerUp = _SystrapPowerUp_Object(
    (1, 3, 6, 1, 4, 1, 39849, 1, 5, 1),
    _SystrapPowerUp_Type()
)
systrapPowerUp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    systrapPowerUp.setStatus("current")
_SystrapShutDown_Type = OctetString
_SystrapShutDown_Object = MibScalar
systrapShutDown = _SystrapShutDown_Object(
    (1, 3, 6, 1, 4, 1, 39849, 1, 5, 2),
    _SystrapShutDown_Type()
)
systrapShutDown.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    systrapShutDown.setStatus("current")
_SystrapAdminLogin_Type = OctetString
_SystrapAdminLogin_Object = MibScalar
systrapAdminLogin = _SystrapAdminLogin_Object(
    (1, 3, 6, 1, 4, 1, 39849, 1, 5, 3),
    _SystrapAdminLogin_Type()
)
systrapAdminLogin.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    systrapAdminLogin.setStatus("current")
_SystrapAdminLogout_Type = OctetString
_SystrapAdminLogout_Object = MibScalar
systrapAdminLogout = _SystrapAdminLogout_Object(
    (1, 3, 6, 1, 4, 1, 39849, 1, 5, 4),
    _SystrapAdminLogout_Type()
)
systrapAdminLogout.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    systrapAdminLogout.setStatus("current")
_SystrapTimeQuality_Type = Integer32
_SystrapTimeQuality_Object = MibScalar
systrapTimeQuality = _SystrapTimeQuality_Object(
    (1, 3, 6, 1, 4, 1, 39849, 1, 5, 5),
    _SystrapTimeQuality_Type()
)
systrapTimeQuality.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    systrapTimeQuality.setStatus("current")
_Ntpsys_ObjectIdentity = ObjectIdentity
ntpsys = _Ntpsys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39849, 3, 1)
)
_NtpSysString_Type = OctetString
_NtpSysString_Object = MibScalar
ntpSysString = _NtpSysString_Object(
    (1, 3, 6, 1, 4, 1, 39849, 3, 1, 1),
    _NtpSysString_Type()
)
ntpSysString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpSysString.setStatus("current")
_NtpSysClock_Type = OctetString
_NtpSysClock_Object = MibScalar
ntpSysClock = _NtpSysClock_Object(
    (1, 3, 6, 1, 4, 1, 39849, 3, 1, 2),
    _NtpSysClock_Type()
)
ntpSysClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpSysClock.setStatus("current")
_NtpSysClockDateTime_Type = OctetString
_NtpSysClockDateTime_Object = MibScalar
ntpSysClockDateTime = _NtpSysClockDateTime_Object(
    (1, 3, 6, 1, 4, 1, 39849, 3, 1, 3),
    _NtpSysClockDateTime_Type()
)
ntpSysClockDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpSysClockDateTime.setStatus("current")
_NtpSysOffset_Type = Integer32
_NtpSysOffset_Object = MibScalar
ntpSysOffset = _NtpSysOffset_Object(
    (1, 3, 6, 1, 4, 1, 39849, 3, 1, 4),
    _NtpSysOffset_Type()
)
ntpSysOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpSysOffset.setStatus("current")
_NtpSysFreq_Type = MilliUnits
_NtpSysFreq_Object = MibScalar
ntpSysFreq = _NtpSysFreq_Object(
    (1, 3, 6, 1, 4, 1, 39849, 3, 1, 5),
    _NtpSysFreq_Type()
)
ntpSysFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpSysFreq.setStatus("current")
_NtpSysSysJitter_Type = MilliUnits
_NtpSysSysJitter_Object = MibScalar
ntpSysSysJitter = _NtpSysSysJitter_Object(
    (1, 3, 6, 1, 4, 1, 39849, 3, 1, 6),
    _NtpSysSysJitter_Type()
)
ntpSysSysJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpSysSysJitter.setStatus("current")
_NtpSysClkJitter_Type = MilliUnits
_NtpSysClkJitter_Object = MibScalar
ntpSysClkJitter = _NtpSysClkJitter_Object(
    (1, 3, 6, 1, 4, 1, 39849, 3, 1, 7),
    _NtpSysClkJitter_Type()
)
ntpSysClkJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpSysClkJitter.setStatus("current")
_NtpSysClkWander_Type = MilliUnits
_NtpSysClkWander_Object = MibScalar
ntpSysClkWander = _NtpSysClkWander_Object(
    (1, 3, 6, 1, 4, 1, 39849, 3, 1, 8),
    _NtpSysClkWander_Type()
)
ntpSysClkWander.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpSysClkWander.setStatus("current")
_NtpSysRootDelay_Type = MilliUnits
_NtpSysRootDelay_Object = MibScalar
ntpSysRootDelay = _NtpSysRootDelay_Object(
    (1, 3, 6, 1, 4, 1, 39849, 3, 1, 9),
    _NtpSysRootDelay_Type()
)
ntpSysRootDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpSysRootDelay.setStatus("current")
_NtpSysRootDispersion_Type = MilliUnits
_NtpSysRootDispersion_Object = MibScalar
ntpSysRootDispersion = _NtpSysRootDispersion_Object(
    (1, 3, 6, 1, 4, 1, 39849, 3, 1, 10),
    _NtpSysRootDispersion_Type()
)
ntpSysRootDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpSysRootDispersion.setStatus("current")
_NtpSysLeap_Type = Integer32
_NtpSysLeap_Object = MibScalar
ntpSysLeap = _NtpSysLeap_Object(
    (1, 3, 6, 1, 4, 1, 39849, 3, 1, 11),
    _NtpSysLeap_Type()
)
ntpSysLeap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpSysLeap.setStatus("current")


class _NtpSysStratum_Type(Integer32):
    """Custom type ntpSysStratum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NtpSysStratum_Type.__name__ = "Integer32"
_NtpSysStratum_Object = MibScalar
ntpSysStratum = _NtpSysStratum_Object(
    (1, 3, 6, 1, 4, 1, 39849, 3, 1, 12),
    _NtpSysStratum_Type()
)
ntpSysStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpSysStratum.setStatus("current")
_NtpSysPrecision_Type = Integer32
_NtpSysPrecision_Object = MibScalar
ntpSysPrecision = _NtpSysPrecision_Object(
    (1, 3, 6, 1, 4, 1, 39849, 3, 1, 13),
    _NtpSysPrecision_Type()
)
ntpSysPrecision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpSysPrecision.setStatus("current")
_NtpSysRefTime_Type = OctetString
_NtpSysRefTime_Object = MibScalar
ntpSysRefTime = _NtpSysRefTime_Object(
    (1, 3, 6, 1, 4, 1, 39849, 3, 1, 14),
    _NtpSysRefTime_Type()
)
ntpSysRefTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpSysRefTime.setStatus("current")
_Ntptrap_ObjectIdentity = ObjectIdentity
ntptrap = _Ntptrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39849, 3, 2)
)
_NtptrapPowerUp_Type = OctetString
_NtptrapPowerUp_Object = MibScalar
ntptrapPowerUp = _NtptrapPowerUp_Object(
    (1, 3, 6, 1, 4, 1, 39849, 3, 2, 1),
    _NtptrapPowerUp_Type()
)
ntptrapPowerUp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntptrapPowerUp.setStatus("current")
_NtptrapShutDown_Type = OctetString
_NtptrapShutDown_Object = MibScalar
ntptrapShutDown = _NtptrapShutDown_Object(
    (1, 3, 6, 1, 4, 1, 39849, 3, 2, 2),
    _NtptrapShutDown_Type()
)
ntptrapShutDown.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntptrapShutDown.setStatus("current")
_NtptrapSynchronized_Type = OctetString
_NtptrapSynchronized_Object = MibScalar
ntptrapSynchronized = _NtptrapSynchronized_Object(
    (1, 3, 6, 1, 4, 1, 39849, 3, 2, 3),
    _NtptrapSynchronized_Type()
)
ntptrapSynchronized.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntptrapSynchronized.setStatus("current")
_NtptrapSynchronizationLost_Type = OctetString
_NtptrapSynchronizationLost_Object = MibScalar
ntptrapSynchronizationLost = _NtptrapSynchronizationLost_Object(
    (1, 3, 6, 1, 4, 1, 39849, 3, 2, 4),
    _NtptrapSynchronizationLost_Type()
)
ntptrapSynchronizationLost.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntptrapSynchronizationLost.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARBITER-ALL-MIB",
    **{"MilliUnits": MilliUnits,
       "MicroUnits": MicroUnits,
       "arbiter": arbiter,
       "sys": sys,
       "device": device,
       "sysDevLabel": sysDevLabel,
       "sysDevProduct": sysDevProduct,
       "sysDevModel": sysDevModel,
       "sysDevSerialNumber": sysDevSerialNumber,
       "version": version,
       "sysDevVerLabel": sysDevVerLabel,
       "sysDevVerCore": sysDevVerCore,
       "sysDevVerMonitor": sysDevVerMonitor,
       "sysDevVerCLOI": sysDevVerCLOI,
       "sysDevVerClock": sysDevVerClock,
       "sysDevVerNTP": sysDevVerNTP,
       "sysDevVerPTP": sysDevVerPTP,
       "sysDevVerSNMP": sysDevVerSNMP,
       "sysDevClockModel": sysDevClockModel,
       "diag": diag,
       "sysDiagLabel": sysDiagLabel,
       "sysDiagTemp": sysDiagTemp,
       "sysDiagTimeQuality": sysDiagTimeQuality,
       "sysDiagNtpStatus": sysDiagNtpStatus,
       "config": config,
       "gnss": gnss,
       "rec1": rec1,
       "gnssRec1Label": gnssRec1Label,
       "gnssRec1Type": gnssRec1Type,
       "gnssRec1SatsVisible": gnssRec1SatsVisible,
       "gnssRec1SatsTracked": gnssRec1SatsTracked,
       "systrap": systrap,
       "systrapPowerUp": systrapPowerUp,
       "systrapShutDown": systrapShutDown,
       "systrapAdminLogin": systrapAdminLogin,
       "systrapAdminLogout": systrapAdminLogout,
       "systrapTimeQuality": systrapTimeQuality,
       "ntp": ntp,
       "ntpsys": ntpsys,
       "ntpSysString": ntpSysString,
       "ntpSysClock": ntpSysClock,
       "ntpSysClockDateTime": ntpSysClockDateTime,
       "ntpSysOffset": ntpSysOffset,
       "ntpSysFreq": ntpSysFreq,
       "ntpSysSysJitter": ntpSysSysJitter,
       "ntpSysClkJitter": ntpSysClkJitter,
       "ntpSysClkWander": ntpSysClkWander,
       "ntpSysRootDelay": ntpSysRootDelay,
       "ntpSysRootDispersion": ntpSysRootDispersion,
       "ntpSysLeap": ntpSysLeap,
       "ntpSysStratum": ntpSysStratum,
       "ntpSysPrecision": ntpSysPrecision,
       "ntpSysRefTime": ntpSysRefTime,
       "ntptrap": ntptrap,
       "ntptrapPowerUp": ntptrapPowerUp,
       "ntptrapShutDown": ntptrapShutDown,
       "ntptrapSynchronized": ntptrapSynchronized,
       "ntptrapSynchronizationLost": ntptrapSynchronizationLost}
)
