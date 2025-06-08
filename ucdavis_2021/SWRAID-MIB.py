# SNMP MIB module (SWRAID-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ucdavis_2021/SWRAID-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 19:49:14 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(ucdExperimental,) = mibBuilder.importSymbols(
    "UCD-SNMP-MIB",
    "ucdExperimental")


# MODULE-IDENTITY

swRaidMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2021, 13, 18)
)
if mibBuilder.loadTexts:
    swRaidMIB.setRevisions(
        ("2007-09-29 18:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class RaidStatusTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("active", 2),
          ("faulty", 3))
    )



# MIB Managed Objects in the order of their OIDs

_SwRaidTable_Object = MibTable
swRaidTable = _SwRaidTable_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 18, 1)
)
if mibBuilder.loadTexts:
    swRaidTable.setStatus("current")
_SwRaidEntry_Object = MibTableRow
swRaidEntry = _SwRaidEntry_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 18, 1, 1)
)
swRaidEntry.setIndexNames(
    (0, "SWRAID-MIB", "swRaidIndex"),
)
if mibBuilder.loadTexts:
    swRaidEntry.setStatus("current")


class _SwRaidIndex_Type(Integer32):
    """Custom type swRaidIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwRaidIndex_Type.__name__ = "Integer32"
_SwRaidIndex_Object = MibTableColumn
swRaidIndex = _SwRaidIndex_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 18, 1, 1, 1),
    _SwRaidIndex_Type()
)
swRaidIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRaidIndex.setStatus("current")
_SwRaidDevice_Type = DisplayString
_SwRaidDevice_Object = MibTableColumn
swRaidDevice = _SwRaidDevice_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 18, 1, 1, 2),
    _SwRaidDevice_Type()
)
swRaidDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRaidDevice.setStatus("current")
_SwRaidPersonality_Type = DisplayString
_SwRaidPersonality_Object = MibTableColumn
swRaidPersonality = _SwRaidPersonality_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 18, 1, 1, 3),
    _SwRaidPersonality_Type()
)
swRaidPersonality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRaidPersonality.setStatus("current")
_SwRaidUnits_Type = DisplayString
_SwRaidUnits_Object = MibTableColumn
swRaidUnits = _SwRaidUnits_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 18, 1, 1, 4),
    _SwRaidUnits_Type()
)
swRaidUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRaidUnits.setStatus("current")
_SwRaidUnitCount_Type = Integer32
_SwRaidUnitCount_Object = MibTableColumn
swRaidUnitCount = _SwRaidUnitCount_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 18, 1, 1, 5),
    _SwRaidUnitCount_Type()
)
swRaidUnitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRaidUnitCount.setStatus("current")
_SwRaidStatus_Type = RaidStatusTC
_SwRaidStatus_Object = MibTableColumn
swRaidStatus = _SwRaidStatus_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 18, 1, 1, 6),
    _SwRaidStatus_Type()
)
swRaidStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRaidStatus.setStatus("current")
_SwRaidErrorFlag_Type = Integer32
_SwRaidErrorFlag_Object = MibScalar
swRaidErrorFlag = _SwRaidErrorFlag_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 18, 100),
    _SwRaidErrorFlag_Type()
)
swRaidErrorFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRaidErrorFlag.setStatus("current")
_SwRaidErrMessage_Type = DisplayString
_SwRaidErrMessage_Object = MibScalar
swRaidErrMessage = _SwRaidErrMessage_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 18, 101),
    _SwRaidErrMessage_Type()
)
swRaidErrMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRaidErrMessage.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SWRAID-MIB",
    **{"RaidStatusTC": RaidStatusTC,
       "swRaidMIB": swRaidMIB,
       "swRaidTable": swRaidTable,
       "swRaidEntry": swRaidEntry,
       "swRaidIndex": swRaidIndex,
       "swRaidDevice": swRaidDevice,
       "swRaidPersonality": swRaidPersonality,
       "swRaidUnits": swRaidUnits,
       "swRaidUnitCount": swRaidUnitCount,
       "swRaidStatus": swRaidStatus,
       "swRaidErrorFlag": swRaidErrorFlag,
       "swRaidErrMessage": swRaidErrMessage}
)
