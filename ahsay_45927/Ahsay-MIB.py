# SNMP MIB module (Ahsay-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ahsay_45927/Ahsay-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 00:15:59 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ahsay_ObjectIdentity = ObjectIdentity
ahsay = _Ahsay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45927)
)
_Obs_ObjectIdentity = ObjectIdentity
obs = _Obs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45927, 1)
)
_Trap_ObjectIdentity = ObjectIdentity
trap = _Trap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45927, 1, 1)
)
_SysService_ObjectIdentity = ObjectIdentity
sysService = _SysService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45927, 1, 1, 1)
)
_SysOutOfMemory_Type = Integer32
_SysOutOfMemory_Object = MibScalar
sysOutOfMemory = _SysOutOfMemory_Object(
    (1, 3, 6, 1, 4, 1, 45927, 1, 1, 1, 1),
    _SysOutOfMemory_Type()
)
sysOutOfMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysOutOfMemory.setStatus("mandatory")
_SysHighCpu_Type = Integer32
_SysHighCpu_Object = MibScalar
sysHighCpu = _SysHighCpu_Object(
    (1, 3, 6, 1, 4, 1, 45927, 1, 1, 1, 2),
    _SysHighCpu_Type()
)
sysHighCpu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHighCpu.setStatus("mandatory")
_SysSystemHomeLowDiskSpace_Type = Integer32
_SysSystemHomeLowDiskSpace_Object = MibScalar
sysSystemHomeLowDiskSpace = _SysSystemHomeLowDiskSpace_Object(
    (1, 3, 6, 1, 4, 1, 45927, 1, 1, 1, 3),
    _SysSystemHomeLowDiskSpace_Type()
)
sysSystemHomeLowDiskSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSystemHomeLowDiskSpace.setStatus("mandatory")
_SysUserHomeLowDiskSpace_Type = Integer32
_SysUserHomeLowDiskSpace_Object = MibScalar
sysUserHomeLowDiskSpace = _SysUserHomeLowDiskSpace_Object(
    (1, 3, 6, 1, 4, 1, 45927, 1, 1, 1, 4),
    _SysUserHomeLowDiskSpace_Type()
)
sysUserHomeLowDiskSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysUserHomeLowDiskSpace.setStatus("mandatory")
_SysPolicyHomeLowDiskSpace_Type = Integer32
_SysPolicyHomeLowDiskSpace_Object = MibScalar
sysPolicyHomeLowDiskSpace = _SysPolicyHomeLowDiskSpace_Object(
    (1, 3, 6, 1, 4, 1, 45927, 1, 1, 1, 5),
    _SysPolicyHomeLowDiskSpace_Type()
)
sysPolicyHomeLowDiskSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysPolicyHomeLowDiskSpace.setStatus("mandatory")
_SysConnection_ObjectIdentity = ObjectIdentity
sysConnection = _SysConnection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45927, 1, 1, 2)
)
_SysAlsConnFailure_Type = OctetString
_SysAlsConnFailure_Object = MibScalar
sysAlsConnFailure = _SysAlsConnFailure_Object(
    (1, 3, 6, 1, 4, 1, 45927, 1, 1, 2, 1),
    _SysAlsConnFailure_Type()
)
sysAlsConnFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysAlsConnFailure.setStatus("mandatory")
_SysRpsConnFailure_Type = OctetString
_SysRpsConnFailure_Object = MibScalar
sysRpsConnFailure = _SysRpsConnFailure_Object(
    (1, 3, 6, 1, 4, 1, 45927, 1, 1, 2, 2),
    _SysRpsConnFailure_Type()
)
sysRpsConnFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysRpsConnFailure.setStatus("mandatory")
_LicError_ObjectIdentity = ObjectIdentity
licError = _LicError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45927, 1, 1, 3)
)
_SysLic1011_Type = OctetString
_SysLic1011_Object = MibScalar
sysLic1011 = _SysLic1011_Object(
    (1, 3, 6, 1, 4, 1, 45927, 1, 1, 3, 1),
    _SysLic1011_Type()
)
sysLic1011.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLic1011.setStatus("mandatory")
_SysLic1012_Type = OctetString
_SysLic1012_Object = MibScalar
sysLic1012 = _SysLic1012_Object(
    (1, 3, 6, 1, 4, 1, 45927, 1, 1, 3, 2),
    _SysLic1012_Type()
)
sysLic1012.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLic1012.setStatus("mandatory")
_UsrAccountError_ObjectIdentity = ObjectIdentity
usrAccountError = _UsrAccountError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45927, 1, 1, 4)
)
_UsrAccountLocked_Type = OctetString
_UsrAccountLocked_Object = MibScalar
usrAccountLocked = _UsrAccountLocked_Object(
    (1, 3, 6, 1, 4, 1, 45927, 1, 1, 4, 1),
    _UsrAccountLocked_Type()
)
usrAccountLocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usrAccountLocked.setStatus("mandatory")
_SysError_ObjectIdentity = ObjectIdentity
sysError = _SysError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45927, 1, 1, 5)
)
_ObsSysError_Type = OctetString
_ObsSysError_Object = MibScalar
obsSysError = _ObsSysError_Object(
    (1, 3, 6, 1, 4, 1, 45927, 1, 1, 5, 1),
    _ObsSysError_Type()
)
obsSysError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obsSysError.setStatus("mandatory")
_GetRequest_ObjectIdentity = ObjectIdentity
getRequest = _GetRequest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45927, 1, 2)
)
_SysPerformance_ObjectIdentity = ObjectIdentity
sysPerformance = _SysPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45927, 1, 2, 1)
)
_SysCpuUsage_Type = Integer32
_SysCpuUsage_Object = MibScalar
sysCpuUsage = _SysCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 45927, 1, 2, 1, 1),
    _SysCpuUsage_Type()
)
sysCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysCpuUsage.setStatus("mandatory")
_SysHeapCurrent_Type = Integer32
_SysHeapCurrent_Object = MibScalar
sysHeapCurrent = _SysHeapCurrent_Object(
    (1, 3, 6, 1, 4, 1, 45927, 1, 2, 1, 2),
    _SysHeapCurrent_Type()
)
sysHeapCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHeapCurrent.setStatus("mandatory")
_SysHeapTotal_Type = Integer32
_SysHeapTotal_Object = MibScalar
sysHeapTotal = _SysHeapTotal_Object(
    (1, 3, 6, 1, 4, 1, 45927, 1, 2, 1, 3),
    _SysHeapTotal_Type()
)
sysHeapTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHeapTotal.setStatus("mandatory")
_SysThreadCurrent_Type = Integer32
_SysThreadCurrent_Object = MibScalar
sysThreadCurrent = _SysThreadCurrent_Object(
    (1, 3, 6, 1, 4, 1, 45927, 1, 2, 1, 4),
    _SysThreadCurrent_Type()
)
sysThreadCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysThreadCurrent.setStatus("mandatory")
_SysThreadLive_Type = Integer32
_SysThreadLive_Object = MibScalar
sysThreadLive = _SysThreadLive_Object(
    (1, 3, 6, 1, 4, 1, 45927, 1, 2, 1, 5),
    _SysThreadLive_Type()
)
sysThreadLive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysThreadLive.setStatus("mandatory")
_SysHome_ObjectIdentity = ObjectIdentity
sysHome = _SysHome_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45927, 1, 2, 2)
)
_SysHomePath_Type = OctetString
_SysHomePath_Object = MibScalar
sysHomePath = _SysHomePath_Object(
    (1, 3, 6, 1, 4, 1, 45927, 1, 2, 2, 1),
    _SysHomePath_Type()
)
sysHomePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHomePath.setStatus("mandatory")
_SysHomeSpaceUsed_Type = Integer32
_SysHomeSpaceUsed_Object = MibScalar
sysHomeSpaceUsed = _SysHomeSpaceUsed_Object(
    (1, 3, 6, 1, 4, 1, 45927, 1, 2, 2, 2),
    _SysHomeSpaceUsed_Type()
)
sysHomeSpaceUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHomeSpaceUsed.setStatus("mandatory")
_SysHomeSpaceFree_Type = Integer32
_SysHomeSpaceFree_Object = MibScalar
sysHomeSpaceFree = _SysHomeSpaceFree_Object(
    (1, 3, 6, 1, 4, 1, 45927, 1, 2, 2, 3),
    _SysHomeSpaceFree_Type()
)
sysHomeSpaceFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHomeSpaceFree.setStatus("mandatory")
_PolHome_ObjectIdentity = ObjectIdentity
polHome = _PolHome_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45927, 1, 2, 3)
)
_PolHomePath_Type = OctetString
_PolHomePath_Object = MibScalar
polHomePath = _PolHomePath_Object(
    (1, 3, 6, 1, 4, 1, 45927, 1, 2, 3, 1),
    _PolHomePath_Type()
)
polHomePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    polHomePath.setStatus("mandatory")
_PolHomeSpaceUsed_Type = Integer32
_PolHomeSpaceUsed_Object = MibScalar
polHomeSpaceUsed = _PolHomeSpaceUsed_Object(
    (1, 3, 6, 1, 4, 1, 45927, 1, 2, 3, 2),
    _PolHomeSpaceUsed_Type()
)
polHomeSpaceUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    polHomeSpaceUsed.setStatus("mandatory")
_PolHomeSpaceFree_Type = Integer32
_PolHomeSpaceFree_Object = MibScalar
polHomeSpaceFree = _PolHomeSpaceFree_Object(
    (1, 3, 6, 1, 4, 1, 45927, 1, 2, 3, 3),
    _PolHomeSpaceFree_Type()
)
polHomeSpaceFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    polHomeSpaceFree.setStatus("mandatory")
_GetNextRequest_ObjectIdentity = ObjectIdentity
getNextRequest = _GetNextRequest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45927, 1, 3)
)
_UsrHome_ObjectIdentity = ObjectIdentity
usrHome = _UsrHome_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45927, 1, 3, 1)
)
_UsrHomeTable_Object = MibTable
usrHomeTable = _UsrHomeTable_Object(
    (1, 3, 6, 1, 4, 1, 45927, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    usrHomeTable.setStatus("mandatory")
_UsrHomeEntry_Object = MibTableRow
usrHomeEntry = _UsrHomeEntry_Object(
    (1, 3, 6, 1, 4, 1, 45927, 1, 3, 1, 1, 1)
)
usrHomeEntry.setIndexNames(
    (0, "Ahsay-MIB", "homePath"),
)
if mibBuilder.loadTexts:
    usrHomeEntry.setStatus("mandatory")


class _HomePath_Type(DisplayString):
    """Custom type homePath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 114),
    )


_HomePath_Type.__name__ = "DisplayString"
_HomePath_Object = MibTableColumn
homePath = _HomePath_Object(
    (1, 3, 6, 1, 4, 1, 45927, 1, 3, 1, 1, 1, 1),
    _HomePath_Type()
)
homePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    homePath.setStatus("mandatory")
_HomeSpaceUsed_Type = Integer32
_HomeSpaceUsed_Object = MibTableColumn
homeSpaceUsed = _HomeSpaceUsed_Object(
    (1, 3, 6, 1, 4, 1, 45927, 1, 3, 1, 1, 1, 2),
    _HomeSpaceUsed_Type()
)
homeSpaceUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    homeSpaceUsed.setStatus("mandatory")
_HomeSpaceFree_Type = Integer32
_HomeSpaceFree_Object = MibTableColumn
homeSpaceFree = _HomeSpaceFree_Object(
    (1, 3, 6, 1, 4, 1, 45927, 1, 3, 1, 1, 1, 3),
    _HomeSpaceFree_Type()
)
homeSpaceFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    homeSpaceFree.setStatus("mandatory")
_UsrProfile_ObjectIdentity = ObjectIdentity
usrProfile = _UsrProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45927, 1, 3, 2)
)
_UsrProfileTable_Object = MibTable
usrProfileTable = _UsrProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 45927, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    usrProfileTable.setStatus("mandatory")
_UsrProfileEntry_Object = MibTableRow
usrProfileEntry = _UsrProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 45927, 1, 3, 2, 1, 1)
)
usrProfileEntry.setIndexNames(
    (0, "Ahsay-MIB", "usrKey"),
)
if mibBuilder.loadTexts:
    usrProfileEntry.setStatus("mandatory")


class _UsrKey_Type(DisplayString):
    """Custom type usrKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 114),
    )


_UsrKey_Type.__name__ = "DisplayString"
_UsrKey_Object = MibTableColumn
usrKey = _UsrKey_Object(
    (1, 3, 6, 1, 4, 1, 45927, 1, 3, 2, 1, 1, 1),
    _UsrKey_Type()
)
usrKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usrKey.setStatus("mandatory")


class _UsrLoginName_Type(DisplayString):
    """Custom type usrLoginName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_UsrLoginName_Type.__name__ = "DisplayString"
_UsrLoginName_Object = MibTableColumn
usrLoginName = _UsrLoginName_Object(
    (1, 3, 6, 1, 4, 1, 45927, 1, 3, 2, 1, 1, 2),
    _UsrLoginName_Type()
)
usrLoginName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usrLoginName.setStatus("mandatory")


class _UsrAlias_Type(DisplayString):
    """Custom type usrAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_UsrAlias_Type.__name__ = "DisplayString"
_UsrAlias_Object = MibTableColumn
usrAlias = _UsrAlias_Object(
    (1, 3, 6, 1, 4, 1, 45927, 1, 3, 2, 1, 1, 3),
    _UsrAlias_Type()
)
usrAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usrAlias.setStatus("mandatory")


class _UsrOwner_Type(DisplayString):
    """Custom type usrOwner based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_UsrOwner_Type.__name__ = "DisplayString"
_UsrOwner_Object = MibTableColumn
usrOwner = _UsrOwner_Object(
    (1, 3, 6, 1, 4, 1, 45927, 1, 3, 2, 1, 1, 4),
    _UsrOwner_Type()
)
usrOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usrOwner.setStatus("mandatory")


class _UsrPayType_Type(DisplayString):
    """Custom type usrPayType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_UsrPayType_Type.__name__ = "DisplayString"
_UsrPayType_Object = MibTableColumn
usrPayType = _UsrPayType_Object(
    (1, 3, 6, 1, 4, 1, 45927, 1, 3, 2, 1, 1, 5),
    _UsrPayType_Type()
)
usrPayType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usrPayType.setStatus("mandatory")


class _UsrClientType_Type(DisplayString):
    """Custom type usrClientType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixed_length = 3


_UsrClientType_Type.__name__ = "DisplayString"
_UsrClientType_Object = MibTableColumn
usrClientType = _UsrClientType_Object(
    (1, 3, 6, 1, 4, 1, 45927, 1, 3, 2, 1, 1, 6),
    _UsrClientType_Type()
)
usrClientType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usrClientType.setStatus("mandatory")


class _UsrStatus_Type(DisplayString):
    """Custom type usrStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_UsrStatus_Type.__name__ = "DisplayString"
_UsrStatus_Object = MibTableColumn
usrStatus = _UsrStatus_Object(
    (1, 3, 6, 1, 4, 1, 45927, 1, 3, 2, 1, 1, 7),
    _UsrStatus_Type()
)
usrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usrStatus.setStatus("mandatory")
_UsrLoginFailureCount_Type = Integer32
_UsrLoginFailureCount_Object = MibTableColumn
usrLoginFailureCount = _UsrLoginFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 45927, 1, 3, 2, 1, 1, 8),
    _UsrLoginFailureCount_Type()
)
usrLoginFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usrLoginFailureCount.setStatus("mandatory")


class _UsrDataSize_Type(DisplayString):
    """Custom type usrDataSize based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_UsrDataSize_Type.__name__ = "DisplayString"
_UsrDataSize_Object = MibTableColumn
usrDataSize = _UsrDataSize_Object(
    (1, 3, 6, 1, 4, 1, 45927, 1, 3, 2, 1, 1, 9),
    _UsrDataSize_Type()
)
usrDataSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usrDataSize.setStatus("mandatory")


class _UsrRetentionSize_Type(DisplayString):
    """Custom type usrRetentionSize based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_UsrRetentionSize_Type.__name__ = "DisplayString"
_UsrRetentionSize_Object = MibTableColumn
usrRetentionSize = _UsrRetentionSize_Object(
    (1, 3, 6, 1, 4, 1, 45927, 1, 3, 2, 1, 1, 10),
    _UsrRetentionSize_Type()
)
usrRetentionSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usrRetentionSize.setStatus("mandatory")


class _UsrQuotaFree_Type(DisplayString):
    """Custom type usrQuotaFree based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_UsrQuotaFree_Type.__name__ = "DisplayString"
_UsrQuotaFree_Object = MibTableColumn
usrQuotaFree = _UsrQuotaFree_Object(
    (1, 3, 6, 1, 4, 1, 45927, 1, 3, 2, 1, 1, 11),
    _UsrQuotaFree_Type()
)
usrQuotaFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usrQuotaFree.setStatus("mandatory")
_RepSender_ObjectIdentity = ObjectIdentity
repSender = _RepSender_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45927, 1, 3, 3)
)
_RepSenderTable_Object = MibTable
repSenderTable = _RepSenderTable_Object(
    (1, 3, 6, 1, 4, 1, 45927, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    repSenderTable.setStatus("mandatory")
_RepSenderEntry_Object = MibTableRow
repSenderEntry = _RepSenderEntry_Object(
    (1, 3, 6, 1, 4, 1, 45927, 1, 3, 3, 1, 1)
)
repSenderEntry.setIndexNames(
    (0, "Ahsay-MIB", "bsetId"),
)
if mibBuilder.loadTexts:
    repSenderEntry.setStatus("mandatory")


class _BsetId_Type(DisplayString):
    """Custom type bsetId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 114),
    )


_BsetId_Type.__name__ = "DisplayString"
_BsetId_Object = MibTableColumn
bsetId = _BsetId_Object(
    (1, 3, 6, 1, 4, 1, 45927, 1, 3, 3, 1, 1, 1),
    _BsetId_Type()
)
bsetId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsetId.setStatus("mandatory")


class _Status_Type(DisplayString):
    """Custom type status based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Status_Type.__name__ = "DisplayString"
_Status_Object = MibTableColumn
status = _Status_Object(
    (1, 3, 6, 1, 4, 1, 45927, 1, 3, 3, 1, 1, 2),
    _Status_Type()
)
status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status.setStatus("mandatory")
_Progress_Type = Integer32
_Progress_Object = MibTableColumn
progress = _Progress_Object(
    (1, 3, 6, 1, 4, 1, 45927, 1, 3, 3, 1, 1, 3),
    _Progress_Type()
)
progress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    progress.setStatus("mandatory")


class _TimeLeft_Type(DisplayString):
    """Custom type timeLeft based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TimeLeft_Type.__name__ = "DisplayString"
_TimeLeft_Object = MibTableColumn
timeLeft = _TimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 45927, 1, 3, 3, 1, 1, 4),
    _TimeLeft_Type()
)
timeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeLeft.setStatus("mandatory")


class _Path_Type(DisplayString):
    """Custom type path based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Path_Type.__name__ = "DisplayString"
_Path_Object = MibTableColumn
path = _Path_Object(
    (1, 3, 6, 1, 4, 1, 45927, 1, 3, 3, 1, 1, 5),
    _Path_Type()
)
path.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    path.setStatus("mandatory")
_Rps_ObjectIdentity = ObjectIdentity
rps = _Rps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45927, 2)
)
_RpsTrap_ObjectIdentity = ObjectIdentity
rpsTrap = _RpsTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45927, 2, 1)
)
_RpsSysError_ObjectIdentity = ObjectIdentity
rpsSysError = _RpsSysError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45927, 2, 1, 1)
)
_RpsSysErrorGen_Type = OctetString
_RpsSysErrorGen_Object = MibScalar
rpsSysErrorGen = _RpsSysErrorGen_Object(
    (1, 3, 6, 1, 4, 1, 45927, 2, 1, 1, 1),
    _RpsSysErrorGen_Type()
)
rpsSysErrorGen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpsSysErrorGen.setStatus("mandatory")
_RpsSysErrorRetention_Type = OctetString
_RpsSysErrorRetention_Object = MibScalar
rpsSysErrorRetention = _RpsSysErrorRetention_Object(
    (1, 3, 6, 1, 4, 1, 45927, 2, 1, 1, 2),
    _RpsSysErrorRetention_Type()
)
rpsSysErrorRetention.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpsSysErrorRetention.setStatus("mandatory")
_RpsSysErrorCrc_Type = OctetString
_RpsSysErrorCrc_Object = MibScalar
rpsSysErrorCrc = _RpsSysErrorCrc_Object(
    (1, 3, 6, 1, 4, 1, 45927, 2, 1, 1, 3),
    _RpsSysErrorCrc_Type()
)
rpsSysErrorCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpsSysErrorCrc.setStatus("mandatory")
_Rdr_ObjectIdentity = ObjectIdentity
rdr = _Rdr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45927, 3)
)
_RdrTrap_ObjectIdentity = ObjectIdentity
rdrTrap = _RdrTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45927, 3, 1)
)
_RdrSysError_ObjectIdentity = ObjectIdentity
rdrSysError = _RdrSysError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45927, 3, 1, 1)
)
_RdrLicError_Type = OctetString
_RdrLicError_Object = MibScalar
rdrLicError = _RdrLicError_Object(
    (1, 3, 6, 1, 4, 1, 45927, 3, 1, 1, 1),
    _RdrLicError_Type()
)
rdrLicError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdrLicError.setStatus("mandatory")
_Cbs_ObjectIdentity = ObjectIdentity
cbs = _Cbs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45927, 4)
)
_CbsTrap_ObjectIdentity = ObjectIdentity
cbsTrap = _CbsTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45927, 4, 1)
)
_CbsSysError_ObjectIdentity = ObjectIdentity
cbsSysError = _CbsSysError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45927, 4, 1, 1)
)
_CbsJobError_Type = OctetString
_CbsJobError_Object = MibScalar
cbsJobError = _CbsJobError_Object(
    (1, 3, 6, 1, 4, 1, 45927, 4, 1, 1, 1),
    _CbsJobError_Type()
)
cbsJobError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsJobError.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Ahsay-MIB",
    **{"ahsay": ahsay,
       "obs": obs,
       "trap": trap,
       "sysService": sysService,
       "sysOutOfMemory": sysOutOfMemory,
       "sysHighCpu": sysHighCpu,
       "sysSystemHomeLowDiskSpace": sysSystemHomeLowDiskSpace,
       "sysUserHomeLowDiskSpace": sysUserHomeLowDiskSpace,
       "sysPolicyHomeLowDiskSpace": sysPolicyHomeLowDiskSpace,
       "sysConnection": sysConnection,
       "sysAlsConnFailure": sysAlsConnFailure,
       "sysRpsConnFailure": sysRpsConnFailure,
       "licError": licError,
       "sysLic1011": sysLic1011,
       "sysLic1012": sysLic1012,
       "usrAccountError": usrAccountError,
       "usrAccountLocked": usrAccountLocked,
       "sysError": sysError,
       "obsSysError": obsSysError,
       "getRequest": getRequest,
       "sysPerformance": sysPerformance,
       "sysCpuUsage": sysCpuUsage,
       "sysHeapCurrent": sysHeapCurrent,
       "sysHeapTotal": sysHeapTotal,
       "sysThreadCurrent": sysThreadCurrent,
       "sysThreadLive": sysThreadLive,
       "sysHome": sysHome,
       "sysHomePath": sysHomePath,
       "sysHomeSpaceUsed": sysHomeSpaceUsed,
       "sysHomeSpaceFree": sysHomeSpaceFree,
       "polHome": polHome,
       "polHomePath": polHomePath,
       "polHomeSpaceUsed": polHomeSpaceUsed,
       "polHomeSpaceFree": polHomeSpaceFree,
       "getNextRequest": getNextRequest,
       "usrHome": usrHome,
       "usrHomeTable": usrHomeTable,
       "usrHomeEntry": usrHomeEntry,
       "homePath": homePath,
       "homeSpaceUsed": homeSpaceUsed,
       "homeSpaceFree": homeSpaceFree,
       "usrProfile": usrProfile,
       "usrProfileTable": usrProfileTable,
       "usrProfileEntry": usrProfileEntry,
       "usrKey": usrKey,
       "usrLoginName": usrLoginName,
       "usrAlias": usrAlias,
       "usrOwner": usrOwner,
       "usrPayType": usrPayType,
       "usrClientType": usrClientType,
       "usrStatus": usrStatus,
       "usrLoginFailureCount": usrLoginFailureCount,
       "usrDataSize": usrDataSize,
       "usrRetentionSize": usrRetentionSize,
       "usrQuotaFree": usrQuotaFree,
       "repSender": repSender,
       "repSenderTable": repSenderTable,
       "repSenderEntry": repSenderEntry,
       "bsetId": bsetId,
       "status": status,
       "progress": progress,
       "timeLeft": timeLeft,
       "path": path,
       "rps": rps,
       "rpsTrap": rpsTrap,
       "rpsSysError": rpsSysError,
       "rpsSysErrorGen": rpsSysErrorGen,
       "rpsSysErrorRetention": rpsSysErrorRetention,
       "rpsSysErrorCrc": rpsSysErrorCrc,
       "rdr": rdr,
       "rdrTrap": rdrTrap,
       "rdrSysError": rdrSysError,
       "rdrLicError": rdrLicError,
       "cbs": cbs,
       "cbsTrap": cbsTrap,
       "cbsSysError": cbsSysError,
       "cbsJobError": cbsJobError}
)
