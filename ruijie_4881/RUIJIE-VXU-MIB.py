# SNMP MIB module (RUIJIE-VXU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-VXU-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 10:59:00 2025
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

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ruijieVxuMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 126)
)
if mibBuilder.loadTexts:
    ruijieVxuMIB.setRevisions(
        ("2013-08-06 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieVxuMIBObjects_ObjectIdentity = ObjectIdentity
ruijieVxuMIBObjects = _RuijieVxuMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 126, 1)
)
_RuijieVxuDeviceInfo_ObjectIdentity = ObjectIdentity
ruijieVxuDeviceInfo = _RuijieVxuDeviceInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 126, 1, 1)
)
_RuijieVxuDeviceTable_Object = MibTable
ruijieVxuDeviceTable = _RuijieVxuDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 126, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ruijieVxuDeviceTable.setStatus("current")
_RuijieVxuDeviceEntry_Object = MibTableRow
ruijieVxuDeviceEntry = _RuijieVxuDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 126, 1, 1, 1, 1)
)
ruijieVxuDeviceEntry.setIndexNames(
    (0, "RUIJIE-VXU-MIB", "ruijieVxuDeviceID"),
)
if mibBuilder.loadTexts:
    ruijieVxuDeviceEntry.setStatus("current")
_RuijieVxuDeviceID_Type = Integer32
_RuijieVxuDeviceID_Object = MibTableColumn
ruijieVxuDeviceID = _RuijieVxuDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 126, 1, 1, 1, 1, 1),
    _RuijieVxuDeviceID_Type()
)
ruijieVxuDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVxuDeviceID.setStatus("current")
_RuijieVxuDeviceMac_Type = MacAddress
_RuijieVxuDeviceMac_Object = MibTableColumn
ruijieVxuDeviceMac = _RuijieVxuDeviceMac_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 126, 1, 1, 1, 1, 2),
    _RuijieVxuDeviceMac_Type()
)
ruijieVxuDeviceMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVxuDeviceMac.setStatus("current")
_RuijieVxuDeviceDescr_Type = DisplayString
_RuijieVxuDeviceDescr_Object = MibTableColumn
ruijieVxuDeviceDescr = _RuijieVxuDeviceDescr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 126, 1, 1, 1, 1, 3),
    _RuijieVxuDeviceDescr_Type()
)
ruijieVxuDeviceDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieVxuDeviceDescr.setStatus("current")


class _RuijieVxuDeviceRole_Type(Integer32):
    """Custom type ruijieVxuDeviceRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("slaver", 2))
    )


_RuijieVxuDeviceRole_Type.__name__ = "Integer32"
_RuijieVxuDeviceRole_Object = MibTableColumn
ruijieVxuDeviceRole = _RuijieVxuDeviceRole_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 126, 1, 1, 1, 1, 4),
    _RuijieVxuDeviceRole_Type()
)
ruijieVxuDeviceRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVxuDeviceRole.setStatus("current")
_RuijieVxuVxl_ObjectIdentity = ObjectIdentity
ruijieVxuVxl = _RuijieVxuVxl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 126, 1, 2)
)
_RuijieVxuVxlTable_Object = MibTable
ruijieVxuVxlTable = _RuijieVxuVxlTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 126, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ruijieVxuVxlTable.setStatus("current")
_RuijieVxuVxlEntry_Object = MibTableRow
ruijieVxuVxlEntry = _RuijieVxuVxlEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 126, 1, 2, 1, 1)
)
ruijieVxuVxlEntry.setIndexNames(
    (0, "RUIJIE-VXU-MIB", "ruijieVxuChildDeviceID"),
)
if mibBuilder.loadTexts:
    ruijieVxuVxlEntry.setStatus("current")
_RuijieVxuChildDeviceID_Type = Integer32
_RuijieVxuChildDeviceID_Object = MibTableColumn
ruijieVxuChildDeviceID = _RuijieVxuChildDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 126, 1, 2, 1, 1, 1),
    _RuijieVxuChildDeviceID_Type()
)
ruijieVxuChildDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVxuChildDeviceID.setStatus("current")
_RuijieVxuFatherDeviceID_Type = Integer32
_RuijieVxuFatherDeviceID_Object = MibTableColumn
ruijieVxuFatherDeviceID = _RuijieVxuFatherDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 126, 1, 2, 1, 1, 2),
    _RuijieVxuFatherDeviceID_Type()
)
ruijieVxuFatherDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVxuFatherDeviceID.setStatus("current")
_RuijieVxuFatherVxlIndex_Type = Integer32
_RuijieVxuFatherVxlIndex_Object = MibTableColumn
ruijieVxuFatherVxlIndex = _RuijieVxuFatherVxlIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 126, 1, 2, 1, 1, 3),
    _RuijieVxuFatherVxlIndex_Type()
)
ruijieVxuFatherVxlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVxuFatherVxlIndex.setStatus("current")


class _RuijieVxuVxlMode_Type(Integer32):
    """Custom type ruijieVxuVxlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dynamic", 2))
    )


_RuijieVxuVxlMode_Type.__name__ = "Integer32"
_RuijieVxuVxlMode_Object = MibTableColumn
ruijieVxuVxlMode = _RuijieVxuVxlMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 126, 1, 2, 1, 1, 4),
    _RuijieVxuVxlMode_Type()
)
ruijieVxuVxlMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVxuVxlMode.setStatus("current")
_RuijieVxuVxlPortTable_Object = MibTable
ruijieVxuVxlPortTable = _RuijieVxuVxlPortTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 126, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ruijieVxuVxlPortTable.setStatus("current")
_RuijieVxuVxlPortEntry_Object = MibTableRow
ruijieVxuVxlPortEntry = _RuijieVxuVxlPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 126, 1, 2, 2, 1)
)
ruijieVxuVxlPortEntry.setIndexNames(
    (0, "RUIJIE-VXU-MIB", "ruijieVxuVxlDeviceID"),
    (0, "RUIJIE-VXU-MIB", "ruijieVxuVxlIndex"),
    (0, "RUIJIE-VXU-MIB", "ruijieVxuVxlPortIndex"),
)
if mibBuilder.loadTexts:
    ruijieVxuVxlPortEntry.setStatus("current")
_RuijieVxuVxlDeviceID_Type = Integer32
_RuijieVxuVxlDeviceID_Object = MibTableColumn
ruijieVxuVxlDeviceID = _RuijieVxuVxlDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 126, 1, 2, 2, 1, 1),
    _RuijieVxuVxlDeviceID_Type()
)
ruijieVxuVxlDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVxuVxlDeviceID.setStatus("current")
_RuijieVxuVxlIndex_Type = Integer32
_RuijieVxuVxlIndex_Object = MibTableColumn
ruijieVxuVxlIndex = _RuijieVxuVxlIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 126, 1, 2, 2, 1, 2),
    _RuijieVxuVxlIndex_Type()
)
ruijieVxuVxlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVxuVxlIndex.setStatus("current")
_RuijieVxuVxlPortIndex_Type = Integer32
_RuijieVxuVxlPortIndex_Object = MibTableColumn
ruijieVxuVxlPortIndex = _RuijieVxuVxlPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 126, 1, 2, 2, 1, 3),
    _RuijieVxuVxlPortIndex_Type()
)
ruijieVxuVxlPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVxuVxlPortIndex.setStatus("current")


class _RuijieVxuVxlPortMode_Type(Integer32):
    """Custom type ruijieVxuVxlPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dynamic", 2))
    )


_RuijieVxuVxlPortMode_Type.__name__ = "Integer32"
_RuijieVxuVxlPortMode_Object = MibTableColumn
ruijieVxuVxlPortMode = _RuijieVxuVxlPortMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 126, 1, 2, 2, 1, 4),
    _RuijieVxuVxlPortMode_Type()
)
ruijieVxuVxlPortMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVxuVxlPortMode.setStatus("current")
_RuijieVxuVxlPortDeviceID_Type = Integer32
_RuijieVxuVxlPortDeviceID_Object = MibTableColumn
ruijieVxuVxlPortDeviceID = _RuijieVxuVxlPortDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 126, 1, 2, 2, 1, 5),
    _RuijieVxuVxlPortDeviceID_Type()
)
ruijieVxuVxlPortDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVxuVxlPortDeviceID.setStatus("current")
_RuijieVxuVxlPortSlotID_Type = Integer32
_RuijieVxuVxlPortSlotID_Object = MibTableColumn
ruijieVxuVxlPortSlotID = _RuijieVxuVxlPortSlotID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 126, 1, 2, 2, 1, 6),
    _RuijieVxuVxlPortSlotID_Type()
)
ruijieVxuVxlPortSlotID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVxuVxlPortSlotID.setStatus("current")
_RuijieVxuVxlPortID_Type = Integer32
_RuijieVxuVxlPortID_Object = MibTableColumn
ruijieVxuVxlPortID = _RuijieVxuVxlPortID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 126, 1, 2, 2, 1, 7),
    _RuijieVxuVxlPortID_Type()
)
ruijieVxuVxlPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVxuVxlPortID.setStatus("current")
_RuijieVxuVxlPortPeerDeviceID_Type = Integer32
_RuijieVxuVxlPortPeerDeviceID_Object = MibTableColumn
ruijieVxuVxlPortPeerDeviceID = _RuijieVxuVxlPortPeerDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 126, 1, 2, 2, 1, 8),
    _RuijieVxuVxlPortPeerDeviceID_Type()
)
ruijieVxuVxlPortPeerDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVxuVxlPortPeerDeviceID.setStatus("current")
_RuijieVxuVxlPortPeerSlotID_Type = Integer32
_RuijieVxuVxlPortPeerSlotID_Object = MibTableColumn
ruijieVxuVxlPortPeerSlotID = _RuijieVxuVxlPortPeerSlotID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 126, 1, 2, 2, 1, 9),
    _RuijieVxuVxlPortPeerSlotID_Type()
)
ruijieVxuVxlPortPeerSlotID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVxuVxlPortPeerSlotID.setStatus("current")
_RuijieVxuVxlPortPeerID_Type = Integer32
_RuijieVxuVxlPortPeerID_Object = MibTableColumn
ruijieVxuVxlPortPeerID = _RuijieVxuVxlPortPeerID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 126, 1, 2, 2, 1, 10),
    _RuijieVxuVxlPortPeerID_Type()
)
ruijieVxuVxlPortPeerID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVxuVxlPortPeerID.setStatus("current")
_RuijieVxuLocation_ObjectIdentity = ObjectIdentity
ruijieVxuLocation = _RuijieVxuLocation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 126, 1, 3)
)
_RuijieVxuLocationTable_Object = MibTable
ruijieVxuLocationTable = _RuijieVxuLocationTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 126, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ruijieVxuLocationTable.setStatus("current")
_RuijieVxuLocationEntry_Object = MibTableRow
ruijieVxuLocationEntry = _RuijieVxuLocationEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 126, 1, 3, 1, 1)
)
ruijieVxuLocationEntry.setIndexNames(
    (0, "RUIJIE-VXU-MIB", "ruijieVxuLocationDeviceID"),
    (0, "RUIJIE-VXU-MIB", "ruijieVxuLocationSlotID"),
)
if mibBuilder.loadTexts:
    ruijieVxuLocationEntry.setStatus("current")
_RuijieVxuLocationDeviceID_Type = Integer32
_RuijieVxuLocationDeviceID_Object = MibTableColumn
ruijieVxuLocationDeviceID = _RuijieVxuLocationDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 126, 1, 3, 1, 1, 1),
    _RuijieVxuLocationDeviceID_Type()
)
ruijieVxuLocationDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVxuLocationDeviceID.setStatus("current")
_RuijieVxuLocationSlotID_Type = Integer32
_RuijieVxuLocationSlotID_Object = MibTableColumn
ruijieVxuLocationSlotID = _RuijieVxuLocationSlotID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 126, 1, 3, 1, 1, 2),
    _RuijieVxuLocationSlotID_Type()
)
ruijieVxuLocationSlotID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVxuLocationSlotID.setStatus("current")


class _RuijieVxuLocationSet_Type(Integer32):
    """Custom type ruijieVxuLocationSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("light", 1)
    )


_RuijieVxuLocationSet_Type.__name__ = "Integer32"
_RuijieVxuLocationSet_Object = MibTableColumn
ruijieVxuLocationSet = _RuijieVxuLocationSet_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 126, 1, 3, 1, 1, 3),
    _RuijieVxuLocationSet_Type()
)
ruijieVxuLocationSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieVxuLocationSet.setStatus("current")
_RuijieVxuVersion_Type = DisplayString
_RuijieVxuVersion_Object = MibScalar
ruijieVxuVersion = _RuijieVxuVersion_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 126, 1, 4),
    _RuijieVxuVersion_Type()
)
ruijieVxuVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVxuVersion.setStatus("current")
_RuijieVxuMIBTraps_ObjectIdentity = ObjectIdentity
ruijieVxuMIBTraps = _RuijieVxuMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 126, 2)
)
_RuijieVxuTrapsNtfObjects_ObjectIdentity = ObjectIdentity
ruijieVxuTrapsNtfObjects = _RuijieVxuTrapsNtfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 126, 2, 1)
)


class _RuijieVxuDeviceState_Type(Integer32):
    """Custom type ruijieVxuDeviceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("online", 1),
          ("offline", 2))
    )


_RuijieVxuDeviceState_Type.__name__ = "Integer32"
_RuijieVxuDeviceState_Object = MibScalar
ruijieVxuDeviceState = _RuijieVxuDeviceState_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 126, 2, 1, 1),
    _RuijieVxuDeviceState_Type()
)
ruijieVxuDeviceState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieVxuDeviceState.setStatus("current")


class _RuijieVxuVxlState_Type(Integer32):
    """Custom type ruijieVxuVxlState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vxl", 1),
          ("normal", 2))
    )


_RuijieVxuVxlState_Type.__name__ = "Integer32"
_RuijieVxuVxlState_Object = MibScalar
ruijieVxuVxlState = _RuijieVxuVxlState_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 126, 2, 1, 2),
    _RuijieVxuVxlState_Type()
)
ruijieVxuVxlState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieVxuVxlState.setStatus("current")
_RuijieVxuTrapsNotifications_ObjectIdentity = ObjectIdentity
ruijieVxuTrapsNotifications = _RuijieVxuTrapsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 126, 2, 2)
)

# Managed Objects groups


# Notification objects

ruijieVxuNotifyDeviceChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 126, 2, 2, 1)
)
ruijieVxuNotifyDeviceChange.setObjects(
      *(("RUIJIE-VXU-MIB", "ruijieVxuLocationDeviceID"),
        ("RUIJIE-VXU-MIB", "ruijieVxuLocationSlotID"),
        ("RUIJIE-VXU-MIB", "ruijieVxuDeviceState"))
)
if mibBuilder.loadTexts:
    ruijieVxuNotifyDeviceChange.setStatus(
        "current"
    )

ruijieVxuNotifyVxlChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 126, 2, 2, 2)
)
ruijieVxuNotifyVxlChange.setObjects(
      *(("RUIJIE-VXU-MIB", "ruijieVxuVxlPortDeviceID"),
        ("RUIJIE-VXU-MIB", "ruijieVxuVxlPortSlotID"),
        ("RUIJIE-VXU-MIB", "ruijieVxuVxlPortID"),
        ("RUIJIE-VXU-MIB", "ruijieVxuVxlState"))
)
if mibBuilder.loadTexts:
    ruijieVxuNotifyVxlChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-VXU-MIB",
    **{"ruijieVxuMIB": ruijieVxuMIB,
       "ruijieVxuMIBObjects": ruijieVxuMIBObjects,
       "ruijieVxuDeviceInfo": ruijieVxuDeviceInfo,
       "ruijieVxuDeviceTable": ruijieVxuDeviceTable,
       "ruijieVxuDeviceEntry": ruijieVxuDeviceEntry,
       "ruijieVxuDeviceID": ruijieVxuDeviceID,
       "ruijieVxuDeviceMac": ruijieVxuDeviceMac,
       "ruijieVxuDeviceDescr": ruijieVxuDeviceDescr,
       "ruijieVxuDeviceRole": ruijieVxuDeviceRole,
       "ruijieVxuVxl": ruijieVxuVxl,
       "ruijieVxuVxlTable": ruijieVxuVxlTable,
       "ruijieVxuVxlEntry": ruijieVxuVxlEntry,
       "ruijieVxuChildDeviceID": ruijieVxuChildDeviceID,
       "ruijieVxuFatherDeviceID": ruijieVxuFatherDeviceID,
       "ruijieVxuFatherVxlIndex": ruijieVxuFatherVxlIndex,
       "ruijieVxuVxlMode": ruijieVxuVxlMode,
       "ruijieVxuVxlPortTable": ruijieVxuVxlPortTable,
       "ruijieVxuVxlPortEntry": ruijieVxuVxlPortEntry,
       "ruijieVxuVxlDeviceID": ruijieVxuVxlDeviceID,
       "ruijieVxuVxlIndex": ruijieVxuVxlIndex,
       "ruijieVxuVxlPortIndex": ruijieVxuVxlPortIndex,
       "ruijieVxuVxlPortMode": ruijieVxuVxlPortMode,
       "ruijieVxuVxlPortDeviceID": ruijieVxuVxlPortDeviceID,
       "ruijieVxuVxlPortSlotID": ruijieVxuVxlPortSlotID,
       "ruijieVxuVxlPortID": ruijieVxuVxlPortID,
       "ruijieVxuVxlPortPeerDeviceID": ruijieVxuVxlPortPeerDeviceID,
       "ruijieVxuVxlPortPeerSlotID": ruijieVxuVxlPortPeerSlotID,
       "ruijieVxuVxlPortPeerID": ruijieVxuVxlPortPeerID,
       "ruijieVxuLocation": ruijieVxuLocation,
       "ruijieVxuLocationTable": ruijieVxuLocationTable,
       "ruijieVxuLocationEntry": ruijieVxuLocationEntry,
       "ruijieVxuLocationDeviceID": ruijieVxuLocationDeviceID,
       "ruijieVxuLocationSlotID": ruijieVxuLocationSlotID,
       "ruijieVxuLocationSet": ruijieVxuLocationSet,
       "ruijieVxuVersion": ruijieVxuVersion,
       "ruijieVxuMIBTraps": ruijieVxuMIBTraps,
       "ruijieVxuTrapsNtfObjects": ruijieVxuTrapsNtfObjects,
       "ruijieVxuDeviceState": ruijieVxuDeviceState,
       "ruijieVxuVxlState": ruijieVxuVxlState,
       "ruijieVxuTrapsNotifications": ruijieVxuTrapsNotifications,
       "ruijieVxuNotifyDeviceChange": ruijieVxuNotifyDeviceChange,
       "ruijieVxuNotifyVxlChange": ruijieVxuNotifyVxlChange}
)
