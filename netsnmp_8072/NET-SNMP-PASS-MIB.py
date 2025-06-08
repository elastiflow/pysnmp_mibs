# SNMP MIB module (NET-SNMP-PASS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/netsnmp_8072/NET-SNMP-PASS-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 30 16:28:10 2025
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

(netSnmpExamples,) = mibBuilder.importSymbols(
    "NET-SNMP-EXAMPLES-MIB",
    "netSnmpExamples")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

netSnmpPassExamples = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 2, 255)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _NetSnmpPassString_Type(SnmpAdminString):
    """Custom type netSnmpPassString based on SnmpAdminString"""
    defaultValue = OctetString("Life, the Universe, and Everything")


_NetSnmpPassString_Type.__name__ = "SnmpAdminString"
_NetSnmpPassString_Object = MibScalar
netSnmpPassString = _NetSnmpPassString_Object(
    (1, 3, 6, 1, 4, 1, 8072, 2, 255, 1),
    _NetSnmpPassString_Type()
)
netSnmpPassString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netSnmpPassString.setStatus("current")
_NetSnmpPassTable_Object = MibTable
netSnmpPassTable = _NetSnmpPassTable_Object(
    (1, 3, 6, 1, 4, 1, 8072, 2, 255, 2)
)
if mibBuilder.loadTexts:
    netSnmpPassTable.setStatus("current")
_NetSnmpPassEntry_Object = MibTableRow
netSnmpPassEntry = _NetSnmpPassEntry_Object(
    (1, 3, 6, 1, 4, 1, 8072, 2, 255, 2, 1)
)
netSnmpPassEntry.setIndexNames(
    (0, "NET-SNMP-PASS-MIB", "netSnmpPassIndex"),
)
if mibBuilder.loadTexts:
    netSnmpPassEntry.setStatus("current")
_NetSnmpPassIndex_Type = Integer32
_NetSnmpPassIndex_Object = MibTableColumn
netSnmpPassIndex = _NetSnmpPassIndex_Object(
    (1, 3, 6, 1, 4, 1, 8072, 2, 255, 2, 1, 1),
    _NetSnmpPassIndex_Type()
)
netSnmpPassIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    netSnmpPassIndex.setStatus("current")


class _NetSnmpPassInteger_Type(Integer32):
    """Custom type netSnmpPassInteger based on Integer32"""
    defaultValue = 42


_NetSnmpPassInteger_Type.__name__ = "Integer32"
_NetSnmpPassInteger_Object = MibTableColumn
netSnmpPassInteger = _NetSnmpPassInteger_Object(
    (1, 3, 6, 1, 4, 1, 8072, 2, 255, 2, 1, 2),
    _NetSnmpPassInteger_Type()
)
netSnmpPassInteger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netSnmpPassInteger.setStatus("current")


class _NetSnmpPassOID_Type(ObjectIdentifier):
    """Custom type netSnmpPassOID based on ObjectIdentifier"""
    defaultValue = (1, 3, 6, 1, 4, 1, 8072, 2, 255, 99)


_NetSnmpPassOID_Type.__name__ = "ObjectIdentifier"
_NetSnmpPassOID_Object = MibTableColumn
netSnmpPassOID = _NetSnmpPassOID_Object(
    (1, 3, 6, 1, 4, 1, 8072, 2, 255, 2, 1, 3),
    _NetSnmpPassOID_Type()
)
netSnmpPassOID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netSnmpPassOID.setStatus("current")


class _NetSnmpPassTimeTicks_Type(TimeTicks):
    """Custom type netSnmpPassTimeTicks based on TimeTicks"""
    defaultValue = 363136200


_NetSnmpPassTimeTicks_Type.__name__ = "TimeTicks"
_NetSnmpPassTimeTicks_Object = MibScalar
netSnmpPassTimeTicks = _NetSnmpPassTimeTicks_Object(
    (1, 3, 6, 1, 4, 1, 8072, 2, 255, 3),
    _NetSnmpPassTimeTicks_Type()
)
netSnmpPassTimeTicks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netSnmpPassTimeTicks.setStatus("current")


class _NetSnmpPassIpAddress_Type(IpAddress):
    """Custom type netSnmpPassIpAddress based on IpAddress"""
    defaultHexValue = "7f000001"


_NetSnmpPassIpAddress_Type.__name__ = "IpAddress"
_NetSnmpPassIpAddress_Object = MibScalar
netSnmpPassIpAddress = _NetSnmpPassIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8072, 2, 255, 4),
    _NetSnmpPassIpAddress_Type()
)
netSnmpPassIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netSnmpPassIpAddress.setStatus("current")
_NetSnmpPassCounter_Type = Counter32
_NetSnmpPassCounter_Object = MibScalar
netSnmpPassCounter = _NetSnmpPassCounter_Object(
    (1, 3, 6, 1, 4, 1, 8072, 2, 255, 5),
    _NetSnmpPassCounter_Type()
)
netSnmpPassCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netSnmpPassCounter.setStatus("current")


class _NetSnmpPassGauge_Type(Gauge32):
    """Custom type netSnmpPassGauge based on Gauge32"""
    defaultValue = 42


_NetSnmpPassGauge_Type.__name__ = "Gauge32"
_NetSnmpPassGauge_Object = MibScalar
netSnmpPassGauge = _NetSnmpPassGauge_Object(
    (1, 3, 6, 1, 4, 1, 8072, 2, 255, 6),
    _NetSnmpPassGauge_Type()
)
netSnmpPassGauge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netSnmpPassGauge.setStatus("current")
_NetSnmpPassOIDValue_ObjectIdentity = ObjectIdentity
netSnmpPassOIDValue = _NetSnmpPassOIDValue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8072, 2, 255, 99)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NET-SNMP-PASS-MIB",
    **{"netSnmpPassExamples": netSnmpPassExamples,
       "netSnmpPassString": netSnmpPassString,
       "netSnmpPassTable": netSnmpPassTable,
       "netSnmpPassEntry": netSnmpPassEntry,
       "netSnmpPassIndex": netSnmpPassIndex,
       "netSnmpPassInteger": netSnmpPassInteger,
       "netSnmpPassOID": netSnmpPassOID,
       "netSnmpPassTimeTicks": netSnmpPassTimeTicks,
       "netSnmpPassIpAddress": netSnmpPassIpAddress,
       "netSnmpPassCounter": netSnmpPassCounter,
       "netSnmpPassGauge": netSnmpPassGauge,
       "netSnmpPassOIDValue": netSnmpPassOIDValue}
)
