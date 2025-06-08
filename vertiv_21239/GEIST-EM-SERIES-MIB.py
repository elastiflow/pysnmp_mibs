# SNMP MIB module (GEIST-EM-SERIES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/vertiv_21239/GEIST-EM-SERIES-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 20:17:19 2025
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

geist = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21239)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EmMeter_ObjectIdentity = ObjectIdentity
emMeter = _EmMeter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21239, 3)
)
_UnitInfo_ObjectIdentity = ObjectIdentity
unitInfo = _UnitInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21239, 3, 1)
)
_UnitInfoTitle_Type = DisplayString
_UnitInfoTitle_Object = MibScalar
unitInfoTitle = _UnitInfoTitle_Object(
    (1, 3, 6, 1, 4, 1, 21239, 3, 1, 1),
    _UnitInfoTitle_Type()
)
unitInfoTitle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitInfoTitle.setStatus("mandatory")
_UnitInfoVersion_Type = DisplayString
_UnitInfoVersion_Object = MibScalar
unitInfoVersion = _UnitInfoVersion_Object(
    (1, 3, 6, 1, 4, 1, 21239, 3, 1, 2),
    _UnitInfoVersion_Type()
)
unitInfoVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitInfoVersion.setStatus("mandatory")
_UnitInfoName_Type = DisplayString
_UnitInfoName_Object = MibScalar
unitInfoName = _UnitInfoName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 3, 1, 3),
    _UnitInfoName_Type()
)
unitInfoName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitInfoName.setStatus("mandatory")
_UnitInfoMAC_Type = DisplayString
_UnitInfoMAC_Object = MibScalar
unitInfoMAC = _UnitInfoMAC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 3, 1, 4),
    _UnitInfoMAC_Type()
)
unitInfoMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitInfoMAC.setStatus("mandatory")
_UnitInfoIP_Type = DisplayString
_UnitInfoIP_Object = MibScalar
unitInfoIP = _UnitInfoIP_Object(
    (1, 3, 6, 1, 4, 1, 21239, 3, 1, 5),
    _UnitInfoIP_Type()
)
unitInfoIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitInfoIP.setStatus("mandatory")


class _UnitInfoMainCount_Type(Integer32):
    """Custom type unitInfoMainCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_UnitInfoMainCount_Type.__name__ = "Integer32"
_UnitInfoMainCount_Object = MibScalar
unitInfoMainCount = _UnitInfoMainCount_Object(
    (1, 3, 6, 1, 4, 1, 21239, 3, 1, 6),
    _UnitInfoMainCount_Type()
)
unitInfoMainCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitInfoMainCount.setStatus("mandatory")


class _UnitInfoAuxCount_Type(Integer32):
    """Custom type unitInfoAuxCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_UnitInfoAuxCount_Type.__name__ = "Integer32"
_UnitInfoAuxCount_Object = MibScalar
unitInfoAuxCount = _UnitInfoAuxCount_Object(
    (1, 3, 6, 1, 4, 1, 21239, 3, 1, 7),
    _UnitInfoAuxCount_Type()
)
unitInfoAuxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitInfoAuxCount.setStatus("mandatory")
_UnitInfoProductID_Type = Gauge32
_UnitInfoProductID_Object = MibScalar
unitInfoProductID = _UnitInfoProductID_Object(
    (1, 3, 6, 1, 4, 1, 21239, 3, 1, 8),
    _UnitInfoProductID_Type()
)
unitInfoProductID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitInfoProductID.setStatus("current")
_MainChannelTable_Object = MibTable
mainChannelTable = _MainChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 3, 2)
)
if mibBuilder.loadTexts:
    mainChannelTable.setStatus("mandatory")
_MainChannelEntry_Object = MibTableRow
mainChannelEntry = _MainChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 3, 2, 1)
)
mainChannelEntry.setIndexNames(
    (0, "GEIST-EM-SERIES-MIB", "mainChannelIndex"),
)
if mibBuilder.loadTexts:
    mainChannelEntry.setStatus("mandatory")
_MainChannelIndex_Type = Integer32
_MainChannelIndex_Object = MibTableColumn
mainChannelIndex = _MainChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 3, 2, 1, 1),
    _MainChannelIndex_Type()
)
mainChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainChannelIndex.setStatus("mandatory")
_MainChannelName_Type = DisplayString
_MainChannelName_Object = MibTableColumn
mainChannelName = _MainChannelName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 3, 2, 1, 2),
    _MainChannelName_Type()
)
mainChannelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainChannelName.setStatus("mandatory")
_MainChannelFriendly_Type = DisplayString
_MainChannelFriendly_Object = MibTableColumn
mainChannelFriendly = _MainChannelFriendly_Object(
    (1, 3, 6, 1, 4, 1, 21239, 3, 2, 1, 3),
    _MainChannelFriendly_Type()
)
mainChannelFriendly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainChannelFriendly.setStatus("mandatory")
_MainChannelDeciAmps_Type = Integer32
_MainChannelDeciAmps_Object = MibTableColumn
mainChannelDeciAmps = _MainChannelDeciAmps_Object(
    (1, 3, 6, 1, 4, 1, 21239, 3, 2, 1, 4),
    _MainChannelDeciAmps_Type()
)
mainChannelDeciAmps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainChannelDeciAmps.setStatus("mandatory")
if mibBuilder.loadTexts:
    mainChannelDeciAmps.setUnits("0.1 Amps")
_MainChannelGroup_Type = DisplayString
_MainChannelGroup_Object = MibTableColumn
mainChannelGroup = _MainChannelGroup_Object(
    (1, 3, 6, 1, 4, 1, 21239, 3, 2, 1, 5),
    _MainChannelGroup_Type()
)
mainChannelGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainChannelGroup.setStatus("mandatory")
_AuxChannelTable_Object = MibTable
auxChannelTable = _AuxChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 3, 3)
)
if mibBuilder.loadTexts:
    auxChannelTable.setStatus("mandatory")
_AuxChannelEntry_Object = MibTableRow
auxChannelEntry = _AuxChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 3, 3, 1)
)
auxChannelEntry.setIndexNames(
    (0, "GEIST-EM-SERIES-MIB", "auxChannelIndex"),
)
if mibBuilder.loadTexts:
    auxChannelEntry.setStatus("mandatory")
_AuxChannelIndex_Type = Integer32
_AuxChannelIndex_Object = MibTableColumn
auxChannelIndex = _AuxChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 3, 3, 1, 1),
    _AuxChannelIndex_Type()
)
auxChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxChannelIndex.setStatus("mandatory")
_AuxChannelName_Type = DisplayString
_AuxChannelName_Object = MibTableColumn
auxChannelName = _AuxChannelName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 3, 3, 1, 2),
    _AuxChannelName_Type()
)
auxChannelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxChannelName.setStatus("mandatory")
_AuxChannelFriendly_Type = DisplayString
_AuxChannelFriendly_Object = MibTableColumn
auxChannelFriendly = _AuxChannelFriendly_Object(
    (1, 3, 6, 1, 4, 1, 21239, 3, 3, 1, 3),
    _AuxChannelFriendly_Type()
)
auxChannelFriendly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxChannelFriendly.setStatus("mandatory")
_AuxChannelDeciAmps_Type = Integer32
_AuxChannelDeciAmps_Object = MibTableColumn
auxChannelDeciAmps = _AuxChannelDeciAmps_Object(
    (1, 3, 6, 1, 4, 1, 21239, 3, 3, 1, 4),
    _AuxChannelDeciAmps_Type()
)
auxChannelDeciAmps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxChannelDeciAmps.setStatus("mandatory")
if mibBuilder.loadTexts:
    auxChannelDeciAmps.setUnits("0.1 Amps")
_AuxChannelGroup_Type = DisplayString
_AuxChannelGroup_Object = MibTableColumn
auxChannelGroup = _AuxChannelGroup_Object(
    (1, 3, 6, 1, 4, 1, 21239, 3, 3, 1, 5),
    _AuxChannelGroup_Type()
)
auxChannelGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxChannelGroup.setStatus("mandatory")

# Managed Objects groups


# Notification objects

mainChannelDeciAmps01ALARM = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 3, 0, 1)
)
mainChannelDeciAmps01ALARM.setObjects(
    ("GEIST-EM-SERIES-MIB", "mainChannelDeciAmps")
)
if mibBuilder.loadTexts:
    mainChannelDeciAmps01ALARM.setStatus(
        ""
    )

mainChannelDeciAmps02ALARM = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 3, 0, 2)
)
mainChannelDeciAmps02ALARM.setObjects(
    ("GEIST-EM-SERIES-MIB", "mainChannelDeciAmps")
)
if mibBuilder.loadTexts:
    mainChannelDeciAmps02ALARM.setStatus(
        ""
    )

mainChannelDeciAmps03ALARM = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 3, 0, 3)
)
mainChannelDeciAmps03ALARM.setObjects(
    ("GEIST-EM-SERIES-MIB", "mainChannelDeciAmps")
)
if mibBuilder.loadTexts:
    mainChannelDeciAmps03ALARM.setStatus(
        ""
    )

mainChannelDeciAmps04ALARM = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 3, 0, 4)
)
mainChannelDeciAmps04ALARM.setObjects(
    ("GEIST-EM-SERIES-MIB", "mainChannelDeciAmps")
)
if mibBuilder.loadTexts:
    mainChannelDeciAmps04ALARM.setStatus(
        ""
    )

mainChannelDeciAmps05ALARM = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 3, 0, 5)
)
mainChannelDeciAmps05ALARM.setObjects(
    ("GEIST-EM-SERIES-MIB", "mainChannelDeciAmps")
)
if mibBuilder.loadTexts:
    mainChannelDeciAmps05ALARM.setStatus(
        ""
    )

mainChannelDeciAmps06ALARM = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 3, 0, 6)
)
mainChannelDeciAmps06ALARM.setObjects(
    ("GEIST-EM-SERIES-MIB", "mainChannelDeciAmps")
)
if mibBuilder.loadTexts:
    mainChannelDeciAmps06ALARM.setStatus(
        ""
    )

mainChannelDeciAmps07ALARM = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 3, 0, 7)
)
mainChannelDeciAmps07ALARM.setObjects(
    ("GEIST-EM-SERIES-MIB", "mainChannelDeciAmps")
)
if mibBuilder.loadTexts:
    mainChannelDeciAmps07ALARM.setStatus(
        ""
    )

mainChannelDeciAmps08ALARM = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 3, 0, 8)
)
mainChannelDeciAmps08ALARM.setObjects(
    ("GEIST-EM-SERIES-MIB", "mainChannelDeciAmps")
)
if mibBuilder.loadTexts:
    mainChannelDeciAmps08ALARM.setStatus(
        ""
    )

auxChannelDeciAmps01ALARM = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 3, 0, 9)
)
auxChannelDeciAmps01ALARM.setObjects(
    ("GEIST-EM-SERIES-MIB", "auxChannelDeciAmps")
)
if mibBuilder.loadTexts:
    auxChannelDeciAmps01ALARM.setStatus(
        ""
    )

auxChannelDeciAmps02ALARM = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 3, 0, 10)
)
auxChannelDeciAmps02ALARM.setObjects(
    ("GEIST-EM-SERIES-MIB", "auxChannelDeciAmps")
)
if mibBuilder.loadTexts:
    auxChannelDeciAmps02ALARM.setStatus(
        ""
    )

auxChannelDeciAmps03ALARM = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 3, 0, 11)
)
auxChannelDeciAmps03ALARM.setObjects(
    ("GEIST-EM-SERIES-MIB", "auxChannelDeciAmps")
)
if mibBuilder.loadTexts:
    auxChannelDeciAmps03ALARM.setStatus(
        ""
    )

auxChannelDeciAmps04ALARM = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 3, 0, 12)
)
auxChannelDeciAmps04ALARM.setObjects(
    ("GEIST-EM-SERIES-MIB", "auxChannelDeciAmps")
)
if mibBuilder.loadTexts:
    auxChannelDeciAmps04ALARM.setStatus(
        ""
    )

auxChannelDeciAmps05ALARM = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 3, 0, 13)
)
auxChannelDeciAmps05ALARM.setObjects(
    ("GEIST-EM-SERIES-MIB", "auxChannelDeciAmps")
)
if mibBuilder.loadTexts:
    auxChannelDeciAmps05ALARM.setStatus(
        ""
    )

auxChannelDeciAmps06ALARM = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 3, 0, 14)
)
auxChannelDeciAmps06ALARM.setObjects(
    ("GEIST-EM-SERIES-MIB", "auxChannelDeciAmps")
)
if mibBuilder.loadTexts:
    auxChannelDeciAmps06ALARM.setStatus(
        ""
    )

auxChannelDeciAmps07ALARM = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 3, 0, 15)
)
auxChannelDeciAmps07ALARM.setObjects(
    ("GEIST-EM-SERIES-MIB", "auxChannelDeciAmps")
)
if mibBuilder.loadTexts:
    auxChannelDeciAmps07ALARM.setStatus(
        ""
    )

auxChannelDeciAmps08ALARM = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 3, 0, 16)
)
auxChannelDeciAmps08ALARM.setObjects(
    ("GEIST-EM-SERIES-MIB", "auxChannelDeciAmps")
)
if mibBuilder.loadTexts:
    auxChannelDeciAmps08ALARM.setStatus(
        ""
    )

auxChannelDeciAmps09ALARM = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 3, 0, 17)
)
auxChannelDeciAmps09ALARM.setObjects(
    ("GEIST-EM-SERIES-MIB", "auxChannelDeciAmps")
)
if mibBuilder.loadTexts:
    auxChannelDeciAmps09ALARM.setStatus(
        ""
    )

auxChannelDeciAmps10ALARM = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 3, 0, 18)
)
auxChannelDeciAmps10ALARM.setObjects(
    ("GEIST-EM-SERIES-MIB", "auxChannelDeciAmps")
)
if mibBuilder.loadTexts:
    auxChannelDeciAmps10ALARM.setStatus(
        ""
    )

auxChannelDeciAmps11ALARM = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 3, 0, 19)
)
auxChannelDeciAmps11ALARM.setObjects(
    ("GEIST-EM-SERIES-MIB", "auxChannelDeciAmps")
)
if mibBuilder.loadTexts:
    auxChannelDeciAmps11ALARM.setStatus(
        ""
    )

auxChannelDeciAmps12ALARM = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 3, 0, 20)
)
auxChannelDeciAmps12ALARM.setObjects(
    ("GEIST-EM-SERIES-MIB", "auxChannelDeciAmps")
)
if mibBuilder.loadTexts:
    auxChannelDeciAmps12ALARM.setStatus(
        ""
    )

auxChannelDeciAmps13ALARM = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 3, 0, 21)
)
auxChannelDeciAmps13ALARM.setObjects(
    ("GEIST-EM-SERIES-MIB", "auxChannelDeciAmps")
)
if mibBuilder.loadTexts:
    auxChannelDeciAmps13ALARM.setStatus(
        ""
    )

auxChannelDeciAmps14ALARM = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 3, 0, 22)
)
auxChannelDeciAmps14ALARM.setObjects(
    ("GEIST-EM-SERIES-MIB", "auxChannelDeciAmps")
)
if mibBuilder.loadTexts:
    auxChannelDeciAmps14ALARM.setStatus(
        ""
    )

auxChannelDeciAmps15ALARM = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 3, 0, 23)
)
auxChannelDeciAmps15ALARM.setObjects(
    ("GEIST-EM-SERIES-MIB", "auxChannelDeciAmps")
)
if mibBuilder.loadTexts:
    auxChannelDeciAmps15ALARM.setStatus(
        ""
    )

auxChannelDeciAmps16ALARM = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 3, 0, 24)
)
auxChannelDeciAmps16ALARM.setObjects(
    ("GEIST-EM-SERIES-MIB", "auxChannelDeciAmps")
)
if mibBuilder.loadTexts:
    auxChannelDeciAmps16ALARM.setStatus(
        ""
    )

auxChannelDeciAmps17ALARM = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 3, 0, 25)
)
auxChannelDeciAmps17ALARM.setObjects(
    ("GEIST-EM-SERIES-MIB", "auxChannelDeciAmps")
)
if mibBuilder.loadTexts:
    auxChannelDeciAmps17ALARM.setStatus(
        ""
    )

auxChannelDeciAmps18ALARM = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 3, 0, 26)
)
auxChannelDeciAmps18ALARM.setObjects(
    ("GEIST-EM-SERIES-MIB", "auxChannelDeciAmps")
)
if mibBuilder.loadTexts:
    auxChannelDeciAmps18ALARM.setStatus(
        ""
    )

auxChannelDeciAmps19ALARM = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 3, 0, 27)
)
auxChannelDeciAmps19ALARM.setObjects(
    ("GEIST-EM-SERIES-MIB", "auxChannelDeciAmps")
)
if mibBuilder.loadTexts:
    auxChannelDeciAmps19ALARM.setStatus(
        ""
    )

auxChannelDeciAmps20ALARM = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 3, 0, 28)
)
auxChannelDeciAmps20ALARM.setObjects(
    ("GEIST-EM-SERIES-MIB", "auxChannelDeciAmps")
)
if mibBuilder.loadTexts:
    auxChannelDeciAmps20ALARM.setStatus(
        ""
    )

auxChannelDeciAmps21ALARM = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 3, 0, 29)
)
auxChannelDeciAmps21ALARM.setObjects(
    ("GEIST-EM-SERIES-MIB", "auxChannelDeciAmps")
)
if mibBuilder.loadTexts:
    auxChannelDeciAmps21ALARM.setStatus(
        ""
    )

auxChannelDeciAmps22ALARM = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 3, 0, 30)
)
auxChannelDeciAmps22ALARM.setObjects(
    ("GEIST-EM-SERIES-MIB", "auxChannelDeciAmps")
)
if mibBuilder.loadTexts:
    auxChannelDeciAmps22ALARM.setStatus(
        ""
    )

auxChannelDeciAmps23ALARM = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 3, 0, 31)
)
auxChannelDeciAmps23ALARM.setObjects(
    ("GEIST-EM-SERIES-MIB", "auxChannelDeciAmps")
)
if mibBuilder.loadTexts:
    auxChannelDeciAmps23ALARM.setStatus(
        ""
    )

auxChannelDeciAmps24ALARM = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 3, 0, 32)
)
auxChannelDeciAmps24ALARM.setObjects(
    ("GEIST-EM-SERIES-MIB", "auxChannelDeciAmps")
)
if mibBuilder.loadTexts:
    auxChannelDeciAmps24ALARM.setStatus(
        ""
    )

auxChannelDeciAmps25ALARM = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 3, 0, 33)
)
auxChannelDeciAmps25ALARM.setObjects(
    ("GEIST-EM-SERIES-MIB", "auxChannelDeciAmps")
)
if mibBuilder.loadTexts:
    auxChannelDeciAmps25ALARM.setStatus(
        ""
    )

auxChannelDeciAmps26ALARM = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 3, 0, 34)
)
auxChannelDeciAmps26ALARM.setObjects(
    ("GEIST-EM-SERIES-MIB", "auxChannelDeciAmps")
)
if mibBuilder.loadTexts:
    auxChannelDeciAmps26ALARM.setStatus(
        ""
    )

auxChannelDeciAmps27ALARM = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 3, 0, 35)
)
auxChannelDeciAmps27ALARM.setObjects(
    ("GEIST-EM-SERIES-MIB", "auxChannelDeciAmps")
)
if mibBuilder.loadTexts:
    auxChannelDeciAmps27ALARM.setStatus(
        ""
    )

auxChannelDeciAmps28ALARM = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 3, 0, 36)
)
auxChannelDeciAmps28ALARM.setObjects(
    ("GEIST-EM-SERIES-MIB", "auxChannelDeciAmps")
)
if mibBuilder.loadTexts:
    auxChannelDeciAmps28ALARM.setStatus(
        ""
    )

auxChannelDeciAmps29ALARM = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 3, 0, 37)
)
auxChannelDeciAmps29ALARM.setObjects(
    ("GEIST-EM-SERIES-MIB", "auxChannelDeciAmps")
)
if mibBuilder.loadTexts:
    auxChannelDeciAmps29ALARM.setStatus(
        ""
    )

auxChannelDeciAmps30ALARM = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 3, 0, 38)
)
auxChannelDeciAmps30ALARM.setObjects(
    ("GEIST-EM-SERIES-MIB", "auxChannelDeciAmps")
)
if mibBuilder.loadTexts:
    auxChannelDeciAmps30ALARM.setStatus(
        ""
    )

auxChannelDeciAmps31ALARM = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 3, 0, 39)
)
auxChannelDeciAmps31ALARM.setObjects(
    ("GEIST-EM-SERIES-MIB", "auxChannelDeciAmps")
)
if mibBuilder.loadTexts:
    auxChannelDeciAmps31ALARM.setStatus(
        ""
    )

auxChannelDeciAmps32ALARM = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 3, 0, 40)
)
auxChannelDeciAmps32ALARM.setObjects(
    ("GEIST-EM-SERIES-MIB", "auxChannelDeciAmps")
)
if mibBuilder.loadTexts:
    auxChannelDeciAmps32ALARM.setStatus(
        ""
    )

mainChannelDeciAmps01WARN = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 3, 0, 41)
)
mainChannelDeciAmps01WARN.setObjects(
    ("GEIST-EM-SERIES-MIB", "mainChannelDeciAmps")
)
if mibBuilder.loadTexts:
    mainChannelDeciAmps01WARN.setStatus(
        ""
    )

mainChannelDeciAmps02WARN = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 3, 0, 42)
)
mainChannelDeciAmps02WARN.setObjects(
    ("GEIST-EM-SERIES-MIB", "mainChannelDeciAmps")
)
if mibBuilder.loadTexts:
    mainChannelDeciAmps02WARN.setStatus(
        ""
    )

mainChannelDeciAmps03WARN = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 3, 0, 43)
)
mainChannelDeciAmps03WARN.setObjects(
    ("GEIST-EM-SERIES-MIB", "mainChannelDeciAmps")
)
if mibBuilder.loadTexts:
    mainChannelDeciAmps03WARN.setStatus(
        ""
    )

mainChannelDeciAmps04WARN = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 3, 0, 44)
)
mainChannelDeciAmps04WARN.setObjects(
    ("GEIST-EM-SERIES-MIB", "mainChannelDeciAmps")
)
if mibBuilder.loadTexts:
    mainChannelDeciAmps04WARN.setStatus(
        ""
    )

mainChannelDeciAmps05WARN = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 3, 0, 45)
)
mainChannelDeciAmps05WARN.setObjects(
    ("GEIST-EM-SERIES-MIB", "mainChannelDeciAmps")
)
if mibBuilder.loadTexts:
    mainChannelDeciAmps05WARN.setStatus(
        ""
    )

mainChannelDeciAmps06WARN = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 3, 0, 46)
)
mainChannelDeciAmps06WARN.setObjects(
    ("GEIST-EM-SERIES-MIB", "mainChannelDeciAmps")
)
if mibBuilder.loadTexts:
    mainChannelDeciAmps06WARN.setStatus(
        ""
    )

mainChannelDeciAmps07WARN = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 3, 0, 47)
)
mainChannelDeciAmps07WARN.setObjects(
    ("GEIST-EM-SERIES-MIB", "mainChannelDeciAmps")
)
if mibBuilder.loadTexts:
    mainChannelDeciAmps07WARN.setStatus(
        ""
    )

mainChannelDeciAmps08WARN = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 3, 0, 48)
)
mainChannelDeciAmps08WARN.setObjects(
    ("GEIST-EM-SERIES-MIB", "mainChannelDeciAmps")
)
if mibBuilder.loadTexts:
    mainChannelDeciAmps08WARN.setStatus(
        ""
    )

auxChannelDeciAmps01WARN = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 3, 0, 49)
)
auxChannelDeciAmps01WARN.setObjects(
    ("GEIST-EM-SERIES-MIB", "auxChannelDeciAmps")
)
if mibBuilder.loadTexts:
    auxChannelDeciAmps01WARN.setStatus(
        ""
    )

auxChannelDeciAmps02WARN = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 3, 0, 50)
)
auxChannelDeciAmps02WARN.setObjects(
    ("GEIST-EM-SERIES-MIB", "auxChannelDeciAmps")
)
if mibBuilder.loadTexts:
    auxChannelDeciAmps02WARN.setStatus(
        ""
    )

auxChannelDeciAmps03WARN = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 3, 0, 51)
)
auxChannelDeciAmps03WARN.setObjects(
    ("GEIST-EM-SERIES-MIB", "auxChannelDeciAmps")
)
if mibBuilder.loadTexts:
    auxChannelDeciAmps03WARN.setStatus(
        ""
    )

auxChannelDeciAmps04WARN = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 3, 0, 52)
)
auxChannelDeciAmps04WARN.setObjects(
    ("GEIST-EM-SERIES-MIB", "auxChannelDeciAmps")
)
if mibBuilder.loadTexts:
    auxChannelDeciAmps04WARN.setStatus(
        ""
    )

auxChannelDeciAmps05WARN = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 3, 0, 53)
)
auxChannelDeciAmps05WARN.setObjects(
    ("GEIST-EM-SERIES-MIB", "auxChannelDeciAmps")
)
if mibBuilder.loadTexts:
    auxChannelDeciAmps05WARN.setStatus(
        ""
    )

auxChannelDeciAmps06WARN = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 3, 0, 54)
)
auxChannelDeciAmps06WARN.setObjects(
    ("GEIST-EM-SERIES-MIB", "auxChannelDeciAmps")
)
if mibBuilder.loadTexts:
    auxChannelDeciAmps06WARN.setStatus(
        ""
    )

auxChannelDeciAmps07WARN = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 3, 0, 55)
)
auxChannelDeciAmps07WARN.setObjects(
    ("GEIST-EM-SERIES-MIB", "auxChannelDeciAmps")
)
if mibBuilder.loadTexts:
    auxChannelDeciAmps07WARN.setStatus(
        ""
    )

auxChannelDeciAmps08WARN = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 3, 0, 56)
)
auxChannelDeciAmps08WARN.setObjects(
    ("GEIST-EM-SERIES-MIB", "auxChannelDeciAmps")
)
if mibBuilder.loadTexts:
    auxChannelDeciAmps08WARN.setStatus(
        ""
    )

auxChannelDeciAmps09WARN = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 3, 0, 57)
)
auxChannelDeciAmps09WARN.setObjects(
    ("GEIST-EM-SERIES-MIB", "auxChannelDeciAmps")
)
if mibBuilder.loadTexts:
    auxChannelDeciAmps09WARN.setStatus(
        ""
    )

auxChannelDeciAmps10WARN = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 3, 0, 58)
)
auxChannelDeciAmps10WARN.setObjects(
    ("GEIST-EM-SERIES-MIB", "auxChannelDeciAmps")
)
if mibBuilder.loadTexts:
    auxChannelDeciAmps10WARN.setStatus(
        ""
    )

auxChannelDeciAmps11WARN = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 3, 0, 59)
)
auxChannelDeciAmps11WARN.setObjects(
    ("GEIST-EM-SERIES-MIB", "auxChannelDeciAmps")
)
if mibBuilder.loadTexts:
    auxChannelDeciAmps11WARN.setStatus(
        ""
    )

auxChannelDeciAmps12WARN = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 3, 0, 60)
)
auxChannelDeciAmps12WARN.setObjects(
    ("GEIST-EM-SERIES-MIB", "auxChannelDeciAmps")
)
if mibBuilder.loadTexts:
    auxChannelDeciAmps12WARN.setStatus(
        ""
    )

auxChannelDeciAmps13WARN = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 3, 0, 61)
)
auxChannelDeciAmps13WARN.setObjects(
    ("GEIST-EM-SERIES-MIB", "auxChannelDeciAmps")
)
if mibBuilder.loadTexts:
    auxChannelDeciAmps13WARN.setStatus(
        ""
    )

auxChannelDeciAmps14WARN = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 3, 0, 62)
)
auxChannelDeciAmps14WARN.setObjects(
    ("GEIST-EM-SERIES-MIB", "auxChannelDeciAmps")
)
if mibBuilder.loadTexts:
    auxChannelDeciAmps14WARN.setStatus(
        ""
    )

auxChannelDeciAmps15WARN = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 3, 0, 63)
)
auxChannelDeciAmps15WARN.setObjects(
    ("GEIST-EM-SERIES-MIB", "auxChannelDeciAmps")
)
if mibBuilder.loadTexts:
    auxChannelDeciAmps15WARN.setStatus(
        ""
    )

auxChannelDeciAmps16WARN = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 3, 0, 64)
)
auxChannelDeciAmps16WARN.setObjects(
    ("GEIST-EM-SERIES-MIB", "auxChannelDeciAmps")
)
if mibBuilder.loadTexts:
    auxChannelDeciAmps16WARN.setStatus(
        ""
    )

auxChannelDeciAmps17WARN = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 3, 0, 65)
)
auxChannelDeciAmps17WARN.setObjects(
    ("GEIST-EM-SERIES-MIB", "auxChannelDeciAmps")
)
if mibBuilder.loadTexts:
    auxChannelDeciAmps17WARN.setStatus(
        ""
    )

auxChannelDeciAmps18WARN = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 3, 0, 66)
)
auxChannelDeciAmps18WARN.setObjects(
    ("GEIST-EM-SERIES-MIB", "auxChannelDeciAmps")
)
if mibBuilder.loadTexts:
    auxChannelDeciAmps18WARN.setStatus(
        ""
    )

auxChannelDeciAmps19WARN = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 3, 0, 67)
)
auxChannelDeciAmps19WARN.setObjects(
    ("GEIST-EM-SERIES-MIB", "auxChannelDeciAmps")
)
if mibBuilder.loadTexts:
    auxChannelDeciAmps19WARN.setStatus(
        ""
    )

auxChannelDeciAmps20WARN = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 3, 0, 68)
)
auxChannelDeciAmps20WARN.setObjects(
    ("GEIST-EM-SERIES-MIB", "auxChannelDeciAmps")
)
if mibBuilder.loadTexts:
    auxChannelDeciAmps20WARN.setStatus(
        ""
    )

auxChannelDeciAmps21WARN = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 3, 0, 69)
)
auxChannelDeciAmps21WARN.setObjects(
    ("GEIST-EM-SERIES-MIB", "auxChannelDeciAmps")
)
if mibBuilder.loadTexts:
    auxChannelDeciAmps21WARN.setStatus(
        ""
    )

auxChannelDeciAmps22WARN = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 3, 0, 70)
)
auxChannelDeciAmps22WARN.setObjects(
    ("GEIST-EM-SERIES-MIB", "auxChannelDeciAmps")
)
if mibBuilder.loadTexts:
    auxChannelDeciAmps22WARN.setStatus(
        ""
    )

auxChannelDeciAmps23WARN = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 3, 0, 71)
)
auxChannelDeciAmps23WARN.setObjects(
    ("GEIST-EM-SERIES-MIB", "auxChannelDeciAmps")
)
if mibBuilder.loadTexts:
    auxChannelDeciAmps23WARN.setStatus(
        ""
    )

auxChannelDeciAmps24WARN = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 3, 0, 72)
)
auxChannelDeciAmps24WARN.setObjects(
    ("GEIST-EM-SERIES-MIB", "auxChannelDeciAmps")
)
if mibBuilder.loadTexts:
    auxChannelDeciAmps24WARN.setStatus(
        ""
    )

auxChannelDeciAmps25WARN = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 3, 0, 73)
)
auxChannelDeciAmps25WARN.setObjects(
    ("GEIST-EM-SERIES-MIB", "auxChannelDeciAmps")
)
if mibBuilder.loadTexts:
    auxChannelDeciAmps25WARN.setStatus(
        ""
    )

auxChannelDeciAmps26WARN = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 3, 0, 74)
)
auxChannelDeciAmps26WARN.setObjects(
    ("GEIST-EM-SERIES-MIB", "auxChannelDeciAmps")
)
if mibBuilder.loadTexts:
    auxChannelDeciAmps26WARN.setStatus(
        ""
    )

auxChannelDeciAmps27WARN = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 3, 0, 75)
)
auxChannelDeciAmps27WARN.setObjects(
    ("GEIST-EM-SERIES-MIB", "auxChannelDeciAmps")
)
if mibBuilder.loadTexts:
    auxChannelDeciAmps27WARN.setStatus(
        ""
    )

auxChannelDeciAmps28WARN = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 3, 0, 76)
)
auxChannelDeciAmps28WARN.setObjects(
    ("GEIST-EM-SERIES-MIB", "auxChannelDeciAmps")
)
if mibBuilder.loadTexts:
    auxChannelDeciAmps28WARN.setStatus(
        ""
    )

auxChannelDeciAmps29WARN = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 3, 0, 77)
)
auxChannelDeciAmps29WARN.setObjects(
    ("GEIST-EM-SERIES-MIB", "auxChannelDeciAmps")
)
if mibBuilder.loadTexts:
    auxChannelDeciAmps29WARN.setStatus(
        ""
    )

auxChannelDeciAmps30WARN = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 3, 0, 78)
)
auxChannelDeciAmps30WARN.setObjects(
    ("GEIST-EM-SERIES-MIB", "auxChannelDeciAmps")
)
if mibBuilder.loadTexts:
    auxChannelDeciAmps30WARN.setStatus(
        ""
    )

auxChannelDeciAmps31WARN = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 3, 0, 79)
)
auxChannelDeciAmps31WARN.setObjects(
    ("GEIST-EM-SERIES-MIB", "auxChannelDeciAmps")
)
if mibBuilder.loadTexts:
    auxChannelDeciAmps31WARN.setStatus(
        ""
    )

auxChannelDeciAmps32WARN = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 3, 0, 80)
)
auxChannelDeciAmps32WARN.setObjects(
    ("GEIST-EM-SERIES-MIB", "auxChannelDeciAmps")
)
if mibBuilder.loadTexts:
    auxChannelDeciAmps32WARN.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GEIST-EM-SERIES-MIB",
    **{"geist": geist,
       "emMeter": emMeter,
       "mainChannelDeciAmps01ALARM": mainChannelDeciAmps01ALARM,
       "mainChannelDeciAmps02ALARM": mainChannelDeciAmps02ALARM,
       "mainChannelDeciAmps03ALARM": mainChannelDeciAmps03ALARM,
       "mainChannelDeciAmps04ALARM": mainChannelDeciAmps04ALARM,
       "mainChannelDeciAmps05ALARM": mainChannelDeciAmps05ALARM,
       "mainChannelDeciAmps06ALARM": mainChannelDeciAmps06ALARM,
       "mainChannelDeciAmps07ALARM": mainChannelDeciAmps07ALARM,
       "mainChannelDeciAmps08ALARM": mainChannelDeciAmps08ALARM,
       "auxChannelDeciAmps01ALARM": auxChannelDeciAmps01ALARM,
       "auxChannelDeciAmps02ALARM": auxChannelDeciAmps02ALARM,
       "auxChannelDeciAmps03ALARM": auxChannelDeciAmps03ALARM,
       "auxChannelDeciAmps04ALARM": auxChannelDeciAmps04ALARM,
       "auxChannelDeciAmps05ALARM": auxChannelDeciAmps05ALARM,
       "auxChannelDeciAmps06ALARM": auxChannelDeciAmps06ALARM,
       "auxChannelDeciAmps07ALARM": auxChannelDeciAmps07ALARM,
       "auxChannelDeciAmps08ALARM": auxChannelDeciAmps08ALARM,
       "auxChannelDeciAmps09ALARM": auxChannelDeciAmps09ALARM,
       "auxChannelDeciAmps10ALARM": auxChannelDeciAmps10ALARM,
       "auxChannelDeciAmps11ALARM": auxChannelDeciAmps11ALARM,
       "auxChannelDeciAmps12ALARM": auxChannelDeciAmps12ALARM,
       "auxChannelDeciAmps13ALARM": auxChannelDeciAmps13ALARM,
       "auxChannelDeciAmps14ALARM": auxChannelDeciAmps14ALARM,
       "auxChannelDeciAmps15ALARM": auxChannelDeciAmps15ALARM,
       "auxChannelDeciAmps16ALARM": auxChannelDeciAmps16ALARM,
       "auxChannelDeciAmps17ALARM": auxChannelDeciAmps17ALARM,
       "auxChannelDeciAmps18ALARM": auxChannelDeciAmps18ALARM,
       "auxChannelDeciAmps19ALARM": auxChannelDeciAmps19ALARM,
       "auxChannelDeciAmps20ALARM": auxChannelDeciAmps20ALARM,
       "auxChannelDeciAmps21ALARM": auxChannelDeciAmps21ALARM,
       "auxChannelDeciAmps22ALARM": auxChannelDeciAmps22ALARM,
       "auxChannelDeciAmps23ALARM": auxChannelDeciAmps23ALARM,
       "auxChannelDeciAmps24ALARM": auxChannelDeciAmps24ALARM,
       "auxChannelDeciAmps25ALARM": auxChannelDeciAmps25ALARM,
       "auxChannelDeciAmps26ALARM": auxChannelDeciAmps26ALARM,
       "auxChannelDeciAmps27ALARM": auxChannelDeciAmps27ALARM,
       "auxChannelDeciAmps28ALARM": auxChannelDeciAmps28ALARM,
       "auxChannelDeciAmps29ALARM": auxChannelDeciAmps29ALARM,
       "auxChannelDeciAmps30ALARM": auxChannelDeciAmps30ALARM,
       "auxChannelDeciAmps31ALARM": auxChannelDeciAmps31ALARM,
       "auxChannelDeciAmps32ALARM": auxChannelDeciAmps32ALARM,
       "mainChannelDeciAmps01WARN": mainChannelDeciAmps01WARN,
       "mainChannelDeciAmps02WARN": mainChannelDeciAmps02WARN,
       "mainChannelDeciAmps03WARN": mainChannelDeciAmps03WARN,
       "mainChannelDeciAmps04WARN": mainChannelDeciAmps04WARN,
       "mainChannelDeciAmps05WARN": mainChannelDeciAmps05WARN,
       "mainChannelDeciAmps06WARN": mainChannelDeciAmps06WARN,
       "mainChannelDeciAmps07WARN": mainChannelDeciAmps07WARN,
       "mainChannelDeciAmps08WARN": mainChannelDeciAmps08WARN,
       "auxChannelDeciAmps01WARN": auxChannelDeciAmps01WARN,
       "auxChannelDeciAmps02WARN": auxChannelDeciAmps02WARN,
       "auxChannelDeciAmps03WARN": auxChannelDeciAmps03WARN,
       "auxChannelDeciAmps04WARN": auxChannelDeciAmps04WARN,
       "auxChannelDeciAmps05WARN": auxChannelDeciAmps05WARN,
       "auxChannelDeciAmps06WARN": auxChannelDeciAmps06WARN,
       "auxChannelDeciAmps07WARN": auxChannelDeciAmps07WARN,
       "auxChannelDeciAmps08WARN": auxChannelDeciAmps08WARN,
       "auxChannelDeciAmps09WARN": auxChannelDeciAmps09WARN,
       "auxChannelDeciAmps10WARN": auxChannelDeciAmps10WARN,
       "auxChannelDeciAmps11WARN": auxChannelDeciAmps11WARN,
       "auxChannelDeciAmps12WARN": auxChannelDeciAmps12WARN,
       "auxChannelDeciAmps13WARN": auxChannelDeciAmps13WARN,
       "auxChannelDeciAmps14WARN": auxChannelDeciAmps14WARN,
       "auxChannelDeciAmps15WARN": auxChannelDeciAmps15WARN,
       "auxChannelDeciAmps16WARN": auxChannelDeciAmps16WARN,
       "auxChannelDeciAmps17WARN": auxChannelDeciAmps17WARN,
       "auxChannelDeciAmps18WARN": auxChannelDeciAmps18WARN,
       "auxChannelDeciAmps19WARN": auxChannelDeciAmps19WARN,
       "auxChannelDeciAmps20WARN": auxChannelDeciAmps20WARN,
       "auxChannelDeciAmps21WARN": auxChannelDeciAmps21WARN,
       "auxChannelDeciAmps22WARN": auxChannelDeciAmps22WARN,
       "auxChannelDeciAmps23WARN": auxChannelDeciAmps23WARN,
       "auxChannelDeciAmps24WARN": auxChannelDeciAmps24WARN,
       "auxChannelDeciAmps25WARN": auxChannelDeciAmps25WARN,
       "auxChannelDeciAmps26WARN": auxChannelDeciAmps26WARN,
       "auxChannelDeciAmps27WARN": auxChannelDeciAmps27WARN,
       "auxChannelDeciAmps28WARN": auxChannelDeciAmps28WARN,
       "auxChannelDeciAmps29WARN": auxChannelDeciAmps29WARN,
       "auxChannelDeciAmps30WARN": auxChannelDeciAmps30WARN,
       "auxChannelDeciAmps31WARN": auxChannelDeciAmps31WARN,
       "auxChannelDeciAmps32WARN": auxChannelDeciAmps32WARN,
       "unitInfo": unitInfo,
       "unitInfoTitle": unitInfoTitle,
       "unitInfoVersion": unitInfoVersion,
       "unitInfoName": unitInfoName,
       "unitInfoMAC": unitInfoMAC,
       "unitInfoIP": unitInfoIP,
       "unitInfoMainCount": unitInfoMainCount,
       "unitInfoAuxCount": unitInfoAuxCount,
       "unitInfoProductID": unitInfoProductID,
       "mainChannelTable": mainChannelTable,
       "mainChannelEntry": mainChannelEntry,
       "mainChannelIndex": mainChannelIndex,
       "mainChannelName": mainChannelName,
       "mainChannelFriendly": mainChannelFriendly,
       "mainChannelDeciAmps": mainChannelDeciAmps,
       "mainChannelGroup": mainChannelGroup,
       "auxChannelTable": auxChannelTable,
       "auxChannelEntry": auxChannelEntry,
       "auxChannelIndex": auxChannelIndex,
       "auxChannelName": auxChannelName,
       "auxChannelFriendly": auxChannelFriendly,
       "auxChannelDeciAmps": auxChannelDeciAmps,
       "auxChannelGroup": auxChannelGroup}
)
