# SNMP MIB module (CISCO-LWAPP-TRUSTSEC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-LWAPP-TRUSTSEC-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:55:06 2025
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

(cLApSysMacAddress,) = mibBuilder.importSymbols(
    "CISCO-LWAPP-AP-MIB",
    "cLApSysMacAddress")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CtsSecurityGroupTag,) = mibBuilder.importSymbols(
    "CISCO-TRUSTSEC-TC-MIB",
    "CtsSecurityGroupTag")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoLwappTrustSecMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 836)
)
if mibBuilder.loadTexts:
    ciscoLwappTrustSecMIB.setRevisions(
        ("2017-02-10 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ClCtsMIBNotifs_ObjectIdentity = ObjectIdentity
clCtsMIBNotifs = _ClCtsMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 836, 0)
)
_ClCtsTableMIBObjects_ObjectIdentity = ObjectIdentity
clCtsTableMIBObjects = _ClCtsTableMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 836, 1)
)
_ClCtsApSxpPeerTable_Object = MibTable
clCtsApSxpPeerTable = _ClCtsApSxpPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 836, 1, 1)
)
if mibBuilder.loadTexts:
    clCtsApSxpPeerTable.setStatus("current")
_CLCtsApSxpPeerEntry_Object = MibTableRow
cLCtsApSxpPeerEntry = _CLCtsApSxpPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 836, 1, 1, 1)
)
cLCtsApSxpPeerEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
    (0, "CISCO-LWAPP-TRUSTSEC-MIB", "clCtsApSxpPeerIpType"),
    (0, "CISCO-LWAPP-TRUSTSEC-MIB", "clCtsApSxpPeerIp"),
)
if mibBuilder.loadTexts:
    cLCtsApSxpPeerEntry.setStatus("current")
_ClCtsApSxpPeerIpType_Type = InetAddressType
_ClCtsApSxpPeerIpType_Object = MibTableColumn
clCtsApSxpPeerIpType = _ClCtsApSxpPeerIpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 836, 1, 1, 1, 1),
    _ClCtsApSxpPeerIpType_Type()
)
clCtsApSxpPeerIpType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clCtsApSxpPeerIpType.setStatus("current")
_ClCtsApSxpPeerIp_Type = InetAddress
_ClCtsApSxpPeerIp_Object = MibTableColumn
clCtsApSxpPeerIp = _ClCtsApSxpPeerIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 836, 1, 1, 1, 2),
    _ClCtsApSxpPeerIp_Type()
)
clCtsApSxpPeerIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clCtsApSxpPeerIp.setStatus("current")


class _ClCtsApSxpMode_Type(Integer32):
    """Custom type clCtsApSxpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("speaker", 1),
          ("listener", 2),
          ("both", 3))
    )


_ClCtsApSxpMode_Type.__name__ = "Integer32"
_ClCtsApSxpMode_Object = MibTableColumn
clCtsApSxpMode = _ClCtsApSxpMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 836, 1, 1, 1, 3),
    _ClCtsApSxpMode_Type()
)
clCtsApSxpMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clCtsApSxpMode.setStatus("current")


class _ClCtsApSxpPeerPassword_Type(Integer32):
    """Custom type clCtsApSxpPeerPassword based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notRequired", 0),
          ("required", 1),
          ("default", 2))
    )


_ClCtsApSxpPeerPassword_Type.__name__ = "Integer32"
_ClCtsApSxpPeerPassword_Object = MibTableColumn
clCtsApSxpPeerPassword = _ClCtsApSxpPeerPassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 836, 1, 1, 1, 4),
    _ClCtsApSxpPeerPassword_Type()
)
clCtsApSxpPeerPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clCtsApSxpPeerPassword.setStatus("current")
_ClCtsApSxpPeerRowStatus_Type = RowStatus
_ClCtsApSxpPeerRowStatus_Object = MibTableColumn
clCtsApSxpPeerRowStatus = _ClCtsApSxpPeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 836, 1, 1, 1, 5),
    _ClCtsApSxpPeerRowStatus_Type()
)
clCtsApSxpPeerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clCtsApSxpPeerRowStatus.setStatus("current")
_ClCtsMIBConform_ObjectIdentity = ObjectIdentity
clCtsMIBConform = _ClCtsMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 836, 2)
)
_ClCtsMIBCompliances_ObjectIdentity = ObjectIdentity
clCtsMIBCompliances = _ClCtsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 836, 2, 1)
)
_ClCtsMIBGroups_ObjectIdentity = ObjectIdentity
clCtsMIBGroups = _ClCtsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 836, 2, 2)
)
_ClCtsGlobalMIBObjects_ObjectIdentity = ObjectIdentity
clCtsGlobalMIBObjects = _ClCtsGlobalMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 836, 3)
)


class _ClCtsSecurityGroupTagId_Type(CtsSecurityGroupTag):
    """Custom type clCtsSecurityGroupTagId based on CtsSecurityGroupTag"""
    defaultValue = 0


_ClCtsSecurityGroupTagId_Type.__name__ = "CtsSecurityGroupTag"
_ClCtsSecurityGroupTagId_Object = MibScalar
clCtsSecurityGroupTagId = _ClCtsSecurityGroupTagId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 836, 3, 1),
    _ClCtsSecurityGroupTagId_Type()
)
clCtsSecurityGroupTagId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clCtsSecurityGroupTagId.setStatus("current")


class _ClCtsDeviceId_Type(SnmpAdminString):
    """Custom type clCtsDeviceId based on SnmpAdminString"""
    defaultValue = OctetString(" ")


_ClCtsDeviceId_Type.__name__ = "SnmpAdminString"
_ClCtsDeviceId_Object = MibScalar
clCtsDeviceId = _ClCtsDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 836, 3, 2),
    _ClCtsDeviceId_Type()
)
clCtsDeviceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clCtsDeviceId.setStatus("current")


class _ClCtsDevicePassword_Type(SnmpAdminString):
    """Custom type clCtsDevicePassword based on SnmpAdminString"""
    defaultValue = OctetString("")


_ClCtsDevicePassword_Type.__name__ = "SnmpAdminString"
_ClCtsDevicePassword_Object = MibScalar
clCtsDevicePassword = _ClCtsDevicePassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 836, 3, 3),
    _ClCtsDevicePassword_Type()
)
clCtsDevicePassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clCtsDevicePassword.setStatus("current")


class _ClCtsInlineTagEnableStatus_Type(TruthValue):
    """Custom type clCtsInlineTagEnableStatus based on TruthValue"""
    defaultValue = 2


_ClCtsInlineTagEnableStatus_Type.__name__ = "TruthValue"
_ClCtsInlineTagEnableStatus_Object = MibScalar
clCtsInlineTagEnableStatus = _ClCtsInlineTagEnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 836, 3, 4),
    _ClCtsInlineTagEnableStatus_Type()
)
clCtsInlineTagEnableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clCtsInlineTagEnableStatus.setStatus("current")


class _ClCtsEnableStatus_Type(TruthValue):
    """Custom type clCtsEnableStatus based on TruthValue"""
    defaultValue = 2


_ClCtsEnableStatus_Type.__name__ = "TruthValue"
_ClCtsEnableStatus_Object = MibScalar
clCtsEnableStatus = _ClCtsEnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 836, 3, 6),
    _ClCtsEnableStatus_Type()
)
clCtsEnableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clCtsEnableStatus.setStatus("current")

# Managed Objects groups

clCtsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 836, 2, 2, 1)
)
clCtsGroup.setObjects(
      *(("CISCO-LWAPP-TRUSTSEC-MIB", "clCtsSecurityGroupTagId"),
        ("CISCO-LWAPP-TRUSTSEC-MIB", "clCtsDeviceId"),
        ("CISCO-LWAPP-TRUSTSEC-MIB", "clCtsDevicePassword"),
        ("CISCO-LWAPP-TRUSTSEC-MIB", "clCtsInlineTagEnableStatus"),
        ("CISCO-LWAPP-TRUSTSEC-MIB", "clCtsEnableStatus"),
        ("CISCO-LWAPP-TRUSTSEC-MIB", "clCtsApSxpPeerIpType"),
        ("CISCO-LWAPP-TRUSTSEC-MIB", "clCtsApSxpPeerIp"),
        ("CISCO-LWAPP-TRUSTSEC-MIB", "clCtsApSxpPeerPassword"),
        ("CISCO-LWAPP-TRUSTSEC-MIB", "clCtsApSxpMode"),
        ("CISCO-LWAPP-TRUSTSEC-MIB", "clCtsApSxpPeerRowStatus"))
)
if mibBuilder.loadTexts:
    clCtsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

clCtsMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 836, 2, 1, 1)
)
clCtsMIBCompliance.setObjects(
    ("CISCO-LWAPP-TRUSTSEC-MIB", "clCtsGroup")
)
if mibBuilder.loadTexts:
    clCtsMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LWAPP-TRUSTSEC-MIB",
    **{"ciscoLwappTrustSecMIB": ciscoLwappTrustSecMIB,
       "clCtsMIBNotifs": clCtsMIBNotifs,
       "clCtsTableMIBObjects": clCtsTableMIBObjects,
       "clCtsApSxpPeerTable": clCtsApSxpPeerTable,
       "cLCtsApSxpPeerEntry": cLCtsApSxpPeerEntry,
       "clCtsApSxpPeerIpType": clCtsApSxpPeerIpType,
       "clCtsApSxpPeerIp": clCtsApSxpPeerIp,
       "clCtsApSxpMode": clCtsApSxpMode,
       "clCtsApSxpPeerPassword": clCtsApSxpPeerPassword,
       "clCtsApSxpPeerRowStatus": clCtsApSxpPeerRowStatus,
       "clCtsMIBConform": clCtsMIBConform,
       "clCtsMIBCompliances": clCtsMIBCompliances,
       "clCtsMIBCompliance": clCtsMIBCompliance,
       "clCtsMIBGroups": clCtsMIBGroups,
       "clCtsGroup": clCtsGroup,
       "clCtsGlobalMIBObjects": clCtsGlobalMIBObjects,
       "clCtsSecurityGroupTagId": clCtsSecurityGroupTagId,
       "clCtsDeviceId": clCtsDeviceId,
       "clCtsDevicePassword": clCtsDevicePassword,
       "clCtsInlineTagEnableStatus": clCtsInlineTagEnableStatus,
       "clCtsEnableStatus": clCtsEnableStatus}
)
