# SNMP MIB module (FIREBRICK-GLOBAL) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/firebrick_24693/FIREBRICK-GLOBAL.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 23:00:30 2025
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

(firebrickNewStyle,) = mibBuilder.importSymbols(
    "FIREBRICK-MIB",
    "firebrickNewStyle")

(TextualConvention,) = mibBuilder.importSymbols(
    "RFC1155-SMI",
    "TextualConvention")

(Gauge32,
 ModuleCompliance,
 ModuleIdentity,
 NotificationGroup,
 NotificationType,
 ObjectGroup,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "Gauge32",
    "ModuleCompliance",
    "ModuleIdentity",
    "NotificationGroup",
    "NotificationType",
    "ObjectGroup",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn")

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

fbGlobalMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 24693, 100, 4)
)
if mibBuilder.loadTexts:
    fbGlobalMib.setRevisions(
        ("2023-07-03 00:00",
         "2023-02-17 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FbGlobalMemory_ObjectIdentity = ObjectIdentity
fbGlobalMemory = _FbGlobalMemory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24693, 100, 4, 1)
)
_FbTotalMem_Type = Gauge32
_FbTotalMem_Object = MibScalar
fbTotalMem = _FbTotalMem_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 4, 1, 1),
    _FbTotalMem_Type()
)
fbTotalMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbTotalMem.setStatus("current")
_FbFreeMem_Type = Gauge32
_FbFreeMem_Object = MibScalar
fbFreeMem = _FbFreeMem_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 4, 1, 2),
    _FbFreeMem_Type()
)
fbFreeMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbFreeMem.setStatus("current")
_FbGlobalBuffers_ObjectIdentity = ObjectIdentity
fbGlobalBuffers = _FbGlobalBuffers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24693, 100, 4, 2)
)
_FbFreeBuffers_Type = Gauge32
_FbFreeBuffers_Object = MibScalar
fbFreeBuffers = _FbFreeBuffers_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 4, 2, 1),
    _FbFreeBuffers_Type()
)
fbFreeBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbFreeBuffers.setStatus("current")
_FbFreeLargeBuffers_Type = Gauge32
_FbFreeLargeBuffers_Object = MibScalar
fbFreeLargeBuffers = _FbFreeLargeBuffers_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 4, 2, 2),
    _FbFreeLargeBuffers_Type()
)
fbFreeLargeBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbFreeLargeBuffers.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FIREBRICK-GLOBAL",
    **{"fbGlobalMib": fbGlobalMib,
       "fbGlobalMemory": fbGlobalMemory,
       "fbTotalMem": fbTotalMem,
       "fbFreeMem": fbFreeMem,
       "fbGlobalBuffers": fbGlobalBuffers,
       "fbFreeBuffers": fbFreeBuffers,
       "fbFreeLargeBuffers": fbFreeLargeBuffers}
)
