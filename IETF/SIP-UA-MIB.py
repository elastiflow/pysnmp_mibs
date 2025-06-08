# SNMP MIB module (SIP-UA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/Standards/IETF/SIP-UA-MIB.mib
# Produced by pysmi-1.5.11 at Wed May 21 15:01:16 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(applIndex,) = mibBuilder.importSymbols(
    "NETWORK-SERVICES-MIB",
    "applIndex")

(SipTCEntityRole,) = mibBuilder.importSymbols(
    "SIP-TC-MIB",
    "SipTCEntityRole")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

sipUAMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 150)
)
if mibBuilder.loadTexts:
    sipUAMIB.setRevisions(
        ("2007-04-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SipUAMIBObjects_ObjectIdentity = ObjectIdentity
sipUAMIBObjects = _SipUAMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 150, 1)
)
_SipUACfgServer_ObjectIdentity = ObjectIdentity
sipUACfgServer = _SipUACfgServer_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 150, 1, 1)
)
_SipUACfgServerTable_Object = MibTable
sipUACfgServerTable = _SipUACfgServerTable_Object(
    (1, 3, 6, 1, 2, 1, 150, 1, 1, 1)
)
if mibBuilder.loadTexts:
    sipUACfgServerTable.setStatus("current")
_SipUACfgServerEntry_Object = MibTableRow
sipUACfgServerEntry = _SipUACfgServerEntry_Object(
    (1, 3, 6, 1, 2, 1, 150, 1, 1, 1, 1)
)
sipUACfgServerEntry.setIndexNames(
    (0, "NETWORK-SERVICES-MIB", "applIndex"),
    (0, "SIP-UA-MIB", "sipUACfgServerIndex"),
)
if mibBuilder.loadTexts:
    sipUACfgServerEntry.setStatus("current")


class _SipUACfgServerIndex_Type(Unsigned32):
    """Custom type sipUACfgServerIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_SipUACfgServerIndex_Type.__name__ = "Unsigned32"
_SipUACfgServerIndex_Object = MibTableColumn
sipUACfgServerIndex = _SipUACfgServerIndex_Object(
    (1, 3, 6, 1, 2, 1, 150, 1, 1, 1, 1, 1),
    _SipUACfgServerIndex_Type()
)
sipUACfgServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sipUACfgServerIndex.setStatus("current")
_SipUACfgServerAddressType_Type = InetAddressType
_SipUACfgServerAddressType_Object = MibTableColumn
sipUACfgServerAddressType = _SipUACfgServerAddressType_Object(
    (1, 3, 6, 1, 2, 1, 150, 1, 1, 1, 1, 2),
    _SipUACfgServerAddressType_Type()
)
sipUACfgServerAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipUACfgServerAddressType.setStatus("current")
_SipUACfgServerAddress_Type = InetAddress
_SipUACfgServerAddress_Object = MibTableColumn
sipUACfgServerAddress = _SipUACfgServerAddress_Object(
    (1, 3, 6, 1, 2, 1, 150, 1, 1, 1, 1, 3),
    _SipUACfgServerAddress_Type()
)
sipUACfgServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipUACfgServerAddress.setStatus("current")
_SipUACfgServerRole_Type = SipTCEntityRole
_SipUACfgServerRole_Object = MibTableColumn
sipUACfgServerRole = _SipUACfgServerRole_Object(
    (1, 3, 6, 1, 2, 1, 150, 1, 1, 1, 1, 4),
    _SipUACfgServerRole_Type()
)
sipUACfgServerRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipUACfgServerRole.setStatus("current")
_SipUAMIBConformance_ObjectIdentity = ObjectIdentity
sipUAMIBConformance = _SipUAMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 150, 2)
)
_SipUAMIBCompliances_ObjectIdentity = ObjectIdentity
sipUAMIBCompliances = _SipUAMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 150, 2, 1)
)
_SipUAMIBGroups_ObjectIdentity = ObjectIdentity
sipUAMIBGroups = _SipUAMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 150, 2, 2)
)

# Managed Objects groups

sipUAConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 150, 2, 2, 1)
)
sipUAConfigGroup.setObjects(
      *(("SIP-UA-MIB", "sipUACfgServerAddressType"),
        ("SIP-UA-MIB", "sipUACfgServerAddress"),
        ("SIP-UA-MIB", "sipUACfgServerRole"))
)
if mibBuilder.loadTexts:
    sipUAConfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

sipUACompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 150, 2, 1, 1)
)
sipUACompliance.setObjects(
    ("SIP-UA-MIB", "sipUAConfigGroup")
)
if mibBuilder.loadTexts:
    sipUACompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SIP-UA-MIB",
    **{"sipUAMIB": sipUAMIB,
       "sipUAMIBObjects": sipUAMIBObjects,
       "sipUACfgServer": sipUACfgServer,
       "sipUACfgServerTable": sipUACfgServerTable,
       "sipUACfgServerEntry": sipUACfgServerEntry,
       "sipUACfgServerIndex": sipUACfgServerIndex,
       "sipUACfgServerAddressType": sipUACfgServerAddressType,
       "sipUACfgServerAddress": sipUACfgServerAddress,
       "sipUACfgServerRole": sipUACfgServerRole,
       "sipUAMIBConformance": sipUAMIBConformance,
       "sipUAMIBCompliances": sipUAMIBCompliances,
       "sipUACompliance": sipUACompliance,
       "sipUAMIBGroups": sipUAMIBGroups,
       "sipUAConfigGroup": sipUAConfigGroup}
)
