# SNMP MIB module (JUNIPER-MOBILE-GATEWAYS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/juniper_2636/JUNIPER-MOBILE-GATEWAYS.mib
# Produced by pysmi-1.5.11 at Sat May 31 15:28:20 2025
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
 InetAddressPrefixLength,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetPortNumber")

(Ipv6Address,
 Ipv6AddressIfIdentifier,
 Ipv6AddressPrefix) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address",
    "Ipv6AddressIfIdentifier",
    "Ipv6AddressPrefix")

(EnabledStatus,) = mibBuilder.importSymbols(
    "JUNIPER-MIMSTP-MIB",
    "EnabledStatus")

(jnxMobileGatewayMibRoot,) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxMobileGatewayMibRoot")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

jnxMobileGateways = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 4)
)
if mibBuilder.loadTexts:
    jnxMobileGateways.setRevisions(
        ("2011-01-03 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxMbgGwIndexTable_Object = MibTable
jnxMbgGwIndexTable = _JnxMbgGwIndexTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 4, 1)
)
if mibBuilder.loadTexts:
    jnxMbgGwIndexTable.setStatus("current")
_JnxMbgGwIndexEntry_Object = MibTableRow
jnxMbgGwIndexEntry = _JnxMbgGwIndexEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 4, 1, 1)
)
jnxMbgGwIndexEntry.setIndexNames(
    (0, "JUNIPER-MOBILE-GATEWAYS", "jnxMbgGwIndex"),
)
if mibBuilder.loadTexts:
    jnxMbgGwIndexEntry.setStatus("current")
_JnxMbgGwIndex_Type = Unsigned32
_JnxMbgGwIndex_Object = MibTableColumn
jnxMbgGwIndex = _JnxMbgGwIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 4, 1, 1, 1),
    _JnxMbgGwIndex_Type()
)
jnxMbgGwIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgGwIndex.setStatus("current")
_JnxMbgGwName_Type = DisplayString
_JnxMbgGwName_Object = MibTableColumn
jnxMbgGwName = _JnxMbgGwName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 4, 1, 1, 2),
    _JnxMbgGwName_Type()
)
jnxMbgGwName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgGwName.setStatus("current")
_JnxMbgGwType_Type = DisplayString
_JnxMbgGwType_Object = MibTableColumn
jnxMbgGwType = _JnxMbgGwType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 4, 1, 1, 3),
    _JnxMbgGwType_Type()
)
jnxMbgGwType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgGwType.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-MOBILE-GATEWAYS",
    **{"jnxMobileGateways": jnxMobileGateways,
       "jnxMbgGwIndexTable": jnxMbgGwIndexTable,
       "jnxMbgGwIndexEntry": jnxMbgGwIndexEntry,
       "jnxMbgGwIndex": jnxMbgGwIndex,
       "jnxMbgGwName": jnxMbgGwName,
       "jnxMbgGwType": jnxMbgGwType}
)
