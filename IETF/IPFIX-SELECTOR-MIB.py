# SNMP MIB module (IPFIX-SELECTOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/Standards/IETF/IPFIX-SELECTOR-MIB.mib
# Produced by pysmi-1.5.11 at Wed May 21 14:38:05 2025
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ipfixSelectorMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 194)
)
if mibBuilder.loadTexts:
    ipfixSelectorMIB.setRevisions(
        ("2012-06-11 00:00",
         "2010-03-15 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IpfixSelectorObjects_ObjectIdentity = ObjectIdentity
ipfixSelectorObjects = _IpfixSelectorObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 194, 1)
)
_IpfixSelectorFunctions_ObjectIdentity = ObjectIdentity
ipfixSelectorFunctions = _IpfixSelectorFunctions_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 194, 1, 1)
)
_IpfixFuncSelectAll_ObjectIdentity = ObjectIdentity
ipfixFuncSelectAll = _IpfixFuncSelectAll_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 194, 1, 1, 1)
)
_IpfixFuncSelectAllAvail_Type = TruthValue
_IpfixFuncSelectAllAvail_Object = MibScalar
ipfixFuncSelectAllAvail = _IpfixFuncSelectAllAvail_Object(
    (1, 3, 6, 1, 2, 1, 194, 1, 1, 1, 1),
    _IpfixFuncSelectAllAvail_Type()
)
ipfixFuncSelectAllAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixFuncSelectAllAvail.setStatus("current")
_IpfixSelectorConformance_ObjectIdentity = ObjectIdentity
ipfixSelectorConformance = _IpfixSelectorConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 194, 2)
)
_IpfixSelectorCompliances_ObjectIdentity = ObjectIdentity
ipfixSelectorCompliances = _IpfixSelectorCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 194, 2, 1)
)
_IpfixSelectorGroups_ObjectIdentity = ObjectIdentity
ipfixSelectorGroups = _IpfixSelectorGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 194, 2, 2)
)

# Managed Objects groups

ipfixSelectorBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 194, 2, 2, 1)
)
ipfixSelectorBasicGroup.setObjects(
    ("IPFIX-SELECTOR-MIB", "ipfixFuncSelectAllAvail")
)
if mibBuilder.loadTexts:
    ipfixSelectorBasicGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ipfixSelectorBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 194, 2, 1, 1)
)
ipfixSelectorBasicCompliance.setObjects(
    ("IPFIX-SELECTOR-MIB", "ipfixSelectorBasicGroup")
)
if mibBuilder.loadTexts:
    ipfixSelectorBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPFIX-SELECTOR-MIB",
    **{"ipfixSelectorMIB": ipfixSelectorMIB,
       "ipfixSelectorObjects": ipfixSelectorObjects,
       "ipfixSelectorFunctions": ipfixSelectorFunctions,
       "ipfixFuncSelectAll": ipfixFuncSelectAll,
       "ipfixFuncSelectAllAvail": ipfixFuncSelectAllAvail,
       "ipfixSelectorConformance": ipfixSelectorConformance,
       "ipfixSelectorCompliances": ipfixSelectorCompliances,
       "ipfixSelectorBasicCompliance": ipfixSelectorBasicCompliance,
       "ipfixSelectorGroups": ipfixSelectorGroups,
       "ipfixSelectorBasicGroup": ipfixSelectorBasicGroup}
)
