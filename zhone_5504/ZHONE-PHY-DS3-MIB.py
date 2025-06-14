# SNMP MIB module (ZHONE-PHY-DS3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/zhone_5504/ZHONE-PHY-DS3-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 18:11:11 2025
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

(dsx3ConfigEntry,) = mibBuilder.importSymbols(
    "DS3-MIB",
    "dsx3ConfigEntry")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")

(zhoneDs3Ext,
 zhoneModules) = mibBuilder.importSymbols(
    "Zhone",
    "zhoneDs3Ext",
    "zhoneModules")


# MODULE-IDENTITY

phyDs3 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 6, 17)
)
if mibBuilder.loadTexts:
    phyDs3.setRevisions(
        ("2001-05-14 14:35",
         "2001-04-25 14:25",
         "2001-03-15 08:34")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dsx3ConfigExtTable_Object = MibTable
dsx3ConfigExtTable = _Dsx3ConfigExtTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 10, 2)
)
if mibBuilder.loadTexts:
    dsx3ConfigExtTable.setStatus("current")
_Dsx3ConfigExtEntry_Object = MibTableRow
dsx3ConfigExtEntry = _Dsx3ConfigExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 10, 2, 1)
)
if mibBuilder.loadTexts:
    dsx3ConfigExtEntry.setStatus("current")


class _Dsx3ConfigExtScrambleEnabled_Type(TruthValue):
    """Custom type dsx3ConfigExtScrambleEnabled based on TruthValue"""
    defaultValue = 1


_Dsx3ConfigExtScrambleEnabled_Type.__name__ = "TruthValue"
_Dsx3ConfigExtScrambleEnabled_Object = MibTableColumn
dsx3ConfigExtScrambleEnabled = _Dsx3ConfigExtScrambleEnabled_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 10, 2, 1, 1),
    _Dsx3ConfigExtScrambleEnabled_Type()
)
dsx3ConfigExtScrambleEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3ConfigExtScrambleEnabled.setStatus("current")


class _Dsx3ConfigExtE3Framing_Type(Integer32):
    """Custom type dsx3ConfigExtE3Framing based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("e3FrameOther", 1),
          ("e3FrameG832", 2),
          ("e3FrameG751", 3))
    )


_Dsx3ConfigExtE3Framing_Type.__name__ = "Integer32"
_Dsx3ConfigExtE3Framing_Object = MibTableColumn
dsx3ConfigExtE3Framing = _Dsx3ConfigExtE3Framing_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 10, 2, 1, 2),
    _Dsx3ConfigExtE3Framing_Type()
)
dsx3ConfigExtE3Framing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3ConfigExtE3Framing.setStatus("current")


class _Dsx3ConfigExtAtmFraming_Type(Integer32):
    """Custom type dsx3ConfigExtAtmFraming based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dsx3AtmFramingOther", 1),
          ("dsx3AtmFramingPLCP", 2),
          ("dsx3AtmFramingDirectCellMapped", 3))
    )


_Dsx3ConfigExtAtmFraming_Type.__name__ = "Integer32"
_Dsx3ConfigExtAtmFraming_Object = MibTableColumn
dsx3ConfigExtAtmFraming = _Dsx3ConfigExtAtmFraming_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 10, 2, 1, 3),
    _Dsx3ConfigExtAtmFraming_Type()
)
dsx3ConfigExtAtmFraming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3ConfigExtAtmFraming.setStatus("current")
dsx3ConfigEntry.registerAugmentions(
    ("ZHONE-PHY-DS3-MIB",
     "dsx3ConfigExtEntry")
)
dsx3ConfigExtEntry.setIndexNames(*dsx3ConfigEntry.getIndexNames())

# Managed Objects groups

dsx3ConfigExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 5, 10, 1)
)
dsx3ConfigExtGroup.setObjects(
      *(("ZHONE-PHY-DS3-MIB", "dsx3ConfigExtScrambleEnabled"),
        ("ZHONE-PHY-DS3-MIB", "dsx3ConfigExtE3Framing"),
        ("ZHONE-PHY-DS3-MIB", "dsx3ConfigExtAtmFraming"))
)
if mibBuilder.loadTexts:
    dsx3ConfigExtGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZHONE-PHY-DS3-MIB",
    **{"dsx3ConfigExtGroup": dsx3ConfigExtGroup,
       "dsx3ConfigExtTable": dsx3ConfigExtTable,
       "dsx3ConfigExtEntry": dsx3ConfigExtEntry,
       "dsx3ConfigExtScrambleEnabled": dsx3ConfigExtScrambleEnabled,
       "dsx3ConfigExtE3Framing": dsx3ConfigExtE3Framing,
       "dsx3ConfigExtAtmFraming": dsx3ConfigExtAtmFraming,
       "phyDs3": phyDs3}
)
