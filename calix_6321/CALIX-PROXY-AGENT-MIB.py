# SNMP MIB module (CALIX-PROXY-AGENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/calix_6321/CALIX-PROXY-AGENT-MIB.mib
# Produced by pysmi-1.6.1 at Tue Jun  3 17:18:56 2025
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

(calixManagement,
 calixModules) = mibBuilder.importSymbols(
    "CALIX-SMI",
    "calixManagement",
    "calixModules")

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

(DisplayString,
 NotificationType,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "NotificationType",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

calixSnmpProxy = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 1, 2)
)
if mibBuilder.loadTexts:
    calixSnmpProxy.setRevisions(
        ("2003-04-14 11:11",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CalixProxyAgentMIB_ObjectIdentity = ObjectIdentity
calixProxyAgentMIB = _CalixProxyAgentMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 2, 1)
)
_CalixDevice_ObjectIdentity = ObjectIdentity
calixDevice = _CalixDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 2, 1, 1)
)
_CalixDeviceTable_Object = MibTable
calixDeviceTable = _CalixDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    calixDeviceTable.setStatus("current")
_CalixDeviceEntry_Object = MibTableRow
calixDeviceEntry = _CalixDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 1, 1, 1, 1)
)
calixDeviceEntry.setIndexNames(
    (0, "CALIX-PROXY-AGENT-MIB", "calixDeviceIndex"),
)
if mibBuilder.loadTexts:
    calixDeviceEntry.setStatus("current")


class _CalixDeviceIndex_Type(Integer32):
    """Custom type calixDeviceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 250),
    )


_CalixDeviceIndex_Type.__name__ = "Integer32"
_CalixDeviceIndex_Object = MibTableColumn
calixDeviceIndex = _CalixDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 1, 1, 1, 1, 1),
    _CalixDeviceIndex_Type()
)
calixDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDeviceIndex.setStatus("current")


class _CalixDeviceName_Type(DisplayString):
    """Custom type calixDeviceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CalixDeviceName_Type.__name__ = "DisplayString"
_CalixDeviceName_Object = MibTableColumn
calixDeviceName = _CalixDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 1, 1, 1, 1, 2),
    _CalixDeviceName_Type()
)
calixDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDeviceName.setStatus("current")


class _CalixDeviceDescr_Type(DisplayString):
    """Custom type calixDeviceDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CalixDeviceDescr_Type.__name__ = "DisplayString"
_CalixDeviceDescr_Object = MibTableColumn
calixDeviceDescr = _CalixDeviceDescr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 1, 1, 1, 1, 3),
    _CalixDeviceDescr_Type()
)
calixDeviceDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDeviceDescr.setStatus("current")


class _CalixDeviceAssignedPort_Type(Integer32):
    """Custom type calixDeviceAssignedPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5000, 5250),
    )


_CalixDeviceAssignedPort_Type.__name__ = "Integer32"
_CalixDeviceAssignedPort_Object = MibTableColumn
calixDeviceAssignedPort = _CalixDeviceAssignedPort_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 1, 1, 1, 1, 4),
    _CalixDeviceAssignedPort_Type()
)
calixDeviceAssignedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDeviceAssignedPort.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CALIX-PROXY-AGENT-MIB",
    **{"calixSnmpProxy": calixSnmpProxy,
       "calixProxyAgentMIB": calixProxyAgentMIB,
       "calixDevice": calixDevice,
       "calixDeviceTable": calixDeviceTable,
       "calixDeviceEntry": calixDeviceEntry,
       "calixDeviceIndex": calixDeviceIndex,
       "calixDeviceName": calixDeviceName,
       "calixDeviceDescr": calixDeviceDescr,
       "calixDeviceAssignedPort": calixDeviceAssignedPort}
)
