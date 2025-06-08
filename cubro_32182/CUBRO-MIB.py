# SNMP MIB module (CUBRO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cubro_32182/CUBRO-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 10:58:58 2025
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

cubro_MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 32182)
)
if mibBuilder.loadTexts:
    cubro_MIB.setRevisions(
        ("2016-10-18 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PSUIndex(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



# MIB Managed Objects in the order of their OIDs

_PacketmasterEX_ObjectIdentity = ObjectIdentity
packetmasterEX = _PacketmasterEX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32182, 1)
)
_Environment_ObjectIdentity = ObjectIdentity
environment = _Environment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32182, 1, 1)
)
_PsuTable_Object = MibTable
psuTable = _PsuTable_Object(
    (1, 3, 6, 1, 4, 1, 32182, 1, 1, 1)
)
if mibBuilder.loadTexts:
    psuTable.setStatus("current")
_PsuEntry_Type = PSUIndex
_PsuEntry_Object = MibScalar
psuEntry = _PsuEntry_Object(
    (1, 3, 6, 1, 4, 1, 32182, 1, 1, 1, 1),
    _PsuEntry_Type()
)
psuEntry.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    psuEntry.setStatus("current")
_PsuIndex_Type = PSUIndex
_PsuIndex_Object = MibTableColumn
psuIndex = _PsuIndex_Object(
    (1, 3, 6, 1, 4, 1, 32182, 1, 1, 1, 1, 1),
    _PsuIndex_Type()
)
psuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psuIndex.setStatus("current")


class _PsuPresent_Type(DisplayString):
    """Custom type psuPresent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PsuPresent_Type.__name__ = "DisplayString"
_PsuPresent_Object = MibTableColumn
psuPresent = _PsuPresent_Object(
    (1, 3, 6, 1, 4, 1, 32182, 1, 1, 1, 1, 2),
    _PsuPresent_Type()
)
psuPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psuPresent.setStatus("current")


class _PsuPower_Type(DisplayString):
    """Custom type psuPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PsuPower_Type.__name__ = "DisplayString"
_PsuPower_Object = MibTableColumn
psuPower = _PsuPower_Object(
    (1, 3, 6, 1, 4, 1, 32182, 1, 1, 1, 1, 3),
    _PsuPower_Type()
)
psuPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psuPower.setStatus("current")


class _PsuType_Type(DisplayString):
    """Custom type psuType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PsuType_Type.__name__ = "DisplayString"
_PsuType_Object = MibTableColumn
psuType = _PsuType_Object(
    (1, 3, 6, 1, 4, 1, 32182, 1, 1, 1, 1, 4),
    _PsuType_Type()
)
psuType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psuType.setStatus("current")


class _PsuAlert_Type(DisplayString):
    """Custom type psuAlert based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PsuAlert_Type.__name__ = "DisplayString"
_PsuAlert_Object = MibTableColumn
psuAlert = _PsuAlert_Object(
    (1, 3, 6, 1, 4, 1, 32182, 1, 1, 1, 1, 5),
    _PsuAlert_Type()
)
psuAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psuAlert.setStatus("current")
_EnvConformance_ObjectIdentity = ObjectIdentity
envConformance = _EnvConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32182, 1, 2)
)

# Managed Objects groups

psuInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 32182, 1, 2, 2)
)
psuInfoGroup.setObjects(
      *(("CUBRO-MIB", "psuIndex"),
        ("CUBRO-MIB", "psuPresent"),
        ("CUBRO-MIB", "psuPower"),
        ("CUBRO-MIB", "psuType"),
        ("CUBRO-MIB", "psuAlert"))
)
if mibBuilder.loadTexts:
    psuInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CUBRO-MIB",
    **{"PSUIndex": PSUIndex,
       "cubro-MIB": cubro_MIB,
       "packetmasterEX": packetmasterEX,
       "environment": environment,
       "psuTable": psuTable,
       "psuEntry": psuEntry,
       "psuIndex": psuIndex,
       "psuPresent": psuPresent,
       "psuPower": psuPower,
       "psuType": psuType,
       "psuAlert": psuAlert,
       "envConformance": envConformance,
       "psuInfoGroup": psuInfoGroup}
)
