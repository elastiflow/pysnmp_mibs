# SNMP MIB module (BELAIR-MAU) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ericsson_15768/BELAIR-MAU.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 16:08:43 2025
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

(belairInterfaces,) = mibBuilder.importSymbols(
    "BELAIR-SMI",
    "belairInterfaces")

(BelAirAdminState,) = mibBuilder.importSymbols(
    "BELAIR-TC",
    "BelAirAdminState")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

belairMauMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 4, 5)
)
if mibBuilder.loadTexts:
    belairMauMib.setRevisions(
        ("2005-12-13 09:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Speed(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tenMbps", 1),
          ("hundredMbps", 2))
    )



class Duplex(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fullDuplex", 1),
          ("halfDuplex", 2))
    )



# MIB Managed Objects in the order of their OIDs

_BelairMauObjects_ObjectIdentity = ObjectIdentity
belairMauObjects = _BelairMauObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 4, 5, 1)
)
_BelairIfMauTable_Object = MibTable
belairIfMauTable = _BelairIfMauTable_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 5, 1, 1)
)
if mibBuilder.loadTexts:
    belairIfMauTable.setStatus("current")
_BelairIfMauEntry_Object = MibTableRow
belairIfMauEntry = _BelairIfMauEntry_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 5, 1, 1, 1)
)
belairIfMauEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    belairIfMauEntry.setStatus("current")


class _BelairIfMauType_Type(Integer32):
    """Custom type belairIfMauType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("electrical", 1),
          ("singleMode", 2))
    )


_BelairIfMauType_Type.__name__ = "Integer32"
_BelairIfMauType_Object = MibTableColumn
belairIfMauType = _BelairIfMauType_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 5, 1, 1, 1, 1),
    _BelairIfMauType_Type()
)
belairIfMauType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairIfMauType.setStatus("current")


class _BelairIfMauSpeed_Type(Speed):
    """Custom type belairIfMauSpeed based on Speed"""
    defaultValue = 2


_BelairIfMauSpeed_Type.__name__ = "Speed"
_BelairIfMauSpeed_Object = MibTableColumn
belairIfMauSpeed = _BelairIfMauSpeed_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 5, 1, 1, 1, 2),
    _BelairIfMauSpeed_Type()
)
belairIfMauSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairIfMauSpeed.setStatus("current")


class _BelairIfMauMode_Type(Duplex):
    """Custom type belairIfMauMode based on Duplex"""
    defaultValue = 1


_BelairIfMauMode_Type.__name__ = "Duplex"
_BelairIfMauMode_Object = MibTableColumn
belairIfMauMode = _BelairIfMauMode_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 5, 1, 1, 1, 3),
    _BelairIfMauMode_Type()
)
belairIfMauMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairIfMauMode.setStatus("current")
_BelairIfMauAutoNeg_Type = BelAirAdminState
_BelairIfMauAutoNeg_Object = MibTableColumn
belairIfMauAutoNeg = _BelairIfMauAutoNeg_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 5, 1, 1, 1, 4),
    _BelairIfMauAutoNeg_Type()
)
belairIfMauAutoNeg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    belairIfMauAutoNeg.setStatus("current")
_BelairMauTrapObjects_ObjectIdentity = ObjectIdentity
belairMauTrapObjects = _BelairMauTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 4, 5, 2)
)
_BelairMauConformance_ObjectIdentity = ObjectIdentity
belairMauConformance = _BelairMauConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 4, 5, 3)
)

# Managed Objects groups

belairMauObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15768, 4, 5, 3, 1)
)
belairMauObjectGroup.setObjects(
      *(("BELAIR-MAU", "belairIfMauType"),
        ("BELAIR-MAU", "belairIfMauSpeed"),
        ("BELAIR-MAU", "belairIfMauMode"),
        ("BELAIR-MAU", "belairIfMauAutoNeg"))
)
if mibBuilder.loadTexts:
    belairMauObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BELAIR-MAU",
    **{"Speed": Speed,
       "Duplex": Duplex,
       "belairMauMib": belairMauMib,
       "belairMauObjects": belairMauObjects,
       "belairIfMauTable": belairIfMauTable,
       "belairIfMauEntry": belairIfMauEntry,
       "belairIfMauType": belairIfMauType,
       "belairIfMauSpeed": belairIfMauSpeed,
       "belairIfMauMode": belairIfMauMode,
       "belairIfMauAutoNeg": belairIfMauAutoNeg,
       "belairMauTrapObjects": belairMauTrapObjects,
       "belairMauConformance": belairMauConformance,
       "belairMauObjectGroup": belairMauObjectGroup}
)
