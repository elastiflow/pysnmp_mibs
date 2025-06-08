# SNMP MIB module (VARMOUR-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/varmour_42825/VARMOUR-SYSTEM-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 12:05:54 2025
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")

(varmourMibs,) = mibBuilder.importSymbols(
    "VARMOUR-SMI",
    "varmourMibs")

(VarmourDevice,) = mibBuilder.importSymbols(
    "VARMOUR-TC",
    "VarmourDevice")


# MODULE-IDENTITY

varmour_system = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VaSystem_ObjectIdentity = ObjectIdentity
vaSystem = _VaSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 1, 1)
)


class _VaSysHostname_Type(OctetString):
    """Custom type vaSysHostname based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_VaSysHostname_Type.__name__ = "OctetString"
_VaSysHostname_Object = MibScalar
vaSysHostname = _VaSysHostname_Object(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 1, 1, 1),
    _VaSysHostname_Type()
)
vaSysHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaSysHostname.setStatus("current")


class _VaSysFabIf_Type(OctetString):
    """Custom type vaSysFabIf based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_VaSysFabIf_Type.__name__ = "OctetString"
_VaSysFabIf_Object = MibScalar
vaSysFabIf = _VaSysFabIf_Object(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 1, 1, 2),
    _VaSysFabIf_Type()
)
vaSysFabIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaSysFabIf.setStatus("current")


class _VaSysFabAddr_Type(OctetString):
    """Custom type vaSysFabAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_VaSysFabAddr_Type.__name__ = "OctetString"
_VaSysFabAddr_Object = MibScalar
vaSysFabAddr = _VaSysFabAddr_Object(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 1, 1, 3),
    _VaSysFabAddr_Type()
)
vaSysFabAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaSysFabAddr.setStatus("current")


class _VaSysMgmtIf_Type(OctetString):
    """Custom type vaSysMgmtIf based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_VaSysMgmtIf_Type.__name__ = "OctetString"
_VaSysMgmtIf_Object = MibScalar
vaSysMgmtIf = _VaSysMgmtIf_Object(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 1, 1, 4),
    _VaSysMgmtIf_Type()
)
vaSysMgmtIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaSysMgmtIf.setStatus("current")


class _VaSysMgmtAddr_Type(OctetString):
    """Custom type vaSysMgmtAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_VaSysMgmtAddr_Type.__name__ = "OctetString"
_VaSysMgmtAddr_Object = MibScalar
vaSysMgmtAddr = _VaSysMgmtAddr_Object(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 1, 1, 5),
    _VaSysMgmtAddr_Type()
)
vaSysMgmtAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaSysMgmtAddr.setStatus("current")


class _VaSysMgmtGateway_Type(OctetString):
    """Custom type vaSysMgmtGateway based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_VaSysMgmtGateway_Type.__name__ = "OctetString"
_VaSysMgmtGateway_Object = MibScalar
vaSysMgmtGateway = _VaSysMgmtGateway_Object(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 1, 1, 6),
    _VaSysMgmtGateway_Type()
)
vaSysMgmtGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaSysMgmtGateway.setStatus("current")


class _VaSysTime_Type(OctetString):
    """Custom type vaSysTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_VaSysTime_Type.__name__ = "OctetString"
_VaSysTime_Object = MibScalar
vaSysTime = _VaSysTime_Object(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 1, 1, 7),
    _VaSysTime_Type()
)
vaSysTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaSysTime.setStatus("current")


class _VaSysUptime_Type(OctetString):
    """Custom type vaSysUptime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_VaSysUptime_Type.__name__ = "OctetString"
_VaSysUptime_Object = MibScalar
vaSysUptime = _VaSysUptime_Object(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 1, 1, 8),
    _VaSysUptime_Type()
)
vaSysUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaSysUptime.setStatus("current")


class _VaSysModel_Type(OctetString):
    """Custom type vaSysModel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_VaSysModel_Type.__name__ = "OctetString"
_VaSysModel_Object = MibScalar
vaSysModel = _VaSysModel_Object(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 1, 1, 9),
    _VaSysModel_Type()
)
vaSysModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaSysModel.setStatus("current")


class _VaSysSerialNum_Type(OctetString):
    """Custom type vaSysSerialNum based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_VaSysSerialNum_Type.__name__ = "OctetString"
_VaSysSerialNum_Object = MibScalar
vaSysSerialNum = _VaSysSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 1, 1, 10),
    _VaSysSerialNum_Type()
)
vaSysSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaSysSerialNum.setStatus("current")


class _VaSysSwVer_Type(OctetString):
    """Custom type vaSysSwVer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_VaSysSwVer_Type.__name__ = "OctetString"
_VaSysSwVer_Object = MibScalar
vaSysSwVer = _VaSysSwVer_Object(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 1, 1, 11),
    _VaSysSwVer_Type()
)
vaSysSwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaSysSwVer.setStatus("current")


class _VaSysBootDir_Type(OctetString):
    """Custom type vaSysBootDir based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_VaSysBootDir_Type.__name__ = "OctetString"
_VaSysBootDir_Object = MibScalar
vaSysBootDir = _VaSysBootDir_Object(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 1, 1, 12),
    _VaSysBootDir_Type()
)
vaSysBootDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaSysBootDir.setStatus("current")


class _VaSysSecPack_Type(OctetString):
    """Custom type vaSysSecPack based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_VaSysSecPack_Type.__name__ = "OctetString"
_VaSysSecPack_Object = MibScalar
vaSysSecPack = _VaSysSecPack_Object(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 1, 1, 13),
    _VaSysSecPack_Type()
)
vaSysSecPack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaSysSecPack.setStatus("current")


class _VaSysDirSecret_Type(OctetString):
    """Custom type vaSysDirSecret based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_VaSysDirSecret_Type.__name__ = "OctetString"
_VaSysDirSecret_Object = MibScalar
vaSysDirSecret = _VaSysDirSecret_Object(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 1, 1, 14),
    _VaSysDirSecret_Type()
)
vaSysDirSecret.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaSysDirSecret.setStatus("current")
_VaLicense_ObjectIdentity = ObjectIdentity
vaLicense = _VaLicense_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 1, 2)
)


class _VaLicWarning_Type(OctetString):
    """Custom type vaLicWarning based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VaLicWarning_Type.__name__ = "OctetString"
_VaLicWarning_Object = MibScalar
vaLicWarning = _VaLicWarning_Object(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 1, 2, 1),
    _VaLicWarning_Type()
)
vaLicWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaLicWarning.setStatus("current")


class _VaLicCustName_Type(OctetString):
    """Custom type vaLicCustName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VaLicCustName_Type.__name__ = "OctetString"
_VaLicCustName_Object = MibScalar
vaLicCustName = _VaLicCustName_Object(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 1, 2, 2),
    _VaLicCustName_Type()
)
vaLicCustName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaLicCustName.setStatus("current")


class _VaLicSerialNum_Type(OctetString):
    """Custom type vaLicSerialNum based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VaLicSerialNum_Type.__name__ = "OctetString"
_VaLicSerialNum_Object = MibScalar
vaLicSerialNum = _VaLicSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 1, 2, 3),
    _VaLicSerialNum_Type()
)
vaLicSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaLicSerialNum.setStatus("current")


class _VaLicExpiration_Type(OctetString):
    """Custom type vaLicExpiration based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VaLicExpiration_Type.__name__ = "OctetString"
_VaLicExpiration_Object = MibScalar
vaLicExpiration = _VaLicExpiration_Object(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 1, 2, 4),
    _VaLicExpiration_Type()
)
vaLicExpiration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaLicExpiration.setStatus("current")
_VaLicSeatNum_Type = Integer32
_VaLicSeatNum_Object = MibScalar
vaLicSeatNum = _VaLicSeatNum_Object(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 1, 2, 5),
    _VaLicSeatNum_Type()
)
vaLicSeatNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaLicSeatNum.setStatus("current")


class _VaLicType_Type(OctetString):
    """Custom type vaLicType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VaLicType_Type.__name__ = "OctetString"
_VaLicType_Object = MibScalar
vaLicType = _VaLicType_Object(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 1, 2, 6),
    _VaLicType_Type()
)
vaLicType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaLicType.setStatus("current")


class _VaLicUUID_Type(OctetString):
    """Custom type vaLicUUID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VaLicUUID_Type.__name__ = "OctetString"
_VaLicUUID_Object = MibScalar
vaLicUUID = _VaLicUUID_Object(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 1, 2, 7),
    _VaLicUUID_Type()
)
vaLicUUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaLicUUID.setStatus("current")
_VaLicMaxIoNode_Type = Integer32
_VaLicMaxIoNode_Object = MibScalar
vaLicMaxIoNode = _VaLicMaxIoNode_Object(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 1, 2, 8),
    _VaLicMaxIoNode_Type()
)
vaLicMaxIoNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaLicMaxIoNode.setStatus("current")
_VaLicMaxSnNode_Type = Integer32
_VaLicMaxSnNode_Object = MibScalar
vaLicMaxSnNode = _VaLicMaxSnNode_Object(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 1, 2, 9),
    _VaLicMaxSnNode_Type()
)
vaLicMaxSnNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaLicMaxSnNode.setStatus("current")
_VaLicMaxCapMBS_Type = Integer32
_VaLicMaxCapMBS_Object = MibScalar
vaLicMaxCapMBS = _VaLicMaxCapMBS_Object(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 1, 2, 10),
    _VaLicMaxCapMBS_Type()
)
vaLicMaxCapMBS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaLicMaxCapMBS.setStatus("current")


class _VaLicEpTypeLimit_Type(OctetString):
    """Custom type vaLicEpTypeLimit based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VaLicEpTypeLimit_Type.__name__ = "OctetString"
_VaLicEpTypeLimit_Object = MibScalar
vaLicEpTypeLimit = _VaLicEpTypeLimit_Object(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 1, 2, 11),
    _VaLicEpTypeLimit_Type()
)
vaLicEpTypeLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaLicEpTypeLimit.setStatus("current")


class _VaLicAppId_Type(OctetString):
    """Custom type vaLicAppId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VaLicAppId_Type.__name__ = "OctetString"
_VaLicAppId_Object = MibScalar
vaLicAppId = _VaLicAppId_Object(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 1, 2, 12),
    _VaLicAppId_Type()
)
vaLicAppId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaLicAppId.setStatus("current")


class _VaLicAppStats_Type(OctetString):
    """Custom type vaLicAppStats based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VaLicAppStats_Type.__name__ = "OctetString"
_VaLicAppStats_Object = MibScalar
vaLicAppStats = _VaLicAppStats_Object(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 1, 2, 13),
    _VaLicAppStats_Type()
)
vaLicAppStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaLicAppStats.setStatus("current")


class _VaLicAppCtrl_Type(OctetString):
    """Custom type vaLicAppCtrl based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VaLicAppCtrl_Type.__name__ = "OctetString"
_VaLicAppCtrl_Object = MibScalar
vaLicAppCtrl = _VaLicAppCtrl_Object(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 1, 2, 14),
    _VaLicAppCtrl_Type()
)
vaLicAppCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaLicAppCtrl.setStatus("current")


class _VaLicHA_Type(OctetString):
    """Custom type vaLicHA based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VaLicHA_Type.__name__ = "OctetString"
_VaLicHA_Object = MibScalar
vaLicHA = _VaLicHA_Object(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 1, 2, 15),
    _VaLicHA_Type()
)
vaLicHA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaLicHA.setStatus("current")


class _VaLicSecPack_Type(OctetString):
    """Custom type vaLicSecPack based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VaLicSecPack_Type.__name__ = "OctetString"
_VaLicSecPack_Object = MibScalar
vaLicSecPack = _VaLicSecPack_Object(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 1, 2, 16),
    _VaLicSecPack_Type()
)
vaLicSecPack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaLicSecPack.setStatus("current")
_VaLicVsysNum_Type = Integer32
_VaLicVsysNum_Object = MibScalar
vaLicVsysNum = _VaLicVsysNum_Object(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 1, 2, 17),
    _VaLicVsysNum_Type()
)
vaLicVsysNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaLicVsysNum.setStatus("current")
_VaSystemUser_ObjectIdentity = ObjectIdentity
vaSystemUser = _VaSystemUser_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 1, 3)
)
_VaSystemLogin_ObjectIdentity = ObjectIdentity
vaSystemLogin = _VaSystemLogin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1, 1, 4)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VARMOUR-SYSTEM-MIB",
    **{"varmour-system": varmour_system,
       "vaSystem": vaSystem,
       "vaSysHostname": vaSysHostname,
       "vaSysFabIf": vaSysFabIf,
       "vaSysFabAddr": vaSysFabAddr,
       "vaSysMgmtIf": vaSysMgmtIf,
       "vaSysMgmtAddr": vaSysMgmtAddr,
       "vaSysMgmtGateway": vaSysMgmtGateway,
       "vaSysTime": vaSysTime,
       "vaSysUptime": vaSysUptime,
       "vaSysModel": vaSysModel,
       "vaSysSerialNum": vaSysSerialNum,
       "vaSysSwVer": vaSysSwVer,
       "vaSysBootDir": vaSysBootDir,
       "vaSysSecPack": vaSysSecPack,
       "vaSysDirSecret": vaSysDirSecret,
       "vaLicense": vaLicense,
       "vaLicWarning": vaLicWarning,
       "vaLicCustName": vaLicCustName,
       "vaLicSerialNum": vaLicSerialNum,
       "vaLicExpiration": vaLicExpiration,
       "vaLicSeatNum": vaLicSeatNum,
       "vaLicType": vaLicType,
       "vaLicUUID": vaLicUUID,
       "vaLicMaxIoNode": vaLicMaxIoNode,
       "vaLicMaxSnNode": vaLicMaxSnNode,
       "vaLicMaxCapMBS": vaLicMaxCapMBS,
       "vaLicEpTypeLimit": vaLicEpTypeLimit,
       "vaLicAppId": vaLicAppId,
       "vaLicAppStats": vaLicAppStats,
       "vaLicAppCtrl": vaLicAppCtrl,
       "vaLicHA": vaLicHA,
       "vaLicSecPack": vaLicSecPack,
       "vaLicVsysNum": vaLicVsysNum,
       "vaSystemUser": vaSystemUser,
       "vaSystemLogin": vaSystemLogin}
)
