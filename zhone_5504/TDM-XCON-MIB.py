# SNMP MIB module (TDM-XCON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/zhone_5504/TDM-XCON-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 18:24:44 2025
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

(zhoneDsx,) = mibBuilder.importSymbols(
    "Zhone",
    "zhoneDsx")

(ZhoneRowStatus,) = mibBuilder.importSymbols(
    "Zhone-TC",
    "ZhoneRowStatus")


# MODULE-IDENTITY

zhoneTdmXconMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 11)
)
if mibBuilder.loadTexts:
    zhoneTdmXconMib.setRevisions(
        ("2000-09-12 13:33",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZhoneTdmXconTable_Object = MibTable
zhoneTdmXconTable = _ZhoneTdmXconTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 12)
)
if mibBuilder.loadTexts:
    zhoneTdmXconTable.setStatus("current")
_ZhoneTdmXconEntry_Object = MibTableRow
zhoneTdmXconEntry = _ZhoneTdmXconEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 12, 1)
)
zhoneTdmXconEntry.setIndexNames(
    (0, "TDM-XCON-MIB", "zhoneXconFromWanGroupID"),
    (0, "TDM-XCON-MIB", "zhoneXconFromTS"),
)
if mibBuilder.loadTexts:
    zhoneTdmXconEntry.setStatus("current")


class _ZhoneXconFromWanGroupID_Type(Integer32):
    """Custom type zhoneXconFromWanGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ZhoneXconFromWanGroupID_Type.__name__ = "Integer32"
_ZhoneXconFromWanGroupID_Object = MibTableColumn
zhoneXconFromWanGroupID = _ZhoneXconFromWanGroupID_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 12, 1, 1),
    _ZhoneXconFromWanGroupID_Type()
)
zhoneXconFromWanGroupID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneXconFromWanGroupID.setStatus("current")


class _ZhoneXconFromTS_Type(Integer32):
    """Custom type zhoneXconFromTS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_ZhoneXconFromTS_Type.__name__ = "Integer32"
_ZhoneXconFromTS_Object = MibTableColumn
zhoneXconFromTS = _ZhoneXconFromTS_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 12, 1, 2),
    _ZhoneXconFromTS_Type()
)
zhoneXconFromTS.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneXconFromTS.setStatus("current")


class _ZhoneXconType_Type(Integer32):
    """Custom type zhoneXconType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("voice", 2),
          ("dropAndInsert", 3),
          ("hdlc", 4),
          ("wan", 5),
          ("v35-56KInvertedClock", 6),
          ("v35-56KNormalClock", 7),
          ("v35-64KInvertedClock", 8),
          ("v35-64KNormalClock", 9),
          ("rs232ASync2400", 10),
          ("rs232ASync4800", 11),
          ("rs232ASync9600", 12),
          ("rs232Sync56K", 13),
          ("rs232Sync64K", 14),
          ("rs232ASync2400b5", 15),
          ("rs232ASync2400b10", 16),
          ("rs232ASync2400b20", 17),
          ("rs232ASync4800b5", 18),
          ("rs232ASync4800b10", 19),
          ("rs232ASync9600b5", 20),
          ("rs232Sync9600", 21),
          ("rs232Sync9600b5", 22))
    )


_ZhoneXconType_Type.__name__ = "Integer32"
_ZhoneXconType_Object = MibTableColumn
zhoneXconType = _ZhoneXconType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 12, 1, 3),
    _ZhoneXconType_Type()
)
zhoneXconType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneXconType.setStatus("current")


class _ZhoneXconToPortGroupID_Type(Integer32):
    """Custom type zhoneXconToPortGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ZhoneXconToPortGroupID_Type.__name__ = "Integer32"
_ZhoneXconToPortGroupID_Object = MibTableColumn
zhoneXconToPortGroupID = _ZhoneXconToPortGroupID_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 12, 1, 4),
    _ZhoneXconToPortGroupID_Type()
)
zhoneXconToPortGroupID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneXconToPortGroupID.setStatus("current")


class _ZhoneXconToTS_Type(Integer32):
    """Custom type zhoneXconToTS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_ZhoneXconToTS_Type.__name__ = "Integer32"
_ZhoneXconToTS_Object = MibTableColumn
zhoneXconToTS = _ZhoneXconToTS_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 12, 1, 5),
    _ZhoneXconToTS_Type()
)
zhoneXconToTS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneXconToTS.setStatus("current")


class _ZhoneXconHighway_Type(Integer32):
    """Custom type zhoneXconHighway based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("na", 1),
          ("busA", 2),
          ("busB", 3))
    )


_ZhoneXconHighway_Type.__name__ = "Integer32"
_ZhoneXconHighway_Object = MibTableColumn
zhoneXconHighway = _ZhoneXconHighway_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 12, 1, 6),
    _ZhoneXconHighway_Type()
)
zhoneXconHighway.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneXconHighway.setStatus("current")
_ZhoneXconRowStatus_Type = ZhoneRowStatus
_ZhoneXconRowStatus_Object = MibTableColumn
zhoneXconRowStatus = _ZhoneXconRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 12, 1, 7),
    _ZhoneXconRowStatus_Type()
)
zhoneXconRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneXconRowStatus.setStatus("current")

# Managed Objects groups

zhoneTdmXconObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 11, 1)
)
zhoneTdmXconObjectsGroup.setObjects(
      *(("TDM-XCON-MIB", "zhoneXconType"),
        ("TDM-XCON-MIB", "zhoneXconToPortGroupID"),
        ("TDM-XCON-MIB", "zhoneXconToTS"),
        ("TDM-XCON-MIB", "zhoneXconHighway"),
        ("TDM-XCON-MIB", "zhoneXconRowStatus"))
)
if mibBuilder.loadTexts:
    zhoneTdmXconObjectsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TDM-XCON-MIB",
    **{"zhoneTdmXconMib": zhoneTdmXconMib,
       "zhoneTdmXconObjectsGroup": zhoneTdmXconObjectsGroup,
       "zhoneTdmXconTable": zhoneTdmXconTable,
       "zhoneTdmXconEntry": zhoneTdmXconEntry,
       "zhoneXconFromWanGroupID": zhoneXconFromWanGroupID,
       "zhoneXconFromTS": zhoneXconFromTS,
       "zhoneXconType": zhoneXconType,
       "zhoneXconToPortGroupID": zhoneXconToPortGroupID,
       "zhoneXconToTS": zhoneXconToTS,
       "zhoneXconHighway": zhoneXconHighway,
       "zhoneXconRowStatus": zhoneXconRowStatus}
)
