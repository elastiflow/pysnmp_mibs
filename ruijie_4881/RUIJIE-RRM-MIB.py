# SNMP MIB module (RUIJIE-RRM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-RRM-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:02:06 2025
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ruijieRrmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63)
)
if mibBuilder.loadTexts:
    ruijieRrmMIB.setRevisions(
        ("2009-12-15 00:00",)
    )


# Types definitions



class ProfileState(Integer32):
    """Custom type ProfileState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("fail", 0),
          ("pass", 1))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieRrmMIBObjects_ObjectIdentity = ObjectIdentity
ruijieRrmMIBObjects = _RuijieRrmMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1)
)
_RuijieRrmObjectsGroup_ObjectIdentity = ObjectIdentity
ruijieRrmObjectsGroup = _RuijieRrmObjectsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 1)
)


class _RuijieRrmRFNetworkName_Type(DisplayString):
    """Custom type ruijieRrmRFNetworkName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 19),
    )


_RuijieRrmRFNetworkName_Type.__name__ = "DisplayString"
_RuijieRrmRFNetworkName_Object = MibScalar
ruijieRrmRFNetworkName = _RuijieRrmRFNetworkName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 1, 1),
    _RuijieRrmRFNetworkName_Type()
)
ruijieRrmRFNetworkName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmRFNetworkName.setStatus("current")
_RuijieRrmObjectsDot11a_ObjectIdentity = ObjectIdentity
ruijieRrmObjectsDot11a = _RuijieRrmObjectsDot11a_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 2)
)
_RuijieRrmDCADot11a_ObjectIdentity = ObjectIdentity
ruijieRrmDCADot11a = _RuijieRrmDCADot11a_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 2, 1)
)


class _RuijieRrmDot11aDynamicChannelAssignment_Type(Integer32):
    """Custom type ruijieRrmDot11aDynamicChannelAssignment based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("runOnce", 2),
          ("static", 3))
    )


_RuijieRrmDot11aDynamicChannelAssignment_Type.__name__ = "Integer32"
_RuijieRrmDot11aDynamicChannelAssignment_Object = MibScalar
ruijieRrmDot11aDynamicChannelAssignment = _RuijieRrmDot11aDynamicChannelAssignment_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 2, 1, 1),
    _RuijieRrmDot11aDynamicChannelAssignment_Type()
)
ruijieRrmDot11aDynamicChannelAssignment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmDot11aDynamicChannelAssignment.setStatus("current")


class _RuijieRrmDot11aAnchorTime_Type(Unsigned32):
    """Custom type ruijieRrmDot11aAnchorTime based on Unsigned32"""
    defaultValue = 0


_RuijieRrmDot11aAnchorTime_Type.__name__ = "Unsigned32"
_RuijieRrmDot11aAnchorTime_Object = MibScalar
ruijieRrmDot11aAnchorTime = _RuijieRrmDot11aAnchorTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 2, 1, 2),
    _RuijieRrmDot11aAnchorTime_Type()
)
ruijieRrmDot11aAnchorTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmDot11aAnchorTime.setStatus("current")


class _RuijieRrmDot11aChannalWidth11n_Type(Unsigned32):
    """Custom type ruijieRrmDot11aChannalWidth11n based on Unsigned32"""
    defaultValue = 20


_RuijieRrmDot11aChannalWidth11n_Type.__name__ = "Unsigned32"
_RuijieRrmDot11aChannalWidth11n_Object = MibScalar
ruijieRrmDot11aChannalWidth11n = _RuijieRrmDot11aChannalWidth11n_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 2, 1, 3),
    _RuijieRrmDot11aChannalWidth11n_Type()
)
ruijieRrmDot11aChannalWidth11n.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmDot11aChannalWidth11n.setStatus("current")


class _RuijieRrmDot11aDynamicChannelUpdateInterval_Type(Unsigned32):
    """Custom type ruijieRrmDot11aDynamicChannelUpdateInterval based on Unsigned32"""
    defaultValue = 600


_RuijieRrmDot11aDynamicChannelUpdateInterval_Type.__name__ = "Unsigned32"
_RuijieRrmDot11aDynamicChannelUpdateInterval_Object = MibScalar
ruijieRrmDot11aDynamicChannelUpdateInterval = _RuijieRrmDot11aDynamicChannelUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 2, 1, 4),
    _RuijieRrmDot11aDynamicChannelUpdateInterval_Type()
)
ruijieRrmDot11aDynamicChannelUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmDot11aDynamicChannelUpdateInterval.setStatus("current")


class _RuijieRrmDot11aDCASensitivity_Type(Integer32):
    """Custom type ruijieRrmDot11aDCASensitivity based on Integer32"""
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
        *(("low", 1),
          ("medium", 2),
          ("high", 3))
    )


_RuijieRrmDot11aDCASensitivity_Type.__name__ = "Integer32"
_RuijieRrmDot11aDCASensitivity_Object = MibScalar
ruijieRrmDot11aDCASensitivity = _RuijieRrmDot11aDCASensitivity_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 2, 1, 5),
    _RuijieRrmDot11aDCASensitivity_Type()
)
ruijieRrmDot11aDCASensitivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmDot11aDCASensitivity.setStatus("current")


class _RuijieRrmDot11aForeignInterfereFactorEnable_Type(Integer32):
    """Custom type ruijieRrmDot11aForeignInterfereFactorEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuijieRrmDot11aForeignInterfereFactorEnable_Type.__name__ = "Integer32"
_RuijieRrmDot11aForeignInterfereFactorEnable_Object = MibScalar
ruijieRrmDot11aForeignInterfereFactorEnable = _RuijieRrmDot11aForeignInterfereFactorEnable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 2, 1, 6),
    _RuijieRrmDot11aForeignInterfereFactorEnable_Type()
)
ruijieRrmDot11aForeignInterfereFactorEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmDot11aForeignInterfereFactorEnable.setStatus("current")


class _RuijieRrmDot11aLoadFactorEnable_Type(Integer32):
    """Custom type ruijieRrmDot11aLoadFactorEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuijieRrmDot11aLoadFactorEnable_Type.__name__ = "Integer32"
_RuijieRrmDot11aLoadFactorEnable_Object = MibScalar
ruijieRrmDot11aLoadFactorEnable = _RuijieRrmDot11aLoadFactorEnable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 2, 1, 7),
    _RuijieRrmDot11aLoadFactorEnable_Type()
)
ruijieRrmDot11aLoadFactorEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmDot11aLoadFactorEnable.setStatus("current")


class _RuijieRrmDot11aNoiseFactorEnable_Type(Integer32):
    """Custom type ruijieRrmDot11aNoiseFactorEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuijieRrmDot11aNoiseFactorEnable_Type.__name__ = "Integer32"
_RuijieRrmDot11aNoiseFactorEnable_Object = MibScalar
ruijieRrmDot11aNoiseFactorEnable = _RuijieRrmDot11aNoiseFactorEnable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 2, 1, 8),
    _RuijieRrmDot11aNoiseFactorEnable_Type()
)
ruijieRrmDot11aNoiseFactorEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmDot11aNoiseFactorEnable.setStatus("current")


class _RuijieRrmDot11aChannelUpdateCmdInvoke_Type(Integer32):
    """Custom type ruijieRrmDot11aChannelUpdateCmdInvoke based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("activate", 1))
    )


_RuijieRrmDot11aChannelUpdateCmdInvoke_Type.__name__ = "Integer32"
_RuijieRrmDot11aChannelUpdateCmdInvoke_Object = MibScalar
ruijieRrmDot11aChannelUpdateCmdInvoke = _RuijieRrmDot11aChannelUpdateCmdInvoke_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 2, 1, 9),
    _RuijieRrmDot11aChannelUpdateCmdInvoke_Type()
)
ruijieRrmDot11aChannelUpdateCmdInvoke.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmDot11aChannelUpdateCmdInvoke.setStatus("current")
_RuijieRrmDot11aDCAChannelTable_Object = MibTable
ruijieRrmDot11aDCAChannelTable = _RuijieRrmDot11aDCAChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 2, 1, 10)
)
if mibBuilder.loadTexts:
    ruijieRrmDot11aDCAChannelTable.setStatus("current")
_RuijieRrmDot11aDCAChannelEntry_Object = MibTableRow
ruijieRrmDot11aDCAChannelEntry = _RuijieRrmDot11aDCAChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 2, 1, 10, 1)
)
ruijieRrmDot11aDCAChannelEntry.setIndexNames(
    (0, "RUIJIE-RRM-MIB", "ruijieRrmDot11aDCAChannelIndex"),
)
if mibBuilder.loadTexts:
    ruijieRrmDot11aDCAChannelEntry.setStatus("current")
_RuijieRrmDot11aDCAChannelIndex_Type = Integer32
_RuijieRrmDot11aDCAChannelIndex_Object = MibTableColumn
ruijieRrmDot11aDCAChannelIndex = _RuijieRrmDot11aDCAChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 2, 1, 10, 1, 1),
    _RuijieRrmDot11aDCAChannelIndex_Type()
)
ruijieRrmDot11aDCAChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmDot11aDCAChannelIndex.setStatus("current")


class _RuijieRrmDot11aDCAChannelOperation_Type(Integer32):
    """Custom type ruijieRrmDot11aDCAChannelOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("delete", 0),
          ("add", 1))
    )


_RuijieRrmDot11aDCAChannelOperation_Type.__name__ = "Integer32"
_RuijieRrmDot11aDCAChannelOperation_Object = MibTableColumn
ruijieRrmDot11aDCAChannelOperation = _RuijieRrmDot11aDCAChannelOperation_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 2, 1, 10, 1, 2),
    _RuijieRrmDot11aDCAChannelOperation_Type()
)
ruijieRrmDot11aDCAChannelOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmDot11aDCAChannelOperation.setStatus("current")
_RuijieRrmTPCDot11a_ObjectIdentity = ObjectIdentity
ruijieRrmTPCDot11a = _RuijieRrmTPCDot11a_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 2, 2)
)


class _RuijieRrmDot11aDTPCSupport_Type(Integer32):
    """Custom type ruijieRrmDot11aDTPCSupport based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuijieRrmDot11aDTPCSupport_Type.__name__ = "Integer32"
_RuijieRrmDot11aDTPCSupport_Object = MibScalar
ruijieRrmDot11aDTPCSupport = _RuijieRrmDot11aDTPCSupport_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 2, 2, 1),
    _RuijieRrmDot11aDTPCSupport_Type()
)
ruijieRrmDot11aDTPCSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmDot11aDTPCSupport.setStatus("current")


class _RuijieRrmDot11aDynamicTransmitPowerControl_Type(Integer32):
    """Custom type ruijieRrmDot11aDynamicTransmitPowerControl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("runOnce", 2),
          ("static", 3))
    )


_RuijieRrmDot11aDynamicTransmitPowerControl_Type.__name__ = "Integer32"
_RuijieRrmDot11aDynamicTransmitPowerControl_Object = MibScalar
ruijieRrmDot11aDynamicTransmitPowerControl = _RuijieRrmDot11aDynamicTransmitPowerControl_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 2, 2, 2),
    _RuijieRrmDot11aDynamicTransmitPowerControl_Type()
)
ruijieRrmDot11aDynamicTransmitPowerControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmDot11aDynamicTransmitPowerControl.setStatus("current")


class _RuijieRrmDot11aDynamicTxPowerControlInterval_Type(Unsigned32):
    """Custom type ruijieRrmDot11aDynamicTxPowerControlInterval based on Unsigned32"""
    defaultValue = 600


_RuijieRrmDot11aDynamicTxPowerControlInterval_Type.__name__ = "Unsigned32"
_RuijieRrmDot11aDynamicTxPowerControlInterval_Object = MibScalar
ruijieRrmDot11aDynamicTxPowerControlInterval = _RuijieRrmDot11aDynamicTxPowerControlInterval_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 2, 2, 3),
    _RuijieRrmDot11aDynamicTxPowerControlInterval_Type()
)
ruijieRrmDot11aDynamicTxPowerControlInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmDot11aDynamicTxPowerControlInterval.setStatus("current")


class _RuijieRrmDot11aCurrentTxPowerLevel_Type(Integer32):
    """Custom type ruijieRrmDot11aCurrentTxPowerLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_RuijieRrmDot11aCurrentTxPowerLevel_Type.__name__ = "Integer32"
_RuijieRrmDot11aCurrentTxPowerLevel_Object = MibScalar
ruijieRrmDot11aCurrentTxPowerLevel = _RuijieRrmDot11aCurrentTxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 2, 2, 4),
    _RuijieRrmDot11aCurrentTxPowerLevel_Type()
)
ruijieRrmDot11aCurrentTxPowerLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmDot11aCurrentTxPowerLevel.setStatus("current")


class _RuijieRrmDot11aPowerUpdateCmdInvoke_Type(Integer32):
    """Custom type ruijieRrmDot11aPowerUpdateCmdInvoke based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("activate", 1))
    )


_RuijieRrmDot11aPowerUpdateCmdInvoke_Type.__name__ = "Integer32"
_RuijieRrmDot11aPowerUpdateCmdInvoke_Object = MibScalar
ruijieRrmDot11aPowerUpdateCmdInvoke = _RuijieRrmDot11aPowerUpdateCmdInvoke_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 2, 2, 5),
    _RuijieRrmDot11aPowerUpdateCmdInvoke_Type()
)
ruijieRrmDot11aPowerUpdateCmdInvoke.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmDot11aPowerUpdateCmdInvoke.setStatus("current")


class _RuijieRrmDot11aTXPowerThreshold_Type(Integer32):
    """Custom type ruijieRrmDot11aTXPowerThreshold based on Integer32"""
    defaultValue = -70

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-90, -60),
    )


_RuijieRrmDot11aTXPowerThreshold_Type.__name__ = "Integer32"
_RuijieRrmDot11aTXPowerThreshold_Object = MibScalar
ruijieRrmDot11aTXPowerThreshold = _RuijieRrmDot11aTXPowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 2, 2, 6),
    _RuijieRrmDot11aTXPowerThreshold_Type()
)
ruijieRrmDot11aTXPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmDot11aTXPowerThreshold.setStatus("current")


class _RuijieRrmDot11aTPCNeighborNumber_Type(Integer32):
    """Custom type ruijieRrmDot11aTPCNeighborNumber based on Integer32"""
    defaultValue = 3


_RuijieRrmDot11aTPCNeighborNumber_Type.__name__ = "Integer32"
_RuijieRrmDot11aTPCNeighborNumber_Object = MibScalar
ruijieRrmDot11aTPCNeighborNumber = _RuijieRrmDot11aTPCNeighborNumber_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 2, 2, 7),
    _RuijieRrmDot11aTPCNeighborNumber_Type()
)
ruijieRrmDot11aTPCNeighborNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmDot11aTPCNeighborNumber.setStatus("current")
_RuijieRrmCHDDot11a_ObjectIdentity = ObjectIdentity
ruijieRrmCHDDot11a = _RuijieRrmCHDDot11a_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 2, 3)
)


class _RuijieRrmDot11aCoverageEnable_Type(Integer32):
    """Custom type ruijieRrmDot11aCoverageEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuijieRrmDot11aCoverageEnable_Type.__name__ = "Integer32"
_RuijieRrmDot11aCoverageEnable_Object = MibScalar
ruijieRrmDot11aCoverageEnable = _RuijieRrmDot11aCoverageEnable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 2, 3, 1),
    _RuijieRrmDot11aCoverageEnable_Type()
)
ruijieRrmDot11aCoverageEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmDot11aCoverageEnable.setStatus("current")


class _RuijieRrmDot11aCoverageExceptionGlobal_Type(Integer32):
    """Custom type ruijieRrmDot11aCoverageExceptionGlobal based on Integer32"""
    defaultValue = 25

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RuijieRrmDot11aCoverageExceptionGlobal_Type.__name__ = "Integer32"
_RuijieRrmDot11aCoverageExceptionGlobal_Object = MibScalar
ruijieRrmDot11aCoverageExceptionGlobal = _RuijieRrmDot11aCoverageExceptionGlobal_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 2, 3, 2),
    _RuijieRrmDot11aCoverageExceptionGlobal_Type()
)
ruijieRrmDot11aCoverageExceptionGlobal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmDot11aCoverageExceptionGlobal.setStatus("current")


class _RuijieRrmDot11aCoverageLevelGlobal_Type(Integer32):
    """Custom type ruijieRrmDot11aCoverageLevelGlobal based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 75),
    )


_RuijieRrmDot11aCoverageLevelGlobal_Type.__name__ = "Integer32"
_RuijieRrmDot11aCoverageLevelGlobal_Object = MibScalar
ruijieRrmDot11aCoverageLevelGlobal = _RuijieRrmDot11aCoverageLevelGlobal_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 2, 3, 3),
    _RuijieRrmDot11aCoverageLevelGlobal_Type()
)
ruijieRrmDot11aCoverageLevelGlobal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmDot11aCoverageLevelGlobal.setStatus("current")


class _RuijieRrmDot11aCoverageDataRSSIThreshold_Type(Integer32):
    """Custom type ruijieRrmDot11aCoverageDataRSSIThreshold based on Integer32"""
    defaultValue = -80

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-90, -60),
    )


_RuijieRrmDot11aCoverageDataRSSIThreshold_Type.__name__ = "Integer32"
_RuijieRrmDot11aCoverageDataRSSIThreshold_Object = MibScalar
ruijieRrmDot11aCoverageDataRSSIThreshold = _RuijieRrmDot11aCoverageDataRSSIThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 2, 3, 4),
    _RuijieRrmDot11aCoverageDataRSSIThreshold_Type()
)
ruijieRrmDot11aCoverageDataRSSIThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmDot11aCoverageDataRSSIThreshold.setStatus("current")


class _RuijieRrmDot11aCoverageVoiceRSSIThreshold_Type(Integer32):
    """Custom type ruijieRrmDot11aCoverageVoiceRSSIThreshold based on Integer32"""
    defaultValue = -75

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-90, -60),
    )


_RuijieRrmDot11aCoverageVoiceRSSIThreshold_Type.__name__ = "Integer32"
_RuijieRrmDot11aCoverageVoiceRSSIThreshold_Object = MibScalar
ruijieRrmDot11aCoverageVoiceRSSIThreshold = _RuijieRrmDot11aCoverageVoiceRSSIThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 2, 3, 5),
    _RuijieRrmDot11aCoverageVoiceRSSIThreshold_Type()
)
ruijieRrmDot11aCoverageVoiceRSSIThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmDot11aCoverageVoiceRSSIThreshold.setStatus("current")


class _RuijieRrmDot11aCoverageDataPacketCount_Type(Integer32):
    """Custom type ruijieRrmDot11aCoverageDataPacketCount based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RuijieRrmDot11aCoverageDataPacketCount_Type.__name__ = "Integer32"
_RuijieRrmDot11aCoverageDataPacketCount_Object = MibScalar
ruijieRrmDot11aCoverageDataPacketCount = _RuijieRrmDot11aCoverageDataPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 2, 3, 6),
    _RuijieRrmDot11aCoverageDataPacketCount_Type()
)
ruijieRrmDot11aCoverageDataPacketCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmDot11aCoverageDataPacketCount.setStatus("current")


class _RuijieRrmDot11aCoverageVoicePacketCount_Type(Integer32):
    """Custom type ruijieRrmDot11aCoverageVoicePacketCount based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RuijieRrmDot11aCoverageVoicePacketCount_Type.__name__ = "Integer32"
_RuijieRrmDot11aCoverageVoicePacketCount_Object = MibScalar
ruijieRrmDot11aCoverageVoicePacketCount = _RuijieRrmDot11aCoverageVoicePacketCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 2, 3, 7),
    _RuijieRrmDot11aCoverageVoicePacketCount_Type()
)
ruijieRrmDot11aCoverageVoicePacketCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmDot11aCoverageVoicePacketCount.setStatus("current")


class _RuijieRrmDot11aCoverageDataFailRate_Type(Integer32):
    """Custom type ruijieRrmDot11aCoverageDataFailRate based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RuijieRrmDot11aCoverageDataFailRate_Type.__name__ = "Integer32"
_RuijieRrmDot11aCoverageDataFailRate_Object = MibScalar
ruijieRrmDot11aCoverageDataFailRate = _RuijieRrmDot11aCoverageDataFailRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 2, 3, 8),
    _RuijieRrmDot11aCoverageDataFailRate_Type()
)
ruijieRrmDot11aCoverageDataFailRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmDot11aCoverageDataFailRate.setStatus("current")


class _RuijieRrmDot11aCoverageVoiceFailRate_Type(Integer32):
    """Custom type ruijieRrmDot11aCoverageVoiceFailRate based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RuijieRrmDot11aCoverageVoiceFailRate_Type.__name__ = "Integer32"
_RuijieRrmDot11aCoverageVoiceFailRate_Object = MibScalar
ruijieRrmDot11aCoverageVoiceFailRate = _RuijieRrmDot11aCoverageVoiceFailRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 2, 3, 9),
    _RuijieRrmDot11aCoverageVoiceFailRate_Type()
)
ruijieRrmDot11aCoverageVoiceFailRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmDot11aCoverageVoiceFailRate.setStatus("current")
_RuijieRrmGroupDot11a_ObjectIdentity = ObjectIdentity
ruijieRrmGroupDot11a = _RuijieRrmGroupDot11a_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 2, 4)
)


class _RuijieRrmDot11aGlobalAutomaticGrouping_Type(Integer32):
    """Custom type ruijieRrmDot11aGlobalAutomaticGrouping based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("automatic", 1))
    )


_RuijieRrmDot11aGlobalAutomaticGrouping_Type.__name__ = "Integer32"
_RuijieRrmDot11aGlobalAutomaticGrouping_Object = MibScalar
ruijieRrmDot11aGlobalAutomaticGrouping = _RuijieRrmDot11aGlobalAutomaticGrouping_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 2, 4, 1),
    _RuijieRrmDot11aGlobalAutomaticGrouping_Type()
)
ruijieRrmDot11aGlobalAutomaticGrouping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmDot11aGlobalAutomaticGrouping.setStatus("current")
_RuijieRrmDot11aGroupLeaderMacAddr_Type = MacAddress
_RuijieRrmDot11aGroupLeaderMacAddr_Object = MibScalar
ruijieRrmDot11aGroupLeaderMacAddr = _RuijieRrmDot11aGroupLeaderMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 2, 4, 2),
    _RuijieRrmDot11aGroupLeaderMacAddr_Type()
)
ruijieRrmDot11aGroupLeaderMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmDot11aGroupLeaderMacAddr.setStatus("current")


class _RuijieRrmDot11aGroupLeader_Type(Integer32):
    """Custom type ruijieRrmDot11aGroupLeader based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_RuijieRrmDot11aGroupLeader_Type.__name__ = "Integer32"
_RuijieRrmDot11aGroupLeader_Object = MibScalar
ruijieRrmDot11aGroupLeader = _RuijieRrmDot11aGroupLeader_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 2, 4, 3),
    _RuijieRrmDot11aGroupLeader_Type()
)
ruijieRrmDot11aGroupLeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmDot11aGroupLeader.setStatus("current")
_RuijieRrmDot11aGroupLastUpdateTime_Type = Unsigned32
_RuijieRrmDot11aGroupLastUpdateTime_Object = MibScalar
ruijieRrmDot11aGroupLastUpdateTime = _RuijieRrmDot11aGroupLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 2, 4, 4),
    _RuijieRrmDot11aGroupLastUpdateTime_Type()
)
ruijieRrmDot11aGroupLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmDot11aGroupLastUpdateTime.setStatus("current")


class _RuijieRrmDot11aGroupInterval_Type(Unsigned32):
    """Custom type ruijieRrmDot11aGroupInterval based on Unsigned32"""
    defaultValue = 3600


_RuijieRrmDot11aGroupInterval_Type.__name__ = "Unsigned32"
_RuijieRrmDot11aGroupInterval_Object = MibScalar
ruijieRrmDot11aGroupInterval = _RuijieRrmDot11aGroupInterval_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 2, 4, 5),
    _RuijieRrmDot11aGroupInterval_Type()
)
ruijieRrmDot11aGroupInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmDot11aGroupInterval.setStatus("current")
_RuijieRrmDot11aGroupTable_Object = MibTable
ruijieRrmDot11aGroupTable = _RuijieRrmDot11aGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 2, 4, 6)
)
if mibBuilder.loadTexts:
    ruijieRrmDot11aGroupTable.setStatus("current")
_RuijieRrmDot11aGroupEntry_Object = MibTableRow
ruijieRrmDot11aGroupEntry = _RuijieRrmDot11aGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 2, 4, 6, 1)
)
ruijieRrmDot11aGroupEntry.setIndexNames(
    (0, "RUIJIE-RRM-MIB", "ruijieRrmDot11aPeerMacAddress"),
)
if mibBuilder.loadTexts:
    ruijieRrmDot11aGroupEntry.setStatus("current")
_RuijieRrmDot11aPeerMacAddress_Type = MacAddress
_RuijieRrmDot11aPeerMacAddress_Object = MibTableColumn
ruijieRrmDot11aPeerMacAddress = _RuijieRrmDot11aPeerMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 2, 4, 6, 1, 1),
    _RuijieRrmDot11aPeerMacAddress_Type()
)
ruijieRrmDot11aPeerMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmDot11aPeerMacAddress.setStatus("current")
_RuijieRrmDot11aPeerIpAddress_Type = IpAddress
_RuijieRrmDot11aPeerIpAddress_Object = MibTableColumn
ruijieRrmDot11aPeerIpAddress = _RuijieRrmDot11aPeerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 2, 4, 6, 1, 2),
    _RuijieRrmDot11aPeerIpAddress_Type()
)
ruijieRrmDot11aPeerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmDot11aPeerIpAddress.setStatus("current")
_RuijieRrmDot11aSummaryTable_Object = MibTable
ruijieRrmDot11aSummaryTable = _RuijieRrmDot11aSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 2, 4, 7)
)
if mibBuilder.loadTexts:
    ruijieRrmDot11aSummaryTable.setStatus("current")
_RuijieRrmDot11aSummaryEntry_Object = MibTableRow
ruijieRrmDot11aSummaryEntry = _RuijieRrmDot11aSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 2, 4, 7, 1)
)
ruijieRrmDot11aSummaryEntry.setIndexNames(
    (0, "RUIJIE-RRM-MIB", "ruijieRrmDot11aSummaryMacAddress"),
    (0, "RUIJIE-RRM-MIB", "ruijieRrmDot11aAPRadioID"),
)
if mibBuilder.loadTexts:
    ruijieRrmDot11aSummaryEntry.setStatus("current")
_RuijieRrmDot11aAPname_Type = DisplayString
_RuijieRrmDot11aAPname_Object = MibTableColumn
ruijieRrmDot11aAPname = _RuijieRrmDot11aAPname_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 2, 4, 7, 1, 1),
    _RuijieRrmDot11aAPname_Type()
)
ruijieRrmDot11aAPname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmDot11aAPname.setStatus("current")
_RuijieRrmDot11aAPRadioID_Type = Unsigned32
_RuijieRrmDot11aAPRadioID_Object = MibTableColumn
ruijieRrmDot11aAPRadioID = _RuijieRrmDot11aAPRadioID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 2, 4, 7, 1, 2),
    _RuijieRrmDot11aAPRadioID_Type()
)
ruijieRrmDot11aAPRadioID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmDot11aAPRadioID.setStatus("current")
_RuijieRrmDot11aAPChannel_Type = Unsigned32
_RuijieRrmDot11aAPChannel_Object = MibTableColumn
ruijieRrmDot11aAPChannel = _RuijieRrmDot11aAPChannel_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 2, 4, 7, 1, 3),
    _RuijieRrmDot11aAPChannel_Type()
)
ruijieRrmDot11aAPChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmDot11aAPChannel.setStatus("current")
_RuijieRrmDot11aAPTxPower_Type = Unsigned32
_RuijieRrmDot11aAPTxPower_Object = MibTableColumn
ruijieRrmDot11aAPTxPower = _RuijieRrmDot11aAPTxPower_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 2, 4, 7, 1, 4),
    _RuijieRrmDot11aAPTxPower_Type()
)
ruijieRrmDot11aAPTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmDot11aAPTxPower.setStatus("current")


class _RuijieRrmDot11aAPChannelRrmChangeFlag_Type(Integer32):
    """Custom type ruijieRrmDot11aAPChannelRrmChangeFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_RuijieRrmDot11aAPChannelRrmChangeFlag_Type.__name__ = "Integer32"
_RuijieRrmDot11aAPChannelRrmChangeFlag_Object = MibTableColumn
ruijieRrmDot11aAPChannelRrmChangeFlag = _RuijieRrmDot11aAPChannelRrmChangeFlag_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 2, 4, 7, 1, 5),
    _RuijieRrmDot11aAPChannelRrmChangeFlag_Type()
)
ruijieRrmDot11aAPChannelRrmChangeFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmDot11aAPChannelRrmChangeFlag.setStatus("current")


class _RuijieRrmDot11aAPTxPowerRrmChangeFlag_Type(Integer32):
    """Custom type ruijieRrmDot11aAPTxPowerRrmChangeFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_RuijieRrmDot11aAPTxPowerRrmChangeFlag_Type.__name__ = "Integer32"
_RuijieRrmDot11aAPTxPowerRrmChangeFlag_Object = MibTableColumn
ruijieRrmDot11aAPTxPowerRrmChangeFlag = _RuijieRrmDot11aAPTxPowerRrmChangeFlag_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 2, 4, 7, 1, 6),
    _RuijieRrmDot11aAPTxPowerRrmChangeFlag_Type()
)
ruijieRrmDot11aAPTxPowerRrmChangeFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmDot11aAPTxPowerRrmChangeFlag.setStatus("current")
_RuijieRrmDot11aSummaryMacAddress_Type = MacAddress
_RuijieRrmDot11aSummaryMacAddress_Object = MibTableColumn
ruijieRrmDot11aSummaryMacAddress = _RuijieRrmDot11aSummaryMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 2, 4, 7, 1, 7),
    _RuijieRrmDot11aSummaryMacAddress_Type()
)
ruijieRrmDot11aSummaryMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmDot11aSummaryMacAddress.setStatus("current")
_RuijieRrmProfileDot11a_ObjectIdentity = ObjectIdentity
ruijieRrmProfileDot11a = _RuijieRrmProfileDot11a_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 2, 5)
)


class _RuijieRrmDot11aForeignInterferenceThreshold_Type(Integer32):
    """Custom type ruijieRrmDot11aForeignInterferenceThreshold based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RuijieRrmDot11aForeignInterferenceThreshold_Type.__name__ = "Integer32"
_RuijieRrmDot11aForeignInterferenceThreshold_Object = MibScalar
ruijieRrmDot11aForeignInterferenceThreshold = _RuijieRrmDot11aForeignInterferenceThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 2, 5, 1),
    _RuijieRrmDot11aForeignInterferenceThreshold_Type()
)
ruijieRrmDot11aForeignInterferenceThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmDot11aForeignInterferenceThreshold.setStatus("current")


class _RuijieRrmDot11aForeignNoiseThreshold_Type(Integer32):
    """Custom type ruijieRrmDot11aForeignNoiseThreshold based on Integer32"""
    defaultValue = -70

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-127, 0),
    )


_RuijieRrmDot11aForeignNoiseThreshold_Type.__name__ = "Integer32"
_RuijieRrmDot11aForeignNoiseThreshold_Object = MibScalar
ruijieRrmDot11aForeignNoiseThreshold = _RuijieRrmDot11aForeignNoiseThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 2, 5, 2),
    _RuijieRrmDot11aForeignNoiseThreshold_Type()
)
ruijieRrmDot11aForeignNoiseThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmDot11aForeignNoiseThreshold.setStatus("current")


class _RuijieRrmDot11aRFUtilizationThreshold_Type(Integer32):
    """Custom type ruijieRrmDot11aRFUtilizationThreshold based on Integer32"""
    defaultValue = 80

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RuijieRrmDot11aRFUtilizationThreshold_Type.__name__ = "Integer32"
_RuijieRrmDot11aRFUtilizationThreshold_Object = MibScalar
ruijieRrmDot11aRFUtilizationThreshold = _RuijieRrmDot11aRFUtilizationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 2, 5, 3),
    _RuijieRrmDot11aRFUtilizationThreshold_Type()
)
ruijieRrmDot11aRFUtilizationThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmDot11aRFUtilizationThreshold.setStatus("current")


class _RuijieRrmDot11aThroughputThreshold_Type(Unsigned32):
    """Custom type ruijieRrmDot11aThroughputThreshold based on Unsigned32"""
    defaultValue = 1000000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 10000000),
    )


_RuijieRrmDot11aThroughputThreshold_Type.__name__ = "Unsigned32"
_RuijieRrmDot11aThroughputThreshold_Object = MibScalar
ruijieRrmDot11aThroughputThreshold = _RuijieRrmDot11aThroughputThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 2, 5, 4),
    _RuijieRrmDot11aThroughputThreshold_Type()
)
ruijieRrmDot11aThroughputThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmDot11aThroughputThreshold.setStatus("current")


class _RuijieRrmDot11aMobilesThreshold_Type(Integer32):
    """Custom type ruijieRrmDot11aMobilesThreshold based on Integer32"""
    defaultValue = 12

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 75),
    )


_RuijieRrmDot11aMobilesThreshold_Type.__name__ = "Integer32"
_RuijieRrmDot11aMobilesThreshold_Object = MibScalar
ruijieRrmDot11aMobilesThreshold = _RuijieRrmDot11aMobilesThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 2, 5, 5),
    _RuijieRrmDot11aMobilesThreshold_Type()
)
ruijieRrmDot11aMobilesThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmDot11aMobilesThreshold.setStatus("current")
_RuijieRrmMonitorDot11a_ObjectIdentity = ObjectIdentity
ruijieRrmMonitorDot11a = _RuijieRrmMonitorDot11a_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 2, 6)
)


class _RuijieRrmDot11aMonitorEnable_Type(Integer32):
    """Custom type ruijieRrmDot11aMonitorEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuijieRrmDot11aMonitorEnable_Type.__name__ = "Integer32"
_RuijieRrmDot11aMonitorEnable_Object = MibScalar
ruijieRrmDot11aMonitorEnable = _RuijieRrmDot11aMonitorEnable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 2, 6, 1),
    _RuijieRrmDot11aMonitorEnable_Type()
)
ruijieRrmDot11aMonitorEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmDot11aMonitorEnable.setStatus("current")


class _RuijieRrmDot11aChannelMonitorList_Type(Integer32):
    """Custom type ruijieRrmDot11aChannelMonitorList based on Integer32"""
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
        *(("all", 1),
          ("country", 2),
          ("dca", 3))
    )


_RuijieRrmDot11aChannelMonitorList_Type.__name__ = "Integer32"
_RuijieRrmDot11aChannelMonitorList_Object = MibScalar
ruijieRrmDot11aChannelMonitorList = _RuijieRrmDot11aChannelMonitorList_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 2, 6, 2),
    _RuijieRrmDot11aChannelMonitorList_Type()
)
ruijieRrmDot11aChannelMonitorList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmDot11aChannelMonitorList.setStatus("current")


class _RuijieRrmDot11aMonitorInterval_Type(Unsigned32):
    """Custom type ruijieRrmDot11aMonitorInterval based on Unsigned32"""
    defaultValue = 180

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_RuijieRrmDot11aMonitorInterval_Type.__name__ = "Unsigned32"
_RuijieRrmDot11aMonitorInterval_Object = MibScalar
ruijieRrmDot11aMonitorInterval = _RuijieRrmDot11aMonitorInterval_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 2, 6, 3),
    _RuijieRrmDot11aMonitorInterval_Type()
)
ruijieRrmDot11aMonitorInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmDot11aMonitorInterval.setStatus("current")


class _RuijieRrmDot11aCoverageMeasurementInterval_Type(Unsigned32):
    """Custom type ruijieRrmDot11aCoverageMeasurementInterval based on Unsigned32"""
    defaultValue = 180

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_RuijieRrmDot11aCoverageMeasurementInterval_Type.__name__ = "Unsigned32"
_RuijieRrmDot11aCoverageMeasurementInterval_Object = MibScalar
ruijieRrmDot11aCoverageMeasurementInterval = _RuijieRrmDot11aCoverageMeasurementInterval_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 2, 6, 4),
    _RuijieRrmDot11aCoverageMeasurementInterval_Type()
)
ruijieRrmDot11aCoverageMeasurementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmDot11aCoverageMeasurementInterval.setStatus("current")


class _RuijieRrmDot11aLoadMeasurementInterval_Type(Unsigned32):
    """Custom type ruijieRrmDot11aLoadMeasurementInterval based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_RuijieRrmDot11aLoadMeasurementInterval_Type.__name__ = "Unsigned32"
_RuijieRrmDot11aLoadMeasurementInterval_Object = MibScalar
ruijieRrmDot11aLoadMeasurementInterval = _RuijieRrmDot11aLoadMeasurementInterval_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 2, 6, 5),
    _RuijieRrmDot11aLoadMeasurementInterval_Type()
)
ruijieRrmDot11aLoadMeasurementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmDot11aLoadMeasurementInterval.setStatus("current")


class _RuijieRrmDot11aNoiseMeasurementInterval_Type(Unsigned32):
    """Custom type ruijieRrmDot11aNoiseMeasurementInterval based on Unsigned32"""
    defaultValue = 180

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_RuijieRrmDot11aNoiseMeasurementInterval_Type.__name__ = "Unsigned32"
_RuijieRrmDot11aNoiseMeasurementInterval_Object = MibScalar
ruijieRrmDot11aNoiseMeasurementInterval = _RuijieRrmDot11aNoiseMeasurementInterval_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 2, 6, 6),
    _RuijieRrmDot11aNoiseMeasurementInterval_Type()
)
ruijieRrmDot11aNoiseMeasurementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmDot11aNoiseMeasurementInterval.setStatus("current")


class _RuijieRrmDot11aSignalMeasurementInterval_Type(Unsigned32):
    """Custom type ruijieRrmDot11aSignalMeasurementInterval based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_RuijieRrmDot11aSignalMeasurementInterval_Type.__name__ = "Unsigned32"
_RuijieRrmDot11aSignalMeasurementInterval_Object = MibScalar
ruijieRrmDot11aSignalMeasurementInterval = _RuijieRrmDot11aSignalMeasurementInterval_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 2, 6, 7),
    _RuijieRrmDot11aSignalMeasurementInterval_Type()
)
ruijieRrmDot11aSignalMeasurementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmDot11aSignalMeasurementInterval.setStatus("current")


class _RuijieRrmDot11aNeighborMessageInterval_Type(Unsigned32):
    """Custom type ruijieRrmDot11aNeighborMessageInterval based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_RuijieRrmDot11aNeighborMessageInterval_Type.__name__ = "Unsigned32"
_RuijieRrmDot11aNeighborMessageInterval_Object = MibScalar
ruijieRrmDot11aNeighborMessageInterval = _RuijieRrmDot11aNeighborMessageInterval_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 2, 6, 8),
    _RuijieRrmDot11aNeighborMessageInterval_Type()
)
ruijieRrmDot11aNeighborMessageInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmDot11aNeighborMessageInterval.setStatus("current")
_RuijieRrmFactoryDot11a_ObjectIdentity = ObjectIdentity
ruijieRrmFactoryDot11a = _RuijieRrmFactoryDot11a_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 2, 7)
)


class _RuijieRrmDot11aSetFactoryDefault_Type(Integer32):
    """Custom type ruijieRrmDot11aSetFactoryDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("activate", 1))
    )


_RuijieRrmDot11aSetFactoryDefault_Type.__name__ = "Integer32"
_RuijieRrmDot11aSetFactoryDefault_Object = MibScalar
ruijieRrmDot11aSetFactoryDefault = _RuijieRrmDot11aSetFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 2, 7, 1),
    _RuijieRrmDot11aSetFactoryDefault_Type()
)
ruijieRrmDot11aSetFactoryDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmDot11aSetFactoryDefault.setStatus("current")
_RuijieRrmObjectsDot11b_ObjectIdentity = ObjectIdentity
ruijieRrmObjectsDot11b = _RuijieRrmObjectsDot11b_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 3)
)
_RuijieRrmDCADot11b_ObjectIdentity = ObjectIdentity
ruijieRrmDCADot11b = _RuijieRrmDCADot11b_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 3, 1)
)


class _RuijieRrmDot11bDynamicChannelAssignment_Type(Integer32):
    """Custom type ruijieRrmDot11bDynamicChannelAssignment based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("runOnce", 2),
          ("static", 3))
    )


_RuijieRrmDot11bDynamicChannelAssignment_Type.__name__ = "Integer32"
_RuijieRrmDot11bDynamicChannelAssignment_Object = MibScalar
ruijieRrmDot11bDynamicChannelAssignment = _RuijieRrmDot11bDynamicChannelAssignment_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 3, 1, 1),
    _RuijieRrmDot11bDynamicChannelAssignment_Type()
)
ruijieRrmDot11bDynamicChannelAssignment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmDot11bDynamicChannelAssignment.setStatus("current")


class _RuijieRrmDot11bAnchorTime_Type(Unsigned32):
    """Custom type ruijieRrmDot11bAnchorTime based on Unsigned32"""
    defaultValue = 0


_RuijieRrmDot11bAnchorTime_Type.__name__ = "Unsigned32"
_RuijieRrmDot11bAnchorTime_Object = MibScalar
ruijieRrmDot11bAnchorTime = _RuijieRrmDot11bAnchorTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 3, 1, 2),
    _RuijieRrmDot11bAnchorTime_Type()
)
ruijieRrmDot11bAnchorTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmDot11bAnchorTime.setStatus("current")


class _RuijieRrmDot11bChannalWidth11n_Type(Unsigned32):
    """Custom type ruijieRrmDot11bChannalWidth11n based on Unsigned32"""
    defaultValue = 20


_RuijieRrmDot11bChannalWidth11n_Type.__name__ = "Unsigned32"
_RuijieRrmDot11bChannalWidth11n_Object = MibScalar
ruijieRrmDot11bChannalWidth11n = _RuijieRrmDot11bChannalWidth11n_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 3, 1, 3),
    _RuijieRrmDot11bChannalWidth11n_Type()
)
ruijieRrmDot11bChannalWidth11n.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmDot11bChannalWidth11n.setStatus("current")


class _RuijieRrmDot11bDynamicChannelUpdateInterval_Type(Unsigned32):
    """Custom type ruijieRrmDot11bDynamicChannelUpdateInterval based on Unsigned32"""
    defaultValue = 600


_RuijieRrmDot11bDynamicChannelUpdateInterval_Type.__name__ = "Unsigned32"
_RuijieRrmDot11bDynamicChannelUpdateInterval_Object = MibScalar
ruijieRrmDot11bDynamicChannelUpdateInterval = _RuijieRrmDot11bDynamicChannelUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 3, 1, 4),
    _RuijieRrmDot11bDynamicChannelUpdateInterval_Type()
)
ruijieRrmDot11bDynamicChannelUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmDot11bDynamicChannelUpdateInterval.setStatus("current")


class _RuijieRrmDot11bDCASensitivity_Type(Integer32):
    """Custom type ruijieRrmDot11bDCASensitivity based on Integer32"""
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
        *(("low", 1),
          ("medium", 2),
          ("high", 3))
    )


_RuijieRrmDot11bDCASensitivity_Type.__name__ = "Integer32"
_RuijieRrmDot11bDCASensitivity_Object = MibScalar
ruijieRrmDot11bDCASensitivity = _RuijieRrmDot11bDCASensitivity_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 3, 1, 5),
    _RuijieRrmDot11bDCASensitivity_Type()
)
ruijieRrmDot11bDCASensitivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmDot11bDCASensitivity.setStatus("current")


class _RuijieRrmDot11bForeignInterfereFactorEnable_Type(Integer32):
    """Custom type ruijieRrmDot11bForeignInterfereFactorEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuijieRrmDot11bForeignInterfereFactorEnable_Type.__name__ = "Integer32"
_RuijieRrmDot11bForeignInterfereFactorEnable_Object = MibScalar
ruijieRrmDot11bForeignInterfereFactorEnable = _RuijieRrmDot11bForeignInterfereFactorEnable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 3, 1, 6),
    _RuijieRrmDot11bForeignInterfereFactorEnable_Type()
)
ruijieRrmDot11bForeignInterfereFactorEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmDot11bForeignInterfereFactorEnable.setStatus("current")


class _RuijieRrmDot11bLoadFactorEnable_Type(Integer32):
    """Custom type ruijieRrmDot11bLoadFactorEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuijieRrmDot11bLoadFactorEnable_Type.__name__ = "Integer32"
_RuijieRrmDot11bLoadFactorEnable_Object = MibScalar
ruijieRrmDot11bLoadFactorEnable = _RuijieRrmDot11bLoadFactorEnable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 3, 1, 7),
    _RuijieRrmDot11bLoadFactorEnable_Type()
)
ruijieRrmDot11bLoadFactorEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmDot11bLoadFactorEnable.setStatus("current")


class _RuijieRrmDot11bNoiseFactorEnable_Type(Integer32):
    """Custom type ruijieRrmDot11bNoiseFactorEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuijieRrmDot11bNoiseFactorEnable_Type.__name__ = "Integer32"
_RuijieRrmDot11bNoiseFactorEnable_Object = MibScalar
ruijieRrmDot11bNoiseFactorEnable = _RuijieRrmDot11bNoiseFactorEnable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 3, 1, 8),
    _RuijieRrmDot11bNoiseFactorEnable_Type()
)
ruijieRrmDot11bNoiseFactorEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmDot11bNoiseFactorEnable.setStatus("current")


class _RuijieRrmDot11bChannelUpdateCmdInvoke_Type(Integer32):
    """Custom type ruijieRrmDot11bChannelUpdateCmdInvoke based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("activate", 1))
    )


_RuijieRrmDot11bChannelUpdateCmdInvoke_Type.__name__ = "Integer32"
_RuijieRrmDot11bChannelUpdateCmdInvoke_Object = MibScalar
ruijieRrmDot11bChannelUpdateCmdInvoke = _RuijieRrmDot11bChannelUpdateCmdInvoke_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 3, 1, 9),
    _RuijieRrmDot11bChannelUpdateCmdInvoke_Type()
)
ruijieRrmDot11bChannelUpdateCmdInvoke.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmDot11bChannelUpdateCmdInvoke.setStatus("current")
_RuijieRrmDot11bDCAChannelTable_Object = MibTable
ruijieRrmDot11bDCAChannelTable = _RuijieRrmDot11bDCAChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 3, 1, 10)
)
if mibBuilder.loadTexts:
    ruijieRrmDot11bDCAChannelTable.setStatus("current")
_RuijieRrmDot11bDCAChannelEntry_Object = MibTableRow
ruijieRrmDot11bDCAChannelEntry = _RuijieRrmDot11bDCAChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 3, 1, 10, 1)
)
ruijieRrmDot11bDCAChannelEntry.setIndexNames(
    (0, "RUIJIE-RRM-MIB", "ruijieRrmDot11bDCAChannelIndex"),
)
if mibBuilder.loadTexts:
    ruijieRrmDot11bDCAChannelEntry.setStatus("current")
_RuijieRrmDot11bDCAChannelIndex_Type = Integer32
_RuijieRrmDot11bDCAChannelIndex_Object = MibTableColumn
ruijieRrmDot11bDCAChannelIndex = _RuijieRrmDot11bDCAChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 3, 1, 10, 1, 1),
    _RuijieRrmDot11bDCAChannelIndex_Type()
)
ruijieRrmDot11bDCAChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmDot11bDCAChannelIndex.setStatus("current")


class _RuijieRrmDot11bDCAChannelOperation_Type(Integer32):
    """Custom type ruijieRrmDot11bDCAChannelOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("delete", 0),
          ("add", 1))
    )


_RuijieRrmDot11bDCAChannelOperation_Type.__name__ = "Integer32"
_RuijieRrmDot11bDCAChannelOperation_Object = MibTableColumn
ruijieRrmDot11bDCAChannelOperation = _RuijieRrmDot11bDCAChannelOperation_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 3, 1, 10, 1, 2),
    _RuijieRrmDot11bDCAChannelOperation_Type()
)
ruijieRrmDot11bDCAChannelOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmDot11bDCAChannelOperation.setStatus("current")
_RuijieRrmTPCDot11b_ObjectIdentity = ObjectIdentity
ruijieRrmTPCDot11b = _RuijieRrmTPCDot11b_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 3, 2)
)


class _RuijieRrmDot11bDTPCSupport_Type(Integer32):
    """Custom type ruijieRrmDot11bDTPCSupport based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuijieRrmDot11bDTPCSupport_Type.__name__ = "Integer32"
_RuijieRrmDot11bDTPCSupport_Object = MibScalar
ruijieRrmDot11bDTPCSupport = _RuijieRrmDot11bDTPCSupport_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 3, 2, 1),
    _RuijieRrmDot11bDTPCSupport_Type()
)
ruijieRrmDot11bDTPCSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmDot11bDTPCSupport.setStatus("current")


class _RuijieRrmDot11bDynamicTransmitPowerControl_Type(Integer32):
    """Custom type ruijieRrmDot11bDynamicTransmitPowerControl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("runOnce", 2),
          ("static", 3))
    )


_RuijieRrmDot11bDynamicTransmitPowerControl_Type.__name__ = "Integer32"
_RuijieRrmDot11bDynamicTransmitPowerControl_Object = MibScalar
ruijieRrmDot11bDynamicTransmitPowerControl = _RuijieRrmDot11bDynamicTransmitPowerControl_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 3, 2, 2),
    _RuijieRrmDot11bDynamicTransmitPowerControl_Type()
)
ruijieRrmDot11bDynamicTransmitPowerControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmDot11bDynamicTransmitPowerControl.setStatus("current")


class _RuijieRrmDot11bDynamicTxPowerControlInterval_Type(Unsigned32):
    """Custom type ruijieRrmDot11bDynamicTxPowerControlInterval based on Unsigned32"""
    defaultValue = 600


_RuijieRrmDot11bDynamicTxPowerControlInterval_Type.__name__ = "Unsigned32"
_RuijieRrmDot11bDynamicTxPowerControlInterval_Object = MibScalar
ruijieRrmDot11bDynamicTxPowerControlInterval = _RuijieRrmDot11bDynamicTxPowerControlInterval_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 3, 2, 3),
    _RuijieRrmDot11bDynamicTxPowerControlInterval_Type()
)
ruijieRrmDot11bDynamicTxPowerControlInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmDot11bDynamicTxPowerControlInterval.setStatus("current")


class _RuijieRrmDot11bCurrentTxPowerLevel_Type(Integer32):
    """Custom type ruijieRrmDot11bCurrentTxPowerLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_RuijieRrmDot11bCurrentTxPowerLevel_Type.__name__ = "Integer32"
_RuijieRrmDot11bCurrentTxPowerLevel_Object = MibScalar
ruijieRrmDot11bCurrentTxPowerLevel = _RuijieRrmDot11bCurrentTxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 3, 2, 4),
    _RuijieRrmDot11bCurrentTxPowerLevel_Type()
)
ruijieRrmDot11bCurrentTxPowerLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmDot11bCurrentTxPowerLevel.setStatus("current")


class _RuijieRrmDot11bPowerUpdateCmdInvoke_Type(Integer32):
    """Custom type ruijieRrmDot11bPowerUpdateCmdInvoke based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("activate", 1))
    )


_RuijieRrmDot11bPowerUpdateCmdInvoke_Type.__name__ = "Integer32"
_RuijieRrmDot11bPowerUpdateCmdInvoke_Object = MibScalar
ruijieRrmDot11bPowerUpdateCmdInvoke = _RuijieRrmDot11bPowerUpdateCmdInvoke_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 3, 2, 5),
    _RuijieRrmDot11bPowerUpdateCmdInvoke_Type()
)
ruijieRrmDot11bPowerUpdateCmdInvoke.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmDot11bPowerUpdateCmdInvoke.setStatus("current")


class _RuijieRrmDot11bTXPowerThreshold_Type(Integer32):
    """Custom type ruijieRrmDot11bTXPowerThreshold based on Integer32"""
    defaultValue = -70

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-90, -60),
    )


_RuijieRrmDot11bTXPowerThreshold_Type.__name__ = "Integer32"
_RuijieRrmDot11bTXPowerThreshold_Object = MibScalar
ruijieRrmDot11bTXPowerThreshold = _RuijieRrmDot11bTXPowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 3, 2, 6),
    _RuijieRrmDot11bTXPowerThreshold_Type()
)
ruijieRrmDot11bTXPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmDot11bTXPowerThreshold.setStatus("current")


class _RuijieRrmDot11bTPCNeighborNumber_Type(Integer32):
    """Custom type ruijieRrmDot11bTPCNeighborNumber based on Integer32"""
    defaultValue = 3


_RuijieRrmDot11bTPCNeighborNumber_Type.__name__ = "Integer32"
_RuijieRrmDot11bTPCNeighborNumber_Object = MibScalar
ruijieRrmDot11bTPCNeighborNumber = _RuijieRrmDot11bTPCNeighborNumber_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 3, 2, 7),
    _RuijieRrmDot11bTPCNeighborNumber_Type()
)
ruijieRrmDot11bTPCNeighborNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmDot11bTPCNeighborNumber.setStatus("current")
_RuijieRrmCHDDot11b_ObjectIdentity = ObjectIdentity
ruijieRrmCHDDot11b = _RuijieRrmCHDDot11b_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 3, 3)
)


class _RuijieRrmDot11bCoverageEnable_Type(Integer32):
    """Custom type ruijieRrmDot11bCoverageEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuijieRrmDot11bCoverageEnable_Type.__name__ = "Integer32"
_RuijieRrmDot11bCoverageEnable_Object = MibScalar
ruijieRrmDot11bCoverageEnable = _RuijieRrmDot11bCoverageEnable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 3, 3, 1),
    _RuijieRrmDot11bCoverageEnable_Type()
)
ruijieRrmDot11bCoverageEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmDot11bCoverageEnable.setStatus("current")


class _RuijieRrmDot11bCoverageExceptionGlobal_Type(Integer32):
    """Custom type ruijieRrmDot11bCoverageExceptionGlobal based on Integer32"""
    defaultValue = 25

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RuijieRrmDot11bCoverageExceptionGlobal_Type.__name__ = "Integer32"
_RuijieRrmDot11bCoverageExceptionGlobal_Object = MibScalar
ruijieRrmDot11bCoverageExceptionGlobal = _RuijieRrmDot11bCoverageExceptionGlobal_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 3, 3, 2),
    _RuijieRrmDot11bCoverageExceptionGlobal_Type()
)
ruijieRrmDot11bCoverageExceptionGlobal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmDot11bCoverageExceptionGlobal.setStatus("current")


class _RuijieRrmDot11bCoverageLevelGlobal_Type(Integer32):
    """Custom type ruijieRrmDot11bCoverageLevelGlobal based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 75),
    )


_RuijieRrmDot11bCoverageLevelGlobal_Type.__name__ = "Integer32"
_RuijieRrmDot11bCoverageLevelGlobal_Object = MibScalar
ruijieRrmDot11bCoverageLevelGlobal = _RuijieRrmDot11bCoverageLevelGlobal_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 3, 3, 3),
    _RuijieRrmDot11bCoverageLevelGlobal_Type()
)
ruijieRrmDot11bCoverageLevelGlobal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmDot11bCoverageLevelGlobal.setStatus("current")


class _RuijieRrmDot11bCoverageDataRSSIThreshold_Type(Integer32):
    """Custom type ruijieRrmDot11bCoverageDataRSSIThreshold based on Integer32"""
    defaultValue = -80

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-90, -60),
    )


_RuijieRrmDot11bCoverageDataRSSIThreshold_Type.__name__ = "Integer32"
_RuijieRrmDot11bCoverageDataRSSIThreshold_Object = MibScalar
ruijieRrmDot11bCoverageDataRSSIThreshold = _RuijieRrmDot11bCoverageDataRSSIThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 3, 3, 4),
    _RuijieRrmDot11bCoverageDataRSSIThreshold_Type()
)
ruijieRrmDot11bCoverageDataRSSIThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmDot11bCoverageDataRSSIThreshold.setStatus("current")


class _RuijieRrmDot11bCoverageVoiceRSSIThreshold_Type(Integer32):
    """Custom type ruijieRrmDot11bCoverageVoiceRSSIThreshold based on Integer32"""
    defaultValue = -75

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-90, -60),
    )


_RuijieRrmDot11bCoverageVoiceRSSIThreshold_Type.__name__ = "Integer32"
_RuijieRrmDot11bCoverageVoiceRSSIThreshold_Object = MibScalar
ruijieRrmDot11bCoverageVoiceRSSIThreshold = _RuijieRrmDot11bCoverageVoiceRSSIThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 3, 3, 5),
    _RuijieRrmDot11bCoverageVoiceRSSIThreshold_Type()
)
ruijieRrmDot11bCoverageVoiceRSSIThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmDot11bCoverageVoiceRSSIThreshold.setStatus("current")


class _RuijieRrmDot11bCoverageDataPacketCount_Type(Integer32):
    """Custom type ruijieRrmDot11bCoverageDataPacketCount based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RuijieRrmDot11bCoverageDataPacketCount_Type.__name__ = "Integer32"
_RuijieRrmDot11bCoverageDataPacketCount_Object = MibScalar
ruijieRrmDot11bCoverageDataPacketCount = _RuijieRrmDot11bCoverageDataPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 3, 3, 6),
    _RuijieRrmDot11bCoverageDataPacketCount_Type()
)
ruijieRrmDot11bCoverageDataPacketCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmDot11bCoverageDataPacketCount.setStatus("current")


class _RuijieRrmDot11bCoverageVoicePacketCount_Type(Integer32):
    """Custom type ruijieRrmDot11bCoverageVoicePacketCount based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RuijieRrmDot11bCoverageVoicePacketCount_Type.__name__ = "Integer32"
_RuijieRrmDot11bCoverageVoicePacketCount_Object = MibScalar
ruijieRrmDot11bCoverageVoicePacketCount = _RuijieRrmDot11bCoverageVoicePacketCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 3, 3, 7),
    _RuijieRrmDot11bCoverageVoicePacketCount_Type()
)
ruijieRrmDot11bCoverageVoicePacketCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmDot11bCoverageVoicePacketCount.setStatus("current")


class _RuijieRrmDot11bCoverageDataFailRate_Type(Integer32):
    """Custom type ruijieRrmDot11bCoverageDataFailRate based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RuijieRrmDot11bCoverageDataFailRate_Type.__name__ = "Integer32"
_RuijieRrmDot11bCoverageDataFailRate_Object = MibScalar
ruijieRrmDot11bCoverageDataFailRate = _RuijieRrmDot11bCoverageDataFailRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 3, 3, 8),
    _RuijieRrmDot11bCoverageDataFailRate_Type()
)
ruijieRrmDot11bCoverageDataFailRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmDot11bCoverageDataFailRate.setStatus("current")


class _RuijieRrmDot11bCoverageVoiceFailRate_Type(Integer32):
    """Custom type ruijieRrmDot11bCoverageVoiceFailRate based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RuijieRrmDot11bCoverageVoiceFailRate_Type.__name__ = "Integer32"
_RuijieRrmDot11bCoverageVoiceFailRate_Object = MibScalar
ruijieRrmDot11bCoverageVoiceFailRate = _RuijieRrmDot11bCoverageVoiceFailRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 3, 3, 9),
    _RuijieRrmDot11bCoverageVoiceFailRate_Type()
)
ruijieRrmDot11bCoverageVoiceFailRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmDot11bCoverageVoiceFailRate.setStatus("current")
_RuijieRrmGroupDot11b_ObjectIdentity = ObjectIdentity
ruijieRrmGroupDot11b = _RuijieRrmGroupDot11b_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 3, 4)
)


class _RuijieRrmDot11bGlobalAutomaticGrouping_Type(Integer32):
    """Custom type ruijieRrmDot11bGlobalAutomaticGrouping based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("automatic", 1))
    )


_RuijieRrmDot11bGlobalAutomaticGrouping_Type.__name__ = "Integer32"
_RuijieRrmDot11bGlobalAutomaticGrouping_Object = MibScalar
ruijieRrmDot11bGlobalAutomaticGrouping = _RuijieRrmDot11bGlobalAutomaticGrouping_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 3, 4, 1),
    _RuijieRrmDot11bGlobalAutomaticGrouping_Type()
)
ruijieRrmDot11bGlobalAutomaticGrouping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmDot11bGlobalAutomaticGrouping.setStatus("current")
_RuijieRrmDot11bGroupLeaderMacAddr_Type = MacAddress
_RuijieRrmDot11bGroupLeaderMacAddr_Object = MibScalar
ruijieRrmDot11bGroupLeaderMacAddr = _RuijieRrmDot11bGroupLeaderMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 3, 4, 2),
    _RuijieRrmDot11bGroupLeaderMacAddr_Type()
)
ruijieRrmDot11bGroupLeaderMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmDot11bGroupLeaderMacAddr.setStatus("current")


class _RuijieRrmDot11bGroupLeader_Type(Integer32):
    """Custom type ruijieRrmDot11bGroupLeader based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_RuijieRrmDot11bGroupLeader_Type.__name__ = "Integer32"
_RuijieRrmDot11bGroupLeader_Object = MibScalar
ruijieRrmDot11bGroupLeader = _RuijieRrmDot11bGroupLeader_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 3, 4, 3),
    _RuijieRrmDot11bGroupLeader_Type()
)
ruijieRrmDot11bGroupLeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmDot11bGroupLeader.setStatus("current")
_RuijieRrmDot11bGroupLastUpdateTime_Type = Unsigned32
_RuijieRrmDot11bGroupLastUpdateTime_Object = MibScalar
ruijieRrmDot11bGroupLastUpdateTime = _RuijieRrmDot11bGroupLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 3, 4, 4),
    _RuijieRrmDot11bGroupLastUpdateTime_Type()
)
ruijieRrmDot11bGroupLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmDot11bGroupLastUpdateTime.setStatus("current")


class _RuijieRrmDot11bGroupInterval_Type(Unsigned32):
    """Custom type ruijieRrmDot11bGroupInterval based on Unsigned32"""
    defaultValue = 3600


_RuijieRrmDot11bGroupInterval_Type.__name__ = "Unsigned32"
_RuijieRrmDot11bGroupInterval_Object = MibScalar
ruijieRrmDot11bGroupInterval = _RuijieRrmDot11bGroupInterval_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 3, 4, 5),
    _RuijieRrmDot11bGroupInterval_Type()
)
ruijieRrmDot11bGroupInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmDot11bGroupInterval.setStatus("current")
_RuijieRrmDot11bGroupTable_Object = MibTable
ruijieRrmDot11bGroupTable = _RuijieRrmDot11bGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 3, 4, 6)
)
if mibBuilder.loadTexts:
    ruijieRrmDot11bGroupTable.setStatus("current")
_RuijieRrmDot11bGroupEntry_Object = MibTableRow
ruijieRrmDot11bGroupEntry = _RuijieRrmDot11bGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 3, 4, 6, 1)
)
ruijieRrmDot11bGroupEntry.setIndexNames(
    (0, "RUIJIE-RRM-MIB", "ruijieRrmDot11bPeerMacAddress"),
)
if mibBuilder.loadTexts:
    ruijieRrmDot11bGroupEntry.setStatus("current")
_RuijieRrmDot11bPeerMacAddress_Type = MacAddress
_RuijieRrmDot11bPeerMacAddress_Object = MibTableColumn
ruijieRrmDot11bPeerMacAddress = _RuijieRrmDot11bPeerMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 3, 4, 6, 1, 1),
    _RuijieRrmDot11bPeerMacAddress_Type()
)
ruijieRrmDot11bPeerMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmDot11bPeerMacAddress.setStatus("current")
_RuijieRrmDot11bPeerIpAddress_Type = IpAddress
_RuijieRrmDot11bPeerIpAddress_Object = MibTableColumn
ruijieRrmDot11bPeerIpAddress = _RuijieRrmDot11bPeerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 3, 4, 6, 1, 2),
    _RuijieRrmDot11bPeerIpAddress_Type()
)
ruijieRrmDot11bPeerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmDot11bPeerIpAddress.setStatus("current")
_RuijieRrmDot11bSummaryTable_Object = MibTable
ruijieRrmDot11bSummaryTable = _RuijieRrmDot11bSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 3, 4, 7)
)
if mibBuilder.loadTexts:
    ruijieRrmDot11bSummaryTable.setStatus("current")
_RuijieRrmDot11bSummaryEntry_Object = MibTableRow
ruijieRrmDot11bSummaryEntry = _RuijieRrmDot11bSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 3, 4, 7, 1)
)
ruijieRrmDot11bSummaryEntry.setIndexNames(
    (0, "RUIJIE-RRM-MIB", "ruijieRrmDot11bSummaryMacAddress"),
    (0, "RUIJIE-RRM-MIB", "ruijieRrmDot11bAPRadioID"),
)
if mibBuilder.loadTexts:
    ruijieRrmDot11bSummaryEntry.setStatus("current")
_RuijieRrmDot11bAPname_Type = DisplayString
_RuijieRrmDot11bAPname_Object = MibTableColumn
ruijieRrmDot11bAPname = _RuijieRrmDot11bAPname_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 3, 4, 7, 1, 1),
    _RuijieRrmDot11bAPname_Type()
)
ruijieRrmDot11bAPname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmDot11bAPname.setStatus("current")
_RuijieRrmDot11bAPRadioID_Type = Unsigned32
_RuijieRrmDot11bAPRadioID_Object = MibTableColumn
ruijieRrmDot11bAPRadioID = _RuijieRrmDot11bAPRadioID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 3, 4, 7, 1, 2),
    _RuijieRrmDot11bAPRadioID_Type()
)
ruijieRrmDot11bAPRadioID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmDot11bAPRadioID.setStatus("current")
_RuijieRrmDot11bAPChannel_Type = Unsigned32
_RuijieRrmDot11bAPChannel_Object = MibTableColumn
ruijieRrmDot11bAPChannel = _RuijieRrmDot11bAPChannel_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 3, 4, 7, 1, 3),
    _RuijieRrmDot11bAPChannel_Type()
)
ruijieRrmDot11bAPChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmDot11bAPChannel.setStatus("current")
_RuijieRrmDot11bAPTxPower_Type = Unsigned32
_RuijieRrmDot11bAPTxPower_Object = MibTableColumn
ruijieRrmDot11bAPTxPower = _RuijieRrmDot11bAPTxPower_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 3, 4, 7, 1, 4),
    _RuijieRrmDot11bAPTxPower_Type()
)
ruijieRrmDot11bAPTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmDot11bAPTxPower.setStatus("current")


class _RuijieRrmDot11bAPChannelRrmChangeFlag_Type(Integer32):
    """Custom type ruijieRrmDot11bAPChannelRrmChangeFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_RuijieRrmDot11bAPChannelRrmChangeFlag_Type.__name__ = "Integer32"
_RuijieRrmDot11bAPChannelRrmChangeFlag_Object = MibTableColumn
ruijieRrmDot11bAPChannelRrmChangeFlag = _RuijieRrmDot11bAPChannelRrmChangeFlag_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 3, 4, 7, 1, 5),
    _RuijieRrmDot11bAPChannelRrmChangeFlag_Type()
)
ruijieRrmDot11bAPChannelRrmChangeFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmDot11bAPChannelRrmChangeFlag.setStatus("current")


class _RuijieRrmDot11bAPTxPowerRrmChangeFlag_Type(Integer32):
    """Custom type ruijieRrmDot11bAPTxPowerRrmChangeFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_RuijieRrmDot11bAPTxPowerRrmChangeFlag_Type.__name__ = "Integer32"
_RuijieRrmDot11bAPTxPowerRrmChangeFlag_Object = MibTableColumn
ruijieRrmDot11bAPTxPowerRrmChangeFlag = _RuijieRrmDot11bAPTxPowerRrmChangeFlag_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 3, 4, 7, 1, 6),
    _RuijieRrmDot11bAPTxPowerRrmChangeFlag_Type()
)
ruijieRrmDot11bAPTxPowerRrmChangeFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmDot11bAPTxPowerRrmChangeFlag.setStatus("current")
_RuijieRrmDot11bSummaryMacAddress_Type = MacAddress
_RuijieRrmDot11bSummaryMacAddress_Object = MibTableColumn
ruijieRrmDot11bSummaryMacAddress = _RuijieRrmDot11bSummaryMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 3, 4, 7, 1, 7),
    _RuijieRrmDot11bSummaryMacAddress_Type()
)
ruijieRrmDot11bSummaryMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmDot11bSummaryMacAddress.setStatus("current")
_RuijieRrmProfileDot11b_ObjectIdentity = ObjectIdentity
ruijieRrmProfileDot11b = _RuijieRrmProfileDot11b_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 3, 5)
)


class _RuijieRrmDot11bForeignInterferenceThreshold_Type(Integer32):
    """Custom type ruijieRrmDot11bForeignInterferenceThreshold based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RuijieRrmDot11bForeignInterferenceThreshold_Type.__name__ = "Integer32"
_RuijieRrmDot11bForeignInterferenceThreshold_Object = MibScalar
ruijieRrmDot11bForeignInterferenceThreshold = _RuijieRrmDot11bForeignInterferenceThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 3, 5, 1),
    _RuijieRrmDot11bForeignInterferenceThreshold_Type()
)
ruijieRrmDot11bForeignInterferenceThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmDot11bForeignInterferenceThreshold.setStatus("current")


class _RuijieRrmDot11bForeignNoiseThreshold_Type(Integer32):
    """Custom type ruijieRrmDot11bForeignNoiseThreshold based on Integer32"""
    defaultValue = -70

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-127, 0),
    )


_RuijieRrmDot11bForeignNoiseThreshold_Type.__name__ = "Integer32"
_RuijieRrmDot11bForeignNoiseThreshold_Object = MibScalar
ruijieRrmDot11bForeignNoiseThreshold = _RuijieRrmDot11bForeignNoiseThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 3, 5, 2),
    _RuijieRrmDot11bForeignNoiseThreshold_Type()
)
ruijieRrmDot11bForeignNoiseThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmDot11bForeignNoiseThreshold.setStatus("current")


class _RuijieRrmDot11bRFUtilizationThreshold_Type(Integer32):
    """Custom type ruijieRrmDot11bRFUtilizationThreshold based on Integer32"""
    defaultValue = 80

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RuijieRrmDot11bRFUtilizationThreshold_Type.__name__ = "Integer32"
_RuijieRrmDot11bRFUtilizationThreshold_Object = MibScalar
ruijieRrmDot11bRFUtilizationThreshold = _RuijieRrmDot11bRFUtilizationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 3, 5, 3),
    _RuijieRrmDot11bRFUtilizationThreshold_Type()
)
ruijieRrmDot11bRFUtilizationThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmDot11bRFUtilizationThreshold.setStatus("current")


class _RuijieRrmDot11bThroughputThreshold_Type(Unsigned32):
    """Custom type ruijieRrmDot11bThroughputThreshold based on Unsigned32"""
    defaultValue = 1000000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 10000000),
    )


_RuijieRrmDot11bThroughputThreshold_Type.__name__ = "Unsigned32"
_RuijieRrmDot11bThroughputThreshold_Object = MibScalar
ruijieRrmDot11bThroughputThreshold = _RuijieRrmDot11bThroughputThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 3, 5, 4),
    _RuijieRrmDot11bThroughputThreshold_Type()
)
ruijieRrmDot11bThroughputThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmDot11bThroughputThreshold.setStatus("current")


class _RuijieRrmDot11bMobilesThreshold_Type(Integer32):
    """Custom type ruijieRrmDot11bMobilesThreshold based on Integer32"""
    defaultValue = 12

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 75),
    )


_RuijieRrmDot11bMobilesThreshold_Type.__name__ = "Integer32"
_RuijieRrmDot11bMobilesThreshold_Object = MibScalar
ruijieRrmDot11bMobilesThreshold = _RuijieRrmDot11bMobilesThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 3, 5, 5),
    _RuijieRrmDot11bMobilesThreshold_Type()
)
ruijieRrmDot11bMobilesThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmDot11bMobilesThreshold.setStatus("current")
_RuijieRrmMonitorDot11b_ObjectIdentity = ObjectIdentity
ruijieRrmMonitorDot11b = _RuijieRrmMonitorDot11b_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 3, 6)
)


class _RuijieRrmDot11bMonitorEnable_Type(Integer32):
    """Custom type ruijieRrmDot11bMonitorEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuijieRrmDot11bMonitorEnable_Type.__name__ = "Integer32"
_RuijieRrmDot11bMonitorEnable_Object = MibScalar
ruijieRrmDot11bMonitorEnable = _RuijieRrmDot11bMonitorEnable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 3, 6, 1),
    _RuijieRrmDot11bMonitorEnable_Type()
)
ruijieRrmDot11bMonitorEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmDot11bMonitorEnable.setStatus("current")


class _RuijieRrmDot11bChannelMonitorList_Type(Integer32):
    """Custom type ruijieRrmDot11bChannelMonitorList based on Integer32"""
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
        *(("all", 1),
          ("country", 2),
          ("dca", 3))
    )


_RuijieRrmDot11bChannelMonitorList_Type.__name__ = "Integer32"
_RuijieRrmDot11bChannelMonitorList_Object = MibScalar
ruijieRrmDot11bChannelMonitorList = _RuijieRrmDot11bChannelMonitorList_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 3, 6, 2),
    _RuijieRrmDot11bChannelMonitorList_Type()
)
ruijieRrmDot11bChannelMonitorList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmDot11bChannelMonitorList.setStatus("current")


class _RuijieRrmDot11bMonitorInterval_Type(Unsigned32):
    """Custom type ruijieRrmDot11bMonitorInterval based on Unsigned32"""
    defaultValue = 180

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_RuijieRrmDot11bMonitorInterval_Type.__name__ = "Unsigned32"
_RuijieRrmDot11bMonitorInterval_Object = MibScalar
ruijieRrmDot11bMonitorInterval = _RuijieRrmDot11bMonitorInterval_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 3, 6, 3),
    _RuijieRrmDot11bMonitorInterval_Type()
)
ruijieRrmDot11bMonitorInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmDot11bMonitorInterval.setStatus("current")


class _RuijieRrmDot11bCoverageMeasurementInterval_Type(Unsigned32):
    """Custom type ruijieRrmDot11bCoverageMeasurementInterval based on Unsigned32"""
    defaultValue = 180

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_RuijieRrmDot11bCoverageMeasurementInterval_Type.__name__ = "Unsigned32"
_RuijieRrmDot11bCoverageMeasurementInterval_Object = MibScalar
ruijieRrmDot11bCoverageMeasurementInterval = _RuijieRrmDot11bCoverageMeasurementInterval_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 3, 6, 4),
    _RuijieRrmDot11bCoverageMeasurementInterval_Type()
)
ruijieRrmDot11bCoverageMeasurementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmDot11bCoverageMeasurementInterval.setStatus("current")


class _RuijieRrmDot11bLoadMeasurementInterval_Type(Unsigned32):
    """Custom type ruijieRrmDot11bLoadMeasurementInterval based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_RuijieRrmDot11bLoadMeasurementInterval_Type.__name__ = "Unsigned32"
_RuijieRrmDot11bLoadMeasurementInterval_Object = MibScalar
ruijieRrmDot11bLoadMeasurementInterval = _RuijieRrmDot11bLoadMeasurementInterval_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 3, 6, 5),
    _RuijieRrmDot11bLoadMeasurementInterval_Type()
)
ruijieRrmDot11bLoadMeasurementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmDot11bLoadMeasurementInterval.setStatus("current")


class _RuijieRrmDot11bNoiseMeasurementInterval_Type(Unsigned32):
    """Custom type ruijieRrmDot11bNoiseMeasurementInterval based on Unsigned32"""
    defaultValue = 180

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_RuijieRrmDot11bNoiseMeasurementInterval_Type.__name__ = "Unsigned32"
_RuijieRrmDot11bNoiseMeasurementInterval_Object = MibScalar
ruijieRrmDot11bNoiseMeasurementInterval = _RuijieRrmDot11bNoiseMeasurementInterval_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 3, 6, 6),
    _RuijieRrmDot11bNoiseMeasurementInterval_Type()
)
ruijieRrmDot11bNoiseMeasurementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmDot11bNoiseMeasurementInterval.setStatus("current")


class _RuijieRrmDot11bSignalMeasurementInterval_Type(Unsigned32):
    """Custom type ruijieRrmDot11bSignalMeasurementInterval based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_RuijieRrmDot11bSignalMeasurementInterval_Type.__name__ = "Unsigned32"
_RuijieRrmDot11bSignalMeasurementInterval_Object = MibScalar
ruijieRrmDot11bSignalMeasurementInterval = _RuijieRrmDot11bSignalMeasurementInterval_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 3, 6, 7),
    _RuijieRrmDot11bSignalMeasurementInterval_Type()
)
ruijieRrmDot11bSignalMeasurementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmDot11bSignalMeasurementInterval.setStatus("current")


class _RuijieRrmDot11bNeighborMessageInterval_Type(Unsigned32):
    """Custom type ruijieRrmDot11bNeighborMessageInterval based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_RuijieRrmDot11bNeighborMessageInterval_Type.__name__ = "Unsigned32"
_RuijieRrmDot11bNeighborMessageInterval_Object = MibScalar
ruijieRrmDot11bNeighborMessageInterval = _RuijieRrmDot11bNeighborMessageInterval_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 3, 6, 8),
    _RuijieRrmDot11bNeighborMessageInterval_Type()
)
ruijieRrmDot11bNeighborMessageInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmDot11bNeighborMessageInterval.setStatus("current")
_RuijieRrmFactoryDot11b_ObjectIdentity = ObjectIdentity
ruijieRrmFactoryDot11b = _RuijieRrmFactoryDot11b_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 3, 7)
)


class _RuijieRrmDot11bSetFactoryDefault_Type(Integer32):
    """Custom type ruijieRrmDot11bSetFactoryDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("activate", 1))
    )


_RuijieRrmDot11bSetFactoryDefault_Type.__name__ = "Integer32"
_RuijieRrmDot11bSetFactoryDefault_Object = MibScalar
ruijieRrmDot11bSetFactoryDefault = _RuijieRrmDot11bSetFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 3, 7, 1),
    _RuijieRrmDot11bSetFactoryDefault_Type()
)
ruijieRrmDot11bSetFactoryDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmDot11bSetFactoryDefault.setStatus("current")
_RuijieRrmObjectsAP_ObjectIdentity = ObjectIdentity
ruijieRrmObjectsAP = _RuijieRrmObjectsAP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4)
)


class _RuijieRrmAPIfSlotId_Type(Integer32):
    """Custom type ruijieRrmAPIfSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_RuijieRrmAPIfSlotId_Type.__name__ = "Integer32"
_RuijieRrmAPIfSlotId_Object = MibScalar
ruijieRrmAPIfSlotId = _RuijieRrmAPIfSlotId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 1),
    _RuijieRrmAPIfSlotId_Type()
)
ruijieRrmAPIfSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmAPIfSlotId.setStatus("current")


class _RuijieRrmAPName_Type(DisplayString):
    """Custom type ruijieRrmAPName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijieRrmAPName_Type.__name__ = "DisplayString"
_RuijieRrmAPName_Object = MibScalar
ruijieRrmAPName = _RuijieRrmAPName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 2),
    _RuijieRrmAPName_Type()
)
ruijieRrmAPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmAPName.setStatus("current")
_RuijieRrmAPIfProfileThresholdConfigTable_Object = MibTable
ruijieRrmAPIfProfileThresholdConfigTable = _RuijieRrmAPIfProfileThresholdConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 3)
)
if mibBuilder.loadTexts:
    ruijieRrmAPIfProfileThresholdConfigTable.setStatus("current")
_RuijieRrmAPIfProfileThresholdConfigEntry_Object = MibTableRow
ruijieRrmAPIfProfileThresholdConfigEntry = _RuijieRrmAPIfProfileThresholdConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 3, 1)
)
ruijieRrmAPIfProfileThresholdConfigEntry.setIndexNames(
    (0, "RUIJIE-RRM-MIB", "ruijieRrmAPIfThresholdMacAddr"),
    (0, "RUIJIE-RRM-MIB", "ruijieRrmAPIfThresholdRadioType"),
)
if mibBuilder.loadTexts:
    ruijieRrmAPIfProfileThresholdConfigEntry.setStatus("current")


class _RuijieRrmAPIfThresholdRadioType_Type(Integer32):
    """Custom type ruijieRrmAPIfThresholdRadioType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("type80211a", 0),
          ("type80211b", 1))
    )


_RuijieRrmAPIfThresholdRadioType_Type.__name__ = "Integer32"
_RuijieRrmAPIfThresholdRadioType_Object = MibTableColumn
ruijieRrmAPIfThresholdRadioType = _RuijieRrmAPIfThresholdRadioType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 3, 1, 1),
    _RuijieRrmAPIfThresholdRadioType_Type()
)
ruijieRrmAPIfThresholdRadioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmAPIfThresholdRadioType.setStatus("current")


class _RuijieRrmAPIfForeignInterferenceThreshold_Type(Integer32):
    """Custom type ruijieRrmAPIfForeignInterferenceThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RuijieRrmAPIfForeignInterferenceThreshold_Type.__name__ = "Integer32"
_RuijieRrmAPIfForeignInterferenceThreshold_Object = MibTableColumn
ruijieRrmAPIfForeignInterferenceThreshold = _RuijieRrmAPIfForeignInterferenceThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 3, 1, 2),
    _RuijieRrmAPIfForeignInterferenceThreshold_Type()
)
ruijieRrmAPIfForeignInterferenceThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmAPIfForeignInterferenceThreshold.setStatus("current")


class _RuijieRrmAPIfForeignNoiseThreshold_Type(Integer32):
    """Custom type ruijieRrmAPIfForeignNoiseThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-127, 0),
    )


_RuijieRrmAPIfForeignNoiseThreshold_Type.__name__ = "Integer32"
_RuijieRrmAPIfForeignNoiseThreshold_Object = MibTableColumn
ruijieRrmAPIfForeignNoiseThreshold = _RuijieRrmAPIfForeignNoiseThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 3, 1, 3),
    _RuijieRrmAPIfForeignNoiseThreshold_Type()
)
ruijieRrmAPIfForeignNoiseThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmAPIfForeignNoiseThreshold.setStatus("current")


class _RuijieRrmAPIfRFUtilizationThreshold_Type(Integer32):
    """Custom type ruijieRrmAPIfRFUtilizationThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RuijieRrmAPIfRFUtilizationThreshold_Type.__name__ = "Integer32"
_RuijieRrmAPIfRFUtilizationThreshold_Object = MibTableColumn
ruijieRrmAPIfRFUtilizationThreshold = _RuijieRrmAPIfRFUtilizationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 3, 1, 4),
    _RuijieRrmAPIfRFUtilizationThreshold_Type()
)
ruijieRrmAPIfRFUtilizationThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmAPIfRFUtilizationThreshold.setStatus("current")


class _RuijieRrmAPIfThroughputThreshold_Type(Unsigned32):
    """Custom type ruijieRrmAPIfThroughputThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 10000000),
    )


_RuijieRrmAPIfThroughputThreshold_Type.__name__ = "Unsigned32"
_RuijieRrmAPIfThroughputThreshold_Object = MibTableColumn
ruijieRrmAPIfThroughputThreshold = _RuijieRrmAPIfThroughputThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 3, 1, 5),
    _RuijieRrmAPIfThroughputThreshold_Type()
)
ruijieRrmAPIfThroughputThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmAPIfThroughputThreshold.setStatus("current")


class _RuijieRrmAPIfMobilesThreshold_Type(Integer32):
    """Custom type ruijieRrmAPIfMobilesThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_RuijieRrmAPIfMobilesThreshold_Type.__name__ = "Integer32"
_RuijieRrmAPIfMobilesThreshold_Object = MibTableColumn
ruijieRrmAPIfMobilesThreshold = _RuijieRrmAPIfMobilesThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 3, 1, 6),
    _RuijieRrmAPIfMobilesThreshold_Type()
)
ruijieRrmAPIfMobilesThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmAPIfMobilesThreshold.setStatus("current")


class _RuijieRrmAPIfThresholdName_Type(DisplayString):
    """Custom type ruijieRrmAPIfThresholdName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijieRrmAPIfThresholdName_Type.__name__ = "DisplayString"
_RuijieRrmAPIfThresholdName_Object = MibTableColumn
ruijieRrmAPIfThresholdName = _RuijieRrmAPIfThresholdName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 3, 1, 7),
    _RuijieRrmAPIfThresholdName_Type()
)
ruijieRrmAPIfThresholdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmAPIfThresholdName.setStatus("current")
_RuijieRrmAPIfThresholdMacAddr_Type = MacAddress
_RuijieRrmAPIfThresholdMacAddr_Object = MibTableColumn
ruijieRrmAPIfThresholdMacAddr = _RuijieRrmAPIfThresholdMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 3, 1, 8),
    _RuijieRrmAPIfThresholdMacAddr_Type()
)
ruijieRrmAPIfThresholdMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmAPIfThresholdMacAddr.setStatus("current")


class _RuijieRrmAPIfForeignGlobalConfig_Type(Integer32):
    """Custom type ruijieRrmAPIfForeignGlobalConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RuijieRrmAPIfForeignGlobalConfig_Type.__name__ = "Integer32"
_RuijieRrmAPIfForeignGlobalConfig_Object = MibTableColumn
ruijieRrmAPIfForeignGlobalConfig = _RuijieRrmAPIfForeignGlobalConfig_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 3, 1, 9),
    _RuijieRrmAPIfForeignGlobalConfig_Type()
)
ruijieRrmAPIfForeignGlobalConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmAPIfForeignGlobalConfig.setStatus("current")


class _RuijieRrmAPIfNoiseGlobalConfig_Type(Integer32):
    """Custom type ruijieRrmAPIfNoiseGlobalConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RuijieRrmAPIfNoiseGlobalConfig_Type.__name__ = "Integer32"
_RuijieRrmAPIfNoiseGlobalConfig_Object = MibTableColumn
ruijieRrmAPIfNoiseGlobalConfig = _RuijieRrmAPIfNoiseGlobalConfig_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 3, 1, 10),
    _RuijieRrmAPIfNoiseGlobalConfig_Type()
)
ruijieRrmAPIfNoiseGlobalConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmAPIfNoiseGlobalConfig.setStatus("current")


class _RuijieRrmAPIfRFUtilizationGlobalConfig_Type(Integer32):
    """Custom type ruijieRrmAPIfRFUtilizationGlobalConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RuijieRrmAPIfRFUtilizationGlobalConfig_Type.__name__ = "Integer32"
_RuijieRrmAPIfRFUtilizationGlobalConfig_Object = MibTableColumn
ruijieRrmAPIfRFUtilizationGlobalConfig = _RuijieRrmAPIfRFUtilizationGlobalConfig_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 3, 1, 11),
    _RuijieRrmAPIfRFUtilizationGlobalConfig_Type()
)
ruijieRrmAPIfRFUtilizationGlobalConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmAPIfRFUtilizationGlobalConfig.setStatus("current")


class _RuijieRrmAPIfThroughputGlobalConfig_Type(Integer32):
    """Custom type ruijieRrmAPIfThroughputGlobalConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RuijieRrmAPIfThroughputGlobalConfig_Type.__name__ = "Integer32"
_RuijieRrmAPIfThroughputGlobalConfig_Object = MibTableColumn
ruijieRrmAPIfThroughputGlobalConfig = _RuijieRrmAPIfThroughputGlobalConfig_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 3, 1, 12),
    _RuijieRrmAPIfThroughputGlobalConfig_Type()
)
ruijieRrmAPIfThroughputGlobalConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmAPIfThroughputGlobalConfig.setStatus("current")


class _RuijieRrmAPIfMobilesGlobalConfig_Type(Integer32):
    """Custom type ruijieRrmAPIfMobilesGlobalConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RuijieRrmAPIfMobilesGlobalConfig_Type.__name__ = "Integer32"
_RuijieRrmAPIfMobilesGlobalConfig_Object = MibTableColumn
ruijieRrmAPIfMobilesGlobalConfig = _RuijieRrmAPIfMobilesGlobalConfig_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 3, 1, 13),
    _RuijieRrmAPIfMobilesGlobalConfig_Type()
)
ruijieRrmAPIfMobilesGlobalConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmAPIfMobilesGlobalConfig.setStatus("current")
_RuijieRrmAPIfLoadParametersTable_Object = MibTable
ruijieRrmAPIfLoadParametersTable = _RuijieRrmAPIfLoadParametersTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 4)
)
if mibBuilder.loadTexts:
    ruijieRrmAPIfLoadParametersTable.setStatus("current")
_RuijieRrmAPIfLoadParametersEntry_Object = MibTableRow
ruijieRrmAPIfLoadParametersEntry = _RuijieRrmAPIfLoadParametersEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 4, 1)
)
ruijieRrmAPIfLoadParametersEntry.setIndexNames(
    (0, "RUIJIE-RRM-MIB", "ruijieRrmAPIfLoadMacAddr"),
    (0, "RUIJIE-RRM-MIB", "ruijieRrmAPIfLoadSlotId"),
)
if mibBuilder.loadTexts:
    ruijieRrmAPIfLoadParametersEntry.setStatus("current")


class _RuijieRrmAPIfLoadRxUtilization_Type(Integer32):
    """Custom type ruijieRrmAPIfLoadRxUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RuijieRrmAPIfLoadRxUtilization_Type.__name__ = "Integer32"
_RuijieRrmAPIfLoadRxUtilization_Object = MibTableColumn
ruijieRrmAPIfLoadRxUtilization = _RuijieRrmAPIfLoadRxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 4, 1, 1),
    _RuijieRrmAPIfLoadRxUtilization_Type()
)
ruijieRrmAPIfLoadRxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmAPIfLoadRxUtilization.setStatus("current")


class _RuijieRrmAPIfLoadTxUtilization_Type(Integer32):
    """Custom type ruijieRrmAPIfLoadTxUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RuijieRrmAPIfLoadTxUtilization_Type.__name__ = "Integer32"
_RuijieRrmAPIfLoadTxUtilization_Object = MibTableColumn
ruijieRrmAPIfLoadTxUtilization = _RuijieRrmAPIfLoadTxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 4, 1, 2),
    _RuijieRrmAPIfLoadTxUtilization_Type()
)
ruijieRrmAPIfLoadTxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmAPIfLoadTxUtilization.setStatus("current")


class _RuijieRrmAPIfLoadChannelUtilization_Type(Integer32):
    """Custom type ruijieRrmAPIfLoadChannelUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RuijieRrmAPIfLoadChannelUtilization_Type.__name__ = "Integer32"
_RuijieRrmAPIfLoadChannelUtilization_Object = MibTableColumn
ruijieRrmAPIfLoadChannelUtilization = _RuijieRrmAPIfLoadChannelUtilization_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 4, 1, 3),
    _RuijieRrmAPIfLoadChannelUtilization_Type()
)
ruijieRrmAPIfLoadChannelUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmAPIfLoadChannelUtilization.setStatus("current")
_RuijieRrmAPIfLoadNumOfClients_Type = Integer32
_RuijieRrmAPIfLoadNumOfClients_Object = MibTableColumn
ruijieRrmAPIfLoadNumOfClients = _RuijieRrmAPIfLoadNumOfClients_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 4, 1, 4),
    _RuijieRrmAPIfLoadNumOfClients_Type()
)
ruijieRrmAPIfLoadNumOfClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmAPIfLoadNumOfClients.setStatus("current")
_RuijieRrmAPIfPoorSNRClients_Type = Integer32
_RuijieRrmAPIfPoorSNRClients_Object = MibTableColumn
ruijieRrmAPIfPoorSNRClients = _RuijieRrmAPIfPoorSNRClients_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 4, 1, 5),
    _RuijieRrmAPIfPoorSNRClients_Type()
)
ruijieRrmAPIfPoorSNRClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmAPIfPoorSNRClients.setStatus("current")


class _RuijieRrmAPIfLoadName_Type(DisplayString):
    """Custom type ruijieRrmAPIfLoadName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijieRrmAPIfLoadName_Type.__name__ = "DisplayString"
_RuijieRrmAPIfLoadName_Object = MibTableColumn
ruijieRrmAPIfLoadName = _RuijieRrmAPIfLoadName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 4, 1, 6),
    _RuijieRrmAPIfLoadName_Type()
)
ruijieRrmAPIfLoadName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmAPIfLoadName.setStatus("current")
_RuijieRrmAPIfLoadMacAddr_Type = MacAddress
_RuijieRrmAPIfLoadMacAddr_Object = MibTableColumn
ruijieRrmAPIfLoadMacAddr = _RuijieRrmAPIfLoadMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 4, 1, 7),
    _RuijieRrmAPIfLoadMacAddr_Type()
)
ruijieRrmAPIfLoadMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmAPIfLoadMacAddr.setStatus("current")


class _RuijieRrmAPIfLoadSlotId_Type(Integer32):
    """Custom type ruijieRrmAPIfLoadSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_RuijieRrmAPIfLoadSlotId_Type.__name__ = "Integer32"
_RuijieRrmAPIfLoadSlotId_Object = MibTableColumn
ruijieRrmAPIfLoadSlotId = _RuijieRrmAPIfLoadSlotId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 4, 1, 8),
    _RuijieRrmAPIfLoadSlotId_Type()
)
ruijieRrmAPIfLoadSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmAPIfLoadSlotId.setStatus("current")
_RuijieRrmAPIfThroughput_Type = Integer32
_RuijieRrmAPIfThroughput_Object = MibTableColumn
ruijieRrmAPIfThroughput = _RuijieRrmAPIfThroughput_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 4, 1, 9),
    _RuijieRrmAPIfThroughput_Type()
)
ruijieRrmAPIfThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmAPIfThroughput.setStatus("current")
_RuijieRrmAPIfChannelInterferenceInfoTable_Object = MibTable
ruijieRrmAPIfChannelInterferenceInfoTable = _RuijieRrmAPIfChannelInterferenceInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 5)
)
if mibBuilder.loadTexts:
    ruijieRrmAPIfChannelInterferenceInfoTable.setStatus("current")
_RuijieRrmAPIfChannelInterferenceInfoEntry_Object = MibTableRow
ruijieRrmAPIfChannelInterferenceInfoEntry = _RuijieRrmAPIfChannelInterferenceInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 5, 1)
)
ruijieRrmAPIfChannelInterferenceInfoEntry.setIndexNames(
    (0, "RUIJIE-RRM-MIB", "ruijieRrmAPIfInterferenceMacAddr"),
    (0, "RUIJIE-RRM-MIB", "ruijieRrmAPIfInterferenceSlotId"),
    (0, "RUIJIE-RRM-MIB", "ruijieRrmAPIfInterferenceChannelNo"),
)
if mibBuilder.loadTexts:
    ruijieRrmAPIfChannelInterferenceInfoEntry.setStatus("current")
_RuijieRrmAPIfInterferenceChannelNo_Type = Integer32
_RuijieRrmAPIfInterferenceChannelNo_Object = MibTableColumn
ruijieRrmAPIfInterferenceChannelNo = _RuijieRrmAPIfInterferenceChannelNo_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 5, 1, 1),
    _RuijieRrmAPIfInterferenceChannelNo_Type()
)
ruijieRrmAPIfInterferenceChannelNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmAPIfInterferenceChannelNo.setStatus("current")
_RuijieRrmAPIfInterferencePower_Type = Integer32
_RuijieRrmAPIfInterferencePower_Object = MibTableColumn
ruijieRrmAPIfInterferencePower = _RuijieRrmAPIfInterferencePower_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 5, 1, 2),
    _RuijieRrmAPIfInterferencePower_Type()
)
ruijieRrmAPIfInterferencePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmAPIfInterferencePower.setStatus("current")


class _RuijieRrmAPIfInterferenceUtilization_Type(Integer32):
    """Custom type ruijieRrmAPIfInterferenceUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RuijieRrmAPIfInterferenceUtilization_Type.__name__ = "Integer32"
_RuijieRrmAPIfInterferenceUtilization_Object = MibTableColumn
ruijieRrmAPIfInterferenceUtilization = _RuijieRrmAPIfInterferenceUtilization_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 5, 1, 3),
    _RuijieRrmAPIfInterferenceUtilization_Type()
)
ruijieRrmAPIfInterferenceUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmAPIfInterferenceUtilization.setStatus("current")


class _RuijieRrmAPIfInterferenceName_Type(DisplayString):
    """Custom type ruijieRrmAPIfInterferenceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijieRrmAPIfInterferenceName_Type.__name__ = "DisplayString"
_RuijieRrmAPIfInterferenceName_Object = MibTableColumn
ruijieRrmAPIfInterferenceName = _RuijieRrmAPIfInterferenceName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 5, 1, 4),
    _RuijieRrmAPIfInterferenceName_Type()
)
ruijieRrmAPIfInterferenceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmAPIfInterferenceName.setStatus("current")
_RuijieRrmAPIfInterferenceMacAddr_Type = MacAddress
_RuijieRrmAPIfInterferenceMacAddr_Object = MibTableColumn
ruijieRrmAPIfInterferenceMacAddr = _RuijieRrmAPIfInterferenceMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 5, 1, 5),
    _RuijieRrmAPIfInterferenceMacAddr_Type()
)
ruijieRrmAPIfInterferenceMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmAPIfInterferenceMacAddr.setStatus("current")


class _RuijieRrmAPIfInterferenceSlotId_Type(Integer32):
    """Custom type ruijieRrmAPIfInterferenceSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_RuijieRrmAPIfInterferenceSlotId_Type.__name__ = "Integer32"
_RuijieRrmAPIfInterferenceSlotId_Object = MibTableColumn
ruijieRrmAPIfInterferenceSlotId = _RuijieRrmAPIfInterferenceSlotId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 5, 1, 6),
    _RuijieRrmAPIfInterferenceSlotId_Type()
)
ruijieRrmAPIfInterferenceSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmAPIfInterferenceSlotId.setStatus("current")
_RuijieRrmAPIfChannelNoiseInfoTable_Object = MibTable
ruijieRrmAPIfChannelNoiseInfoTable = _RuijieRrmAPIfChannelNoiseInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 6)
)
if mibBuilder.loadTexts:
    ruijieRrmAPIfChannelNoiseInfoTable.setStatus("current")
_RuijieRrmAPIfChannelNoiseInfoEntry_Object = MibTableRow
ruijieRrmAPIfChannelNoiseInfoEntry = _RuijieRrmAPIfChannelNoiseInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 6, 1)
)
ruijieRrmAPIfChannelNoiseInfoEntry.setIndexNames(
    (0, "RUIJIE-RRM-MIB", "ruijieRrmAPIfNoiseMacAddr"),
    (0, "RUIJIE-RRM-MIB", "ruijieRrmAPIfNoiseSlotId"),
    (0, "RUIJIE-RRM-MIB", "ruijieRrmAPIfNoiseChannelNo"),
)
if mibBuilder.loadTexts:
    ruijieRrmAPIfChannelNoiseInfoEntry.setStatus("current")
_RuijieRrmAPIfNoiseChannelNo_Type = Integer32
_RuijieRrmAPIfNoiseChannelNo_Object = MibTableColumn
ruijieRrmAPIfNoiseChannelNo = _RuijieRrmAPIfNoiseChannelNo_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 6, 1, 1),
    _RuijieRrmAPIfNoiseChannelNo_Type()
)
ruijieRrmAPIfNoiseChannelNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmAPIfNoiseChannelNo.setStatus("current")
_RuijieRrmAPIfDBNoisePower_Type = Integer32
_RuijieRrmAPIfDBNoisePower_Object = MibTableColumn
ruijieRrmAPIfDBNoisePower = _RuijieRrmAPIfDBNoisePower_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 6, 1, 2),
    _RuijieRrmAPIfDBNoisePower_Type()
)
ruijieRrmAPIfDBNoisePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmAPIfDBNoisePower.setStatus("current")


class _RuijieRrmAPIfNoiseName_Type(DisplayString):
    """Custom type ruijieRrmAPIfNoiseName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijieRrmAPIfNoiseName_Type.__name__ = "DisplayString"
_RuijieRrmAPIfNoiseName_Object = MibTableColumn
ruijieRrmAPIfNoiseName = _RuijieRrmAPIfNoiseName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 6, 1, 3),
    _RuijieRrmAPIfNoiseName_Type()
)
ruijieRrmAPIfNoiseName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmAPIfNoiseName.setStatus("current")
_RuijieRrmAPIfNoiseMacAddr_Type = MacAddress
_RuijieRrmAPIfNoiseMacAddr_Object = MibTableColumn
ruijieRrmAPIfNoiseMacAddr = _RuijieRrmAPIfNoiseMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 6, 1, 4),
    _RuijieRrmAPIfNoiseMacAddr_Type()
)
ruijieRrmAPIfNoiseMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmAPIfNoiseMacAddr.setStatus("current")


class _RuijieRrmAPIfNoiseSlotId_Type(Integer32):
    """Custom type ruijieRrmAPIfNoiseSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_RuijieRrmAPIfNoiseSlotId_Type.__name__ = "Integer32"
_RuijieRrmAPIfNoiseSlotId_Object = MibTableColumn
ruijieRrmAPIfNoiseSlotId = _RuijieRrmAPIfNoiseSlotId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 6, 1, 5),
    _RuijieRrmAPIfNoiseSlotId_Type()
)
ruijieRrmAPIfNoiseSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmAPIfNoiseSlotId.setStatus("current")
_RuijieRrmAPIfProfileStateTable_Object = MibTable
ruijieRrmAPIfProfileStateTable = _RuijieRrmAPIfProfileStateTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 7)
)
if mibBuilder.loadTexts:
    ruijieRrmAPIfProfileStateTable.setStatus("current")
_RuijieRrmAPIfProfileStateEntry_Object = MibTableRow
ruijieRrmAPIfProfileStateEntry = _RuijieRrmAPIfProfileStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 7, 1)
)
ruijieRrmAPIfProfileStateEntry.setIndexNames(
    (0, "RUIJIE-RRM-MIB", "ruijieRrmAPIfProfileMacAddr"),
    (0, "RUIJIE-RRM-MIB", "ruijieRrmAPIfProfileSlotId"),
)
if mibBuilder.loadTexts:
    ruijieRrmAPIfProfileStateEntry.setStatus("current")
_RuijieRrmAPIfLoadProfileState_Type = ProfileState
_RuijieRrmAPIfLoadProfileState_Object = MibTableColumn
ruijieRrmAPIfLoadProfileState = _RuijieRrmAPIfLoadProfileState_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 7, 1, 1),
    _RuijieRrmAPIfLoadProfileState_Type()
)
ruijieRrmAPIfLoadProfileState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmAPIfLoadProfileState.setStatus("current")
_RuijieRrmAPIfInterferenceProfileState_Type = ProfileState
_RuijieRrmAPIfInterferenceProfileState_Object = MibTableColumn
ruijieRrmAPIfInterferenceProfileState = _RuijieRrmAPIfInterferenceProfileState_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 7, 1, 2),
    _RuijieRrmAPIfInterferenceProfileState_Type()
)
ruijieRrmAPIfInterferenceProfileState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmAPIfInterferenceProfileState.setStatus("current")
_RuijieRrmAPIfNoiseProfileState_Type = ProfileState
_RuijieRrmAPIfNoiseProfileState_Object = MibTableColumn
ruijieRrmAPIfNoiseProfileState = _RuijieRrmAPIfNoiseProfileState_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 7, 1, 3),
    _RuijieRrmAPIfNoiseProfileState_Type()
)
ruijieRrmAPIfNoiseProfileState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmAPIfNoiseProfileState.setStatus("current")
_RuijieRrmAPIfCoverageProfileState_Type = ProfileState
_RuijieRrmAPIfCoverageProfileState_Object = MibTableColumn
ruijieRrmAPIfCoverageProfileState = _RuijieRrmAPIfCoverageProfileState_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 7, 1, 4),
    _RuijieRrmAPIfCoverageProfileState_Type()
)
ruijieRrmAPIfCoverageProfileState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmAPIfCoverageProfileState.setStatus("current")
_RuijieRrmAPIfPerformanceProfileState_Type = ProfileState
_RuijieRrmAPIfPerformanceProfileState_Object = MibTableColumn
ruijieRrmAPIfPerformanceProfileState = _RuijieRrmAPIfPerformanceProfileState_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 7, 1, 5),
    _RuijieRrmAPIfPerformanceProfileState_Type()
)
ruijieRrmAPIfPerformanceProfileState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmAPIfPerformanceProfileState.setStatus("current")


class _RuijieRrmAPIfProfileName_Type(DisplayString):
    """Custom type ruijieRrmAPIfProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijieRrmAPIfProfileName_Type.__name__ = "DisplayString"
_RuijieRrmAPIfProfileName_Object = MibTableColumn
ruijieRrmAPIfProfileName = _RuijieRrmAPIfProfileName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 7, 1, 6),
    _RuijieRrmAPIfProfileName_Type()
)
ruijieRrmAPIfProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmAPIfProfileName.setStatus("current")
_RuijieRrmAPIfProfileMacAddr_Type = MacAddress
_RuijieRrmAPIfProfileMacAddr_Object = MibTableColumn
ruijieRrmAPIfProfileMacAddr = _RuijieRrmAPIfProfileMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 7, 1, 7),
    _RuijieRrmAPIfProfileMacAddr_Type()
)
ruijieRrmAPIfProfileMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmAPIfProfileMacAddr.setStatus("current")


class _RuijieRrmAPIfProfileSlotId_Type(Integer32):
    """Custom type ruijieRrmAPIfProfileSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_RuijieRrmAPIfProfileSlotId_Type.__name__ = "Integer32"
_RuijieRrmAPIfProfileSlotId_Object = MibTableColumn
ruijieRrmAPIfProfileSlotId = _RuijieRrmAPIfProfileSlotId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 7, 1, 8),
    _RuijieRrmAPIfProfileSlotId_Type()
)
ruijieRrmAPIfProfileSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmAPIfProfileSlotId.setStatus("current")
_RuijieRrmAPIfRxNeighborsTable_Object = MibTable
ruijieRrmAPIfRxNeighborsTable = _RuijieRrmAPIfRxNeighborsTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 8)
)
if mibBuilder.loadTexts:
    ruijieRrmAPIfRxNeighborsTable.setStatus("current")
_RuijieRrmAPIfRxNeighborsEntry_Object = MibTableRow
ruijieRrmAPIfRxNeighborsEntry = _RuijieRrmAPIfRxNeighborsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 8, 1)
)
ruijieRrmAPIfRxNeighborsEntry.setIndexNames(
    (0, "RUIJIE-RRM-MIB", "ruijieRrmAPIfRxNeighborMacAddr"),
    (0, "RUIJIE-RRM-MIB", "ruijieRrmAPIfRxNeighborSlotId"),
    (0, "RUIJIE-RRM-MIB", "ruijieRrmAPIfRxNeighborMacAddress"),
    (0, "RUIJIE-RRM-MIB", "ruijieRrmAPIfRxNeighborSlot"),
)
if mibBuilder.loadTexts:
    ruijieRrmAPIfRxNeighborsEntry.setStatus("current")
_RuijieRrmAPIfRxNeighborMacAddress_Type = MacAddress
_RuijieRrmAPIfRxNeighborMacAddress_Object = MibTableColumn
ruijieRrmAPIfRxNeighborMacAddress = _RuijieRrmAPIfRxNeighborMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 8, 1, 1),
    _RuijieRrmAPIfRxNeighborMacAddress_Type()
)
ruijieRrmAPIfRxNeighborMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmAPIfRxNeighborMacAddress.setStatus("current")
_RuijieRrmAPIfRxNeighborSlot_Type = Integer32
_RuijieRrmAPIfRxNeighborSlot_Object = MibTableColumn
ruijieRrmAPIfRxNeighborSlot = _RuijieRrmAPIfRxNeighborSlot_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 8, 1, 2),
    _RuijieRrmAPIfRxNeighborSlot_Type()
)
ruijieRrmAPIfRxNeighborSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmAPIfRxNeighborSlot.setStatus("current")
_RuijieRrmAPIfRxNeighborIpAddress_Type = IpAddress
_RuijieRrmAPIfRxNeighborIpAddress_Object = MibTableColumn
ruijieRrmAPIfRxNeighborIpAddress = _RuijieRrmAPIfRxNeighborIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 8, 1, 3),
    _RuijieRrmAPIfRxNeighborIpAddress_Type()
)
ruijieRrmAPIfRxNeighborIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmAPIfRxNeighborIpAddress.setStatus("current")
_RuijieRrmAPIfRxNeighborRSSI_Type = Integer32
_RuijieRrmAPIfRxNeighborRSSI_Object = MibTableColumn
ruijieRrmAPIfRxNeighborRSSI = _RuijieRrmAPIfRxNeighborRSSI_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 8, 1, 4),
    _RuijieRrmAPIfRxNeighborRSSI_Type()
)
ruijieRrmAPIfRxNeighborRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmAPIfRxNeighborRSSI.setStatus("current")
_RuijieRrmAPIfRxNeighborSNR_Type = Integer32
_RuijieRrmAPIfRxNeighborSNR_Object = MibTableColumn
ruijieRrmAPIfRxNeighborSNR = _RuijieRrmAPIfRxNeighborSNR_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 8, 1, 5),
    _RuijieRrmAPIfRxNeighborSNR_Type()
)
ruijieRrmAPIfRxNeighborSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmAPIfRxNeighborSNR.setStatus("current")
_RuijieRrmAPIfRxNeighborChannel_Type = Integer32
_RuijieRrmAPIfRxNeighborChannel_Object = MibTableColumn
ruijieRrmAPIfRxNeighborChannel = _RuijieRrmAPIfRxNeighborChannel_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 8, 1, 6),
    _RuijieRrmAPIfRxNeighborChannel_Type()
)
ruijieRrmAPIfRxNeighborChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmAPIfRxNeighborChannel.setStatus("current")


class _RuijieRrmAPIfRxNeighborChannelWidth_Type(Integer32):
    """Custom type ruijieRrmAPIfRxNeighborChannelWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("five", 1),
          ("ten", 2),
          ("twenty", 3),
          ("aboveforty", 4),
          ("belowforty", 5))
    )


_RuijieRrmAPIfRxNeighborChannelWidth_Type.__name__ = "Integer32"
_RuijieRrmAPIfRxNeighborChannelWidth_Object = MibTableColumn
ruijieRrmAPIfRxNeighborChannelWidth = _RuijieRrmAPIfRxNeighborChannelWidth_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 8, 1, 7),
    _RuijieRrmAPIfRxNeighborChannelWidth_Type()
)
ruijieRrmAPIfRxNeighborChannelWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmAPIfRxNeighborChannelWidth.setStatus("current")


class _RuijieRrmAPIfRxNeighborName_Type(DisplayString):
    """Custom type ruijieRrmAPIfRxNeighborName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijieRrmAPIfRxNeighborName_Type.__name__ = "DisplayString"
_RuijieRrmAPIfRxNeighborName_Object = MibTableColumn
ruijieRrmAPIfRxNeighborName = _RuijieRrmAPIfRxNeighborName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 8, 1, 8),
    _RuijieRrmAPIfRxNeighborName_Type()
)
ruijieRrmAPIfRxNeighborName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmAPIfRxNeighborName.setStatus("current")
_RuijieRrmAPIfRxNeighborMacAddr_Type = MacAddress
_RuijieRrmAPIfRxNeighborMacAddr_Object = MibTableColumn
ruijieRrmAPIfRxNeighborMacAddr = _RuijieRrmAPIfRxNeighborMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 8, 1, 9),
    _RuijieRrmAPIfRxNeighborMacAddr_Type()
)
ruijieRrmAPIfRxNeighborMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmAPIfRxNeighborMacAddr.setStatus("current")


class _RuijieRrmAPIfRxNeighborSlotId_Type(Integer32):
    """Custom type ruijieRrmAPIfRxNeighborSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_RuijieRrmAPIfRxNeighborSlotId_Type.__name__ = "Integer32"
_RuijieRrmAPIfRxNeighborSlotId_Object = MibTableColumn
ruijieRrmAPIfRxNeighborSlotId = _RuijieRrmAPIfRxNeighborSlotId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 8, 1, 10),
    _RuijieRrmAPIfRxNeighborSlotId_Type()
)
ruijieRrmAPIfRxNeighborSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmAPIfRxNeighborSlotId.setStatus("current")
_RuijieRrmAPIfStationRSSICoverageInfoTable_Object = MibTable
ruijieRrmAPIfStationRSSICoverageInfoTable = _RuijieRrmAPIfStationRSSICoverageInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 9)
)
if mibBuilder.loadTexts:
    ruijieRrmAPIfStationRSSICoverageInfoTable.setStatus("current")
_RuijieRrmAPIfStationRSSICoverageInfoEntry_Object = MibTableRow
ruijieRrmAPIfStationRSSICoverageInfoEntry = _RuijieRrmAPIfStationRSSICoverageInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 9, 1)
)
ruijieRrmAPIfStationRSSICoverageInfoEntry.setIndexNames(
    (0, "RUIJIE-RRM-MIB", "ruijieRrmAPIfStationRSSIMacAddr"),
    (0, "RUIJIE-RRM-MIB", "ruijieRrmAPIfStationRSSISlotId"),
    (0, "RUIJIE-RRM-MIB", "ruijieRrmAPIfStationRSSICoverageIndex"),
)
if mibBuilder.loadTexts:
    ruijieRrmAPIfStationRSSICoverageInfoEntry.setStatus("current")
_RuijieRrmAPIfStationRSSICoverageIndex_Type = Integer32
_RuijieRrmAPIfStationRSSICoverageIndex_Object = MibTableColumn
ruijieRrmAPIfStationRSSICoverageIndex = _RuijieRrmAPIfStationRSSICoverageIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 9, 1, 1),
    _RuijieRrmAPIfStationRSSICoverageIndex_Type()
)
ruijieRrmAPIfStationRSSICoverageIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmAPIfStationRSSICoverageIndex.setStatus("current")
_RuijieRrmAPIfRSSILevel_Type = Integer32
_RuijieRrmAPIfRSSILevel_Object = MibTableColumn
ruijieRrmAPIfRSSILevel = _RuijieRrmAPIfRSSILevel_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 9, 1, 2),
    _RuijieRrmAPIfRSSILevel_Type()
)
ruijieRrmAPIfRSSILevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmAPIfRSSILevel.setStatus("current")
_RuijieRrmAPIfStationCountOnRSSI_Type = Integer32
_RuijieRrmAPIfStationCountOnRSSI_Object = MibTableColumn
ruijieRrmAPIfStationCountOnRSSI = _RuijieRrmAPIfStationCountOnRSSI_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 9, 1, 3),
    _RuijieRrmAPIfStationCountOnRSSI_Type()
)
ruijieRrmAPIfStationCountOnRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmAPIfStationCountOnRSSI.setStatus("current")


class _RuijieRrmAPIfStationRSSIName_Type(DisplayString):
    """Custom type ruijieRrmAPIfStationRSSIName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijieRrmAPIfStationRSSIName_Type.__name__ = "DisplayString"
_RuijieRrmAPIfStationRSSIName_Object = MibTableColumn
ruijieRrmAPIfStationRSSIName = _RuijieRrmAPIfStationRSSIName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 9, 1, 4),
    _RuijieRrmAPIfStationRSSIName_Type()
)
ruijieRrmAPIfStationRSSIName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmAPIfStationRSSIName.setStatus("current")
_RuijieRrmAPIfStationRSSIMacAddr_Type = MacAddress
_RuijieRrmAPIfStationRSSIMacAddr_Object = MibTableColumn
ruijieRrmAPIfStationRSSIMacAddr = _RuijieRrmAPIfStationRSSIMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 9, 1, 5),
    _RuijieRrmAPIfStationRSSIMacAddr_Type()
)
ruijieRrmAPIfStationRSSIMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmAPIfStationRSSIMacAddr.setStatus("current")


class _RuijieRrmAPIfStationRSSISlotId_Type(Integer32):
    """Custom type ruijieRrmAPIfStationRSSISlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_RuijieRrmAPIfStationRSSISlotId_Type.__name__ = "Integer32"
_RuijieRrmAPIfStationRSSISlotId_Object = MibTableColumn
ruijieRrmAPIfStationRSSISlotId = _RuijieRrmAPIfStationRSSISlotId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 9, 1, 6),
    _RuijieRrmAPIfStationRSSISlotId_Type()
)
ruijieRrmAPIfStationRSSISlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmAPIfStationRSSISlotId.setStatus("current")
_RuijieRrmAPIfStationSNRCoverageInfoTable_Object = MibTable
ruijieRrmAPIfStationSNRCoverageInfoTable = _RuijieRrmAPIfStationSNRCoverageInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 10)
)
if mibBuilder.loadTexts:
    ruijieRrmAPIfStationSNRCoverageInfoTable.setStatus("current")
_RuijieRrmAPIfStationSNRCoverageInfoEntry_Object = MibTableRow
ruijieRrmAPIfStationSNRCoverageInfoEntry = _RuijieRrmAPIfStationSNRCoverageInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 10, 1)
)
ruijieRrmAPIfStationSNRCoverageInfoEntry.setIndexNames(
    (0, "RUIJIE-RRM-MIB", "ruijieRrmAPIfStationSNRMacAddr"),
    (0, "RUIJIE-RRM-MIB", "ruijieRrmAPIfStationSNRSlotId"),
    (0, "RUIJIE-RRM-MIB", "ruijieRrmAPIfStationSNRCoverageIndex"),
)
if mibBuilder.loadTexts:
    ruijieRrmAPIfStationSNRCoverageInfoEntry.setStatus("current")
_RuijieRrmAPIfStationSNRCoverageIndex_Type = Integer32
_RuijieRrmAPIfStationSNRCoverageIndex_Object = MibTableColumn
ruijieRrmAPIfStationSNRCoverageIndex = _RuijieRrmAPIfStationSNRCoverageIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 10, 1, 1),
    _RuijieRrmAPIfStationSNRCoverageIndex_Type()
)
ruijieRrmAPIfStationSNRCoverageIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmAPIfStationSNRCoverageIndex.setStatus("current")
_RuijieRrmAPIfSNRLevel_Type = Integer32
_RuijieRrmAPIfSNRLevel_Object = MibTableColumn
ruijieRrmAPIfSNRLevel = _RuijieRrmAPIfSNRLevel_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 10, 1, 2),
    _RuijieRrmAPIfSNRLevel_Type()
)
ruijieRrmAPIfSNRLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmAPIfSNRLevel.setStatus("current")
_RuijieRrmAPIfStationCountOnSNR_Type = Integer32
_RuijieRrmAPIfStationCountOnSNR_Object = MibTableColumn
ruijieRrmAPIfStationCountOnSNR = _RuijieRrmAPIfStationCountOnSNR_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 10, 1, 3),
    _RuijieRrmAPIfStationCountOnSNR_Type()
)
ruijieRrmAPIfStationCountOnSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmAPIfStationCountOnSNR.setStatus("current")


class _RuijieRrmAPIfStationSNRName_Type(DisplayString):
    """Custom type ruijieRrmAPIfStationSNRName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijieRrmAPIfStationSNRName_Type.__name__ = "DisplayString"
_RuijieRrmAPIfStationSNRName_Object = MibTableColumn
ruijieRrmAPIfStationSNRName = _RuijieRrmAPIfStationSNRName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 10, 1, 4),
    _RuijieRrmAPIfStationSNRName_Type()
)
ruijieRrmAPIfStationSNRName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmAPIfStationSNRName.setStatus("current")
_RuijieRrmAPIfStationSNRMacAddr_Type = MacAddress
_RuijieRrmAPIfStationSNRMacAddr_Object = MibTableColumn
ruijieRrmAPIfStationSNRMacAddr = _RuijieRrmAPIfStationSNRMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 10, 1, 5),
    _RuijieRrmAPIfStationSNRMacAddr_Type()
)
ruijieRrmAPIfStationSNRMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmAPIfStationSNRMacAddr.setStatus("current")


class _RuijieRrmAPIfStationSNRSlotId_Type(Integer32):
    """Custom type ruijieRrmAPIfStationSNRSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_RuijieRrmAPIfStationSNRSlotId_Type.__name__ = "Integer32"
_RuijieRrmAPIfStationSNRSlotId_Object = MibTableColumn
ruijieRrmAPIfStationSNRSlotId = _RuijieRrmAPIfStationSNRSlotId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 10, 1, 6),
    _RuijieRrmAPIfStationSNRSlotId_Type()
)
ruijieRrmAPIfStationSNRSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmAPIfStationSNRSlotId.setStatus("current")
_RuijieRrmAPIfRecommendedRFParametersTable_Object = MibTable
ruijieRrmAPIfRecommendedRFParametersTable = _RuijieRrmAPIfRecommendedRFParametersTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 11)
)
if mibBuilder.loadTexts:
    ruijieRrmAPIfRecommendedRFParametersTable.setStatus("current")
_RuijieRrmAPIfRecommendedRFParametersEntry_Object = MibTableRow
ruijieRrmAPIfRecommendedRFParametersEntry = _RuijieRrmAPIfRecommendedRFParametersEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 11, 1)
)
ruijieRrmAPIfRecommendedRFParametersEntry.setIndexNames(
    (0, "RUIJIE-RRM-MIB", "ruijieRrmAPIfRecommendedMacAddr"),
    (0, "RUIJIE-RRM-MIB", "ruijieRrmAPIfRecommendedSlotId"),
)
if mibBuilder.loadTexts:
    ruijieRrmAPIfRecommendedRFParametersEntry.setStatus("current")
_RuijieRrmAPIfRecommendedChannelNumber_Type = Integer32
_RuijieRrmAPIfRecommendedChannelNumber_Object = MibTableColumn
ruijieRrmAPIfRecommendedChannelNumber = _RuijieRrmAPIfRecommendedChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 11, 1, 1),
    _RuijieRrmAPIfRecommendedChannelNumber_Type()
)
ruijieRrmAPIfRecommendedChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmAPIfRecommendedChannelNumber.setStatus("current")
_RuijieRrmAPIfRecommendedTxPowerLevel_Type = Integer32
_RuijieRrmAPIfRecommendedTxPowerLevel_Object = MibTableColumn
ruijieRrmAPIfRecommendedTxPowerLevel = _RuijieRrmAPIfRecommendedTxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 11, 1, 2),
    _RuijieRrmAPIfRecommendedTxPowerLevel_Type()
)
ruijieRrmAPIfRecommendedTxPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmAPIfRecommendedTxPowerLevel.setStatus("current")
_RuijieRrmAPIfRecommendedRTSThreshold_Type = Integer32
_RuijieRrmAPIfRecommendedRTSThreshold_Object = MibTableColumn
ruijieRrmAPIfRecommendedRTSThreshold = _RuijieRrmAPIfRecommendedRTSThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 11, 1, 3),
    _RuijieRrmAPIfRecommendedRTSThreshold_Type()
)
ruijieRrmAPIfRecommendedRTSThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmAPIfRecommendedRTSThreshold.setStatus("current")
_RuijieRrmAPIfRecommendedFragmentationThreshold_Type = Integer32
_RuijieRrmAPIfRecommendedFragmentationThreshold_Object = MibTableColumn
ruijieRrmAPIfRecommendedFragmentationThreshold = _RuijieRrmAPIfRecommendedFragmentationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 11, 1, 4),
    _RuijieRrmAPIfRecommendedFragmentationThreshold_Type()
)
ruijieRrmAPIfRecommendedFragmentationThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmAPIfRecommendedFragmentationThreshold.setStatus("current")


class _RuijieRrmAPIfRecommendedName_Type(DisplayString):
    """Custom type ruijieRrmAPIfRecommendedName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijieRrmAPIfRecommendedName_Type.__name__ = "DisplayString"
_RuijieRrmAPIfRecommendedName_Object = MibTableColumn
ruijieRrmAPIfRecommendedName = _RuijieRrmAPIfRecommendedName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 11, 1, 5),
    _RuijieRrmAPIfRecommendedName_Type()
)
ruijieRrmAPIfRecommendedName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmAPIfRecommendedName.setStatus("current")
_RuijieRrmAPIfRecommendedMacAddr_Type = MacAddress
_RuijieRrmAPIfRecommendedMacAddr_Object = MibTableColumn
ruijieRrmAPIfRecommendedMacAddr = _RuijieRrmAPIfRecommendedMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 11, 1, 6),
    _RuijieRrmAPIfRecommendedMacAddr_Type()
)
ruijieRrmAPIfRecommendedMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmAPIfRecommendedMacAddr.setStatus("current")


class _RuijieRrmAPIfRecommendedSlotId_Type(Integer32):
    """Custom type ruijieRrmAPIfRecommendedSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_RuijieRrmAPIfRecommendedSlotId_Type.__name__ = "Integer32"
_RuijieRrmAPIfRecommendedSlotId_Object = MibTableColumn
ruijieRrmAPIfRecommendedSlotId = _RuijieRrmAPIfRecommendedSlotId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 11, 1, 7),
    _RuijieRrmAPIfRecommendedSlotId_Type()
)
ruijieRrmAPIfRecommendedSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmAPIfRecommendedSlotId.setStatus("current")
_RuijieRrmAPRadioTable_Object = MibTable
ruijieRrmAPRadioTable = _RuijieRrmAPRadioTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 12)
)
if mibBuilder.loadTexts:
    ruijieRrmAPRadioTable.setStatus("current")
_RuijieRrmAPRadioEntry_Object = MibTableRow
ruijieRrmAPRadioEntry = _RuijieRrmAPRadioEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 12, 1)
)
ruijieRrmAPRadioEntry.setIndexNames(
    (0, "RUIJIE-RRM-MIB", "ruijieRrmAPMacAddr"),
    (0, "RUIJIE-RRM-MIB", "ruijieRrmAPRadioID"),
)
if mibBuilder.loadTexts:
    ruijieRrmAPRadioEntry.setStatus("current")


class _RuijieRrmAPRadioID_Type(Integer32):
    """Custom type ruijieRrmAPRadioID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_RuijieRrmAPRadioID_Type.__name__ = "Integer32"
_RuijieRrmAPRadioID_Object = MibTableColumn
ruijieRrmAPRadioID = _RuijieRrmAPRadioID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 12, 1, 1),
    _RuijieRrmAPRadioID_Type()
)
ruijieRrmAPRadioID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmAPRadioID.setStatus("current")


class _RuijieRrmAPRadioType_Type(Integer32):
    """Custom type ruijieRrmAPRadioType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("type80211a", 0),
          ("type80211b", 1))
    )


_RuijieRrmAPRadioType_Type.__name__ = "Integer32"
_RuijieRrmAPRadioType_Object = MibTableColumn
ruijieRrmAPRadioType = _RuijieRrmAPRadioType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 12, 1, 2),
    _RuijieRrmAPRadioType_Type()
)
ruijieRrmAPRadioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmAPRadioType.setStatus("current")


class _RuijieRrmAPRealName_Type(DisplayString):
    """Custom type ruijieRrmAPRealName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijieRrmAPRealName_Type.__name__ = "DisplayString"
_RuijieRrmAPRealName_Object = MibTableColumn
ruijieRrmAPRealName = _RuijieRrmAPRealName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 12, 1, 3),
    _RuijieRrmAPRealName_Type()
)
ruijieRrmAPRealName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmAPRealName.setStatus("current")
_RuijieRrmAPMacAddr_Type = MacAddress
_RuijieRrmAPMacAddr_Object = MibTableColumn
ruijieRrmAPMacAddr = _RuijieRrmAPMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 12, 1, 4),
    _RuijieRrmAPMacAddr_Type()
)
ruijieRrmAPMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmAPMacAddr.setStatus("current")
_RuijieRrmAPIfThroughputParametersTable_Object = MibTable
ruijieRrmAPIfThroughputParametersTable = _RuijieRrmAPIfThroughputParametersTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 13)
)
if mibBuilder.loadTexts:
    ruijieRrmAPIfThroughputParametersTable.setStatus("current")
_RuijieRrmAPIfThroughputParametersEntry_Object = MibTableRow
ruijieRrmAPIfThroughputParametersEntry = _RuijieRrmAPIfThroughputParametersEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 13, 1)
)
ruijieRrmAPIfThroughputParametersEntry.setIndexNames(
    (0, "RUIJIE-RRM-MIB", "ruijieRrmAPIfThroughputMacAddr"),
    (0, "RUIJIE-RRM-MIB", "ruijieRrmAPIfThroughputSlotId"),
)
if mibBuilder.loadTexts:
    ruijieRrmAPIfThroughputParametersEntry.setStatus("current")
_RuijieRrmAPIfThroughputMacAddr_Type = MacAddress
_RuijieRrmAPIfThroughputMacAddr_Object = MibTableColumn
ruijieRrmAPIfThroughputMacAddr = _RuijieRrmAPIfThroughputMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 13, 1, 1),
    _RuijieRrmAPIfThroughputMacAddr_Type()
)
ruijieRrmAPIfThroughputMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmAPIfThroughputMacAddr.setStatus("current")


class _RuijieRrmAPIfThroughputSlotId_Type(Integer32):
    """Custom type ruijieRrmAPIfThroughputSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_RuijieRrmAPIfThroughputSlotId_Type.__name__ = "Integer32"
_RuijieRrmAPIfThroughputSlotId_Object = MibTableColumn
ruijieRrmAPIfThroughputSlotId = _RuijieRrmAPIfThroughputSlotId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 13, 1, 2),
    _RuijieRrmAPIfThroughputSlotId_Type()
)
ruijieRrmAPIfThroughputSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmAPIfThroughputSlotId.setStatus("current")


class _RuijieRrmAPIfThroughputAPName_Type(DisplayString):
    """Custom type ruijieRrmAPIfThroughputAPName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RuijieRrmAPIfThroughputAPName_Type.__name__ = "DisplayString"
_RuijieRrmAPIfThroughputAPName_Object = MibTableColumn
ruijieRrmAPIfThroughputAPName = _RuijieRrmAPIfThroughputAPName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 13, 1, 3),
    _RuijieRrmAPIfThroughputAPName_Type()
)
ruijieRrmAPIfThroughputAPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmAPIfThroughputAPName.setStatus("current")
_RuijieRrmAPIfThroughputRx_Type = Integer32
_RuijieRrmAPIfThroughputRx_Object = MibTableColumn
ruijieRrmAPIfThroughputRx = _RuijieRrmAPIfThroughputRx_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 13, 1, 4),
    _RuijieRrmAPIfThroughputRx_Type()
)
ruijieRrmAPIfThroughputRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmAPIfThroughputRx.setStatus("current")
_RuijieRrmAPIfThroughputTx_Type = Integer32
_RuijieRrmAPIfThroughputTx_Object = MibTableColumn
ruijieRrmAPIfThroughputTx = _RuijieRrmAPIfThroughputTx_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 13, 1, 5),
    _RuijieRrmAPIfThroughputTx_Type()
)
ruijieRrmAPIfThroughputTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmAPIfThroughputTx.setStatus("current")
_RuijieRrmAPIfThroughputTotal_Type = Integer32
_RuijieRrmAPIfThroughputTotal_Object = MibTableColumn
ruijieRrmAPIfThroughputTotal = _RuijieRrmAPIfThroughputTotal_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 13, 1, 6),
    _RuijieRrmAPIfThroughputTotal_Type()
)
ruijieRrmAPIfThroughputTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmAPIfThroughputTotal.setStatus("current")
_RuijieRrmAPSnrBSSIDTable_Object = MibTable
ruijieRrmAPSnrBSSIDTable = _RuijieRrmAPSnrBSSIDTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 14)
)
if mibBuilder.loadTexts:
    ruijieRrmAPSnrBSSIDTable.setStatus("current")
_RuijieRrmAPSnrBSSIDEntry_Object = MibTableRow
ruijieRrmAPSnrBSSIDEntry = _RuijieRrmAPSnrBSSIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 14, 1)
)
ruijieRrmAPSnrBSSIDEntry.setIndexNames(
    (0, "RUIJIE-RRM-MIB", "ruijieRrmAPSnrBSSIDMacAddr"),
    (0, "RUIJIE-RRM-MIB", "ruijieRrmAPSnrBSSIDSlotId"),
)
if mibBuilder.loadTexts:
    ruijieRrmAPSnrBSSIDEntry.setStatus("current")
_RuijieRrmAPSnrBSSIDMacAddr_Type = MacAddress
_RuijieRrmAPSnrBSSIDMacAddr_Object = MibTableColumn
ruijieRrmAPSnrBSSIDMacAddr = _RuijieRrmAPSnrBSSIDMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 14, 1, 1),
    _RuijieRrmAPSnrBSSIDMacAddr_Type()
)
ruijieRrmAPSnrBSSIDMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmAPSnrBSSIDMacAddr.setStatus("current")


class _RuijieRrmAPSnrBSSIDSlotId_Type(Integer32):
    """Custom type ruijieRrmAPSnrBSSIDSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_RuijieRrmAPSnrBSSIDSlotId_Type.__name__ = "Integer32"
_RuijieRrmAPSnrBSSIDSlotId_Object = MibTableColumn
ruijieRrmAPSnrBSSIDSlotId = _RuijieRrmAPSnrBSSIDSlotId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 14, 1, 2),
    _RuijieRrmAPSnrBSSIDSlotId_Type()
)
ruijieRrmAPSnrBSSIDSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmAPSnrBSSIDSlotId.setStatus("current")


class _RuijieRrmAPSnrBSSIDAPName_Type(DisplayString):
    """Custom type ruijieRrmAPSnrBSSIDAPName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RuijieRrmAPSnrBSSIDAPName_Type.__name__ = "DisplayString"
_RuijieRrmAPSnrBSSIDAPName_Object = MibTableColumn
ruijieRrmAPSnrBSSIDAPName = _RuijieRrmAPSnrBSSIDAPName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 14, 1, 3),
    _RuijieRrmAPSnrBSSIDAPName_Type()
)
ruijieRrmAPSnrBSSIDAPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmAPSnrBSSIDAPName.setStatus("current")
_RuijieRrmAPSnrBSSIDAverageSignalStrength_Type = Integer32
_RuijieRrmAPSnrBSSIDAverageSignalStrength_Object = MibTableColumn
ruijieRrmAPSnrBSSIDAverageSignalStrength = _RuijieRrmAPSnrBSSIDAverageSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 14, 1, 4),
    _RuijieRrmAPSnrBSSIDAverageSignalStrength_Type()
)
ruijieRrmAPSnrBSSIDAverageSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmAPSnrBSSIDAverageSignalStrength.setStatus("current")
_RuijieRrmAPSnrBSSIDSignalPkts_Type = Integer32
_RuijieRrmAPSnrBSSIDSignalPkts_Object = MibTableColumn
ruijieRrmAPSnrBSSIDSignalPkts = _RuijieRrmAPSnrBSSIDSignalPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 14, 1, 5),
    _RuijieRrmAPSnrBSSIDSignalPkts_Type()
)
ruijieRrmAPSnrBSSIDSignalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmAPSnrBSSIDSignalPkts.setStatus("current")
_RuijieRrmAPSnrBSSIDHighestRxSignalStrength_Type = Integer32
_RuijieRrmAPSnrBSSIDHighestRxSignalStrength_Object = MibTableColumn
ruijieRrmAPSnrBSSIDHighestRxSignalStrength = _RuijieRrmAPSnrBSSIDHighestRxSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 14, 1, 6),
    _RuijieRrmAPSnrBSSIDHighestRxSignalStrength_Type()
)
ruijieRrmAPSnrBSSIDHighestRxSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmAPSnrBSSIDHighestRxSignalStrength.setStatus("current")
_RuijieRrmAPSnrBSSIDLowestRxSignalStrength_Type = Integer32
_RuijieRrmAPSnrBSSIDLowestRxSignalStrength_Object = MibTableColumn
ruijieRrmAPSnrBSSIDLowestRxSignalStrength = _RuijieRrmAPSnrBSSIDLowestRxSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 14, 1, 7),
    _RuijieRrmAPSnrBSSIDLowestRxSignalStrength_Type()
)
ruijieRrmAPSnrBSSIDLowestRxSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmAPSnrBSSIDLowestRxSignalStrength.setStatus("current")
_RuijieRrmAPSnrBSSIDSampleTime_Type = Integer32
_RuijieRrmAPSnrBSSIDSampleTime_Object = MibTableColumn
ruijieRrmAPSnrBSSIDSampleTime = _RuijieRrmAPSnrBSSIDSampleTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 1, 4, 14, 1, 8),
    _RuijieRrmAPSnrBSSIDSampleTime_Type()
)
ruijieRrmAPSnrBSSIDSampleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRrmAPSnrBSSIDSampleTime.setStatus("current")
_RuijieRrmMIBTraps_ObjectIdentity = ObjectIdentity
ruijieRrmMIBTraps = _RuijieRrmMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 2)
)
_RuijieRrmTrapControl_ObjectIdentity = ObjectIdentity
ruijieRrmTrapControl = _RuijieRrmTrapControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 2, 1)
)


class _RuijieRrmAPDot11bProfileTrapControlMask_Type(Unsigned32):
    """Custom type ruijieRrmAPDot11bProfileTrapControlMask based on Unsigned32"""
    defaultValue = 0


_RuijieRrmAPDot11bProfileTrapControlMask_Type.__name__ = "Unsigned32"
_RuijieRrmAPDot11bProfileTrapControlMask_Object = MibScalar
ruijieRrmAPDot11bProfileTrapControlMask = _RuijieRrmAPDot11bProfileTrapControlMask_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 2, 1, 1),
    _RuijieRrmAPDot11bProfileTrapControlMask_Type()
)
ruijieRrmAPDot11bProfileTrapControlMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmAPDot11bProfileTrapControlMask.setStatus("current")


class _RuijieRrmAPDot11aProfileTrapControlMask_Type(Unsigned32):
    """Custom type ruijieRrmAPDot11aProfileTrapControlMask based on Unsigned32"""
    defaultValue = 0


_RuijieRrmAPDot11aProfileTrapControlMask_Type.__name__ = "Unsigned32"
_RuijieRrmAPDot11aProfileTrapControlMask_Object = MibScalar
ruijieRrmAPDot11aProfileTrapControlMask = _RuijieRrmAPDot11aProfileTrapControlMask_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 2, 1, 2),
    _RuijieRrmAPDot11aProfileTrapControlMask_Type()
)
ruijieRrmAPDot11aProfileTrapControlMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmAPDot11aProfileTrapControlMask.setStatus("current")


class _RuijieRrmAPDot11bParamUpdateTrapControlMask_Type(Unsigned32):
    """Custom type ruijieRrmAPDot11bParamUpdateTrapControlMask based on Unsigned32"""
    defaultValue = 0


_RuijieRrmAPDot11bParamUpdateTrapControlMask_Type.__name__ = "Unsigned32"
_RuijieRrmAPDot11bParamUpdateTrapControlMask_Object = MibScalar
ruijieRrmAPDot11bParamUpdateTrapControlMask = _RuijieRrmAPDot11bParamUpdateTrapControlMask_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 2, 1, 3),
    _RuijieRrmAPDot11bParamUpdateTrapControlMask_Type()
)
ruijieRrmAPDot11bParamUpdateTrapControlMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmAPDot11bParamUpdateTrapControlMask.setStatus("current")


class _RuijieRrmAPDot11aParamUpdateTrapControlMask_Type(Unsigned32):
    """Custom type ruijieRrmAPDot11aParamUpdateTrapControlMask based on Unsigned32"""
    defaultValue = 0


_RuijieRrmAPDot11aParamUpdateTrapControlMask_Type.__name__ = "Unsigned32"
_RuijieRrmAPDot11aParamUpdateTrapControlMask_Object = MibScalar
ruijieRrmAPDot11aParamUpdateTrapControlMask = _RuijieRrmAPDot11aParamUpdateTrapControlMask_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 2, 1, 4),
    _RuijieRrmAPDot11aParamUpdateTrapControlMask_Type()
)
ruijieRrmAPDot11aParamUpdateTrapControlMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRrmAPDot11aParamUpdateTrapControlMask.setStatus("current")
_RuijieRrmTrapVariable_ObjectIdentity = ObjectIdentity
ruijieRrmTrapVariable = _RuijieRrmTrapVariable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 2, 2)
)
_RuijieRrmAPMacAddrTrapVariable_Type = MacAddress
_RuijieRrmAPMacAddrTrapVariable_Object = MibScalar
ruijieRrmAPMacAddrTrapVariable = _RuijieRrmAPMacAddrTrapVariable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 2, 2, 1),
    _RuijieRrmAPMacAddrTrapVariable_Type()
)
ruijieRrmAPMacAddrTrapVariable.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieRrmAPMacAddrTrapVariable.setStatus("current")
_RuijieRrmAPRadioIDTrapVariable_Type = Integer32
_RuijieRrmAPRadioIDTrapVariable_Object = MibScalar
ruijieRrmAPRadioIDTrapVariable = _RuijieRrmAPRadioIDTrapVariable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 2, 2, 2),
    _RuijieRrmAPRadioIDTrapVariable_Type()
)
ruijieRrmAPRadioIDTrapVariable.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieRrmAPRadioIDTrapVariable.setStatus("current")


class _RuijieRrmAPRadioTypeTrapVariable_Type(Integer32):
    """Custom type ruijieRrmAPRadioTypeTrapVariable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("type80211a", 0),
          ("type80211b", 1))
    )


_RuijieRrmAPRadioTypeTrapVariable_Type.__name__ = "Integer32"
_RuijieRrmAPRadioTypeTrapVariable_Object = MibScalar
ruijieRrmAPRadioTypeTrapVariable = _RuijieRrmAPRadioTypeTrapVariable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 2, 2, 3),
    _RuijieRrmAPRadioTypeTrapVariable_Type()
)
ruijieRrmAPRadioTypeTrapVariable.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieRrmAPRadioTypeTrapVariable.setStatus("current")
_RuijieRrmClientNumberTrapVariable_Type = Integer32
_RuijieRrmClientNumberTrapVariable_Object = MibScalar
ruijieRrmClientNumberTrapVariable = _RuijieRrmClientNumberTrapVariable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 2, 2, 4),
    _RuijieRrmClientNumberTrapVariable_Type()
)
ruijieRrmClientNumberTrapVariable.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieRrmClientNumberTrapVariable.setStatus("current")
_RuijieRrmForeignInterfereTrapVariable_Type = Integer32
_RuijieRrmForeignInterfereTrapVariable_Object = MibScalar
ruijieRrmForeignInterfereTrapVariable = _RuijieRrmForeignInterfereTrapVariable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 2, 2, 5),
    _RuijieRrmForeignInterfereTrapVariable_Type()
)
ruijieRrmForeignInterfereTrapVariable.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieRrmForeignInterfereTrapVariable.setStatus("current")
_RuijieRrmNoiseTrapVariable_Type = Integer32
_RuijieRrmNoiseTrapVariable_Object = MibScalar
ruijieRrmNoiseTrapVariable = _RuijieRrmNoiseTrapVariable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 2, 2, 6),
    _RuijieRrmNoiseTrapVariable_Type()
)
ruijieRrmNoiseTrapVariable.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieRrmNoiseTrapVariable.setStatus("current")
_RuijieRrmThroughputTrapVariable_Type = Unsigned32
_RuijieRrmThroughputTrapVariable_Object = MibScalar
ruijieRrmThroughputTrapVariable = _RuijieRrmThroughputTrapVariable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 2, 2, 7),
    _RuijieRrmThroughputTrapVariable_Type()
)
ruijieRrmThroughputTrapVariable.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieRrmThroughputTrapVariable.setStatus("current")
_RuijieRrmUtilizationTrapVariable_Type = Integer32
_RuijieRrmUtilizationTrapVariable_Object = MibScalar
ruijieRrmUtilizationTrapVariable = _RuijieRrmUtilizationTrapVariable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 2, 2, 8),
    _RuijieRrmUtilizationTrapVariable_Type()
)
ruijieRrmUtilizationTrapVariable.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieRrmUtilizationTrapVariable.setStatus("current")
_RuijieRrmAPTxPowerBeforeChange_Type = Integer32
_RuijieRrmAPTxPowerBeforeChange_Object = MibScalar
ruijieRrmAPTxPowerBeforeChange = _RuijieRrmAPTxPowerBeforeChange_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 2, 2, 9),
    _RuijieRrmAPTxPowerBeforeChange_Type()
)
ruijieRrmAPTxPowerBeforeChange.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieRrmAPTxPowerBeforeChange.setStatus("current")
_RuijieRrmAPTxPowerAfterChange_Type = Integer32
_RuijieRrmAPTxPowerAfterChange_Object = MibScalar
ruijieRrmAPTxPowerAfterChange = _RuijieRrmAPTxPowerAfterChange_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 2, 2, 10),
    _RuijieRrmAPTxPowerAfterChange_Type()
)
ruijieRrmAPTxPowerAfterChange.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieRrmAPTxPowerAfterChange.setStatus("current")
_RuijieRrmAPChannelNumberBeforeChannge_Type = Integer32
_RuijieRrmAPChannelNumberBeforeChannge_Object = MibScalar
ruijieRrmAPChannelNumberBeforeChannge = _RuijieRrmAPChannelNumberBeforeChannge_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 2, 2, 11),
    _RuijieRrmAPChannelNumberBeforeChannge_Type()
)
ruijieRrmAPChannelNumberBeforeChannge.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieRrmAPChannelNumberBeforeChannge.setStatus("current")
_RuijieRrmAPChannelNumberAfterChannge_Type = Integer32
_RuijieRrmAPChannelNumberAfterChannge_Object = MibScalar
ruijieRrmAPChannelNumberAfterChannge = _RuijieRrmAPChannelNumberAfterChannge_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 2, 2, 12),
    _RuijieRrmAPChannelNumberAfterChannge_Type()
)
ruijieRrmAPChannelNumberAfterChannge.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieRrmAPChannelNumberAfterChannge.setStatus("current")
_RuijieRrmDot11bGroupLeaderMacAddrTrapVariable_Type = MacAddress
_RuijieRrmDot11bGroupLeaderMacAddrTrapVariable_Object = MibScalar
ruijieRrmDot11bGroupLeaderMacAddrTrapVariable = _RuijieRrmDot11bGroupLeaderMacAddrTrapVariable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 2, 2, 13),
    _RuijieRrmDot11bGroupLeaderMacAddrTrapVariable_Type()
)
ruijieRrmDot11bGroupLeaderMacAddrTrapVariable.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieRrmDot11bGroupLeaderMacAddrTrapVariable.setStatus("current")
_RuijieRrmDot11aGroupLeaderMacAddrTrapVariable_Type = MacAddress
_RuijieRrmDot11aGroupLeaderMacAddrTrapVariable_Object = MibScalar
ruijieRrmDot11aGroupLeaderMacAddrTrapVariable = _RuijieRrmDot11aGroupLeaderMacAddrTrapVariable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 2, 2, 14),
    _RuijieRrmDot11aGroupLeaderMacAddrTrapVariable_Type()
)
ruijieRrmDot11aGroupLeaderMacAddrTrapVariable.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieRrmDot11aGroupLeaderMacAddrTrapVariable.setStatus("current")


class _RuijieRrmAPChannelChangeReason_Type(Integer32):
    """Custom type ruijieRrmAPChannelChangeReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("signal", 1),
          ("interference", 2),
          ("noise", 3),
          ("load", 4),
          ("radar", 5),
          ("other", 6))
    )


_RuijieRrmAPChannelChangeReason_Type.__name__ = "Integer32"
_RuijieRrmAPChannelChangeReason_Object = MibScalar
ruijieRrmAPChannelChangeReason = _RuijieRrmAPChannelChangeReason_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 2, 2, 15),
    _RuijieRrmAPChannelChangeReason_Type()
)
ruijieRrmAPChannelChangeReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieRrmAPChannelChangeReason.setStatus("current")
_RuijieRrmAPChannelChangeReasonValue_Type = Integer32
_RuijieRrmAPChannelChangeReasonValue_Object = MibScalar
ruijieRrmAPChannelChangeReasonValue = _RuijieRrmAPChannelChangeReasonValue_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 2, 2, 16),
    _RuijieRrmAPChannelChangeReasonValue_Type()
)
ruijieRrmAPChannelChangeReasonValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieRrmAPChannelChangeReasonValue.setStatus("current")


class _RuijieRrmAPTxPowerChangeCoverageFlag_Type(Integer32):
    """Custom type ruijieRrmAPTxPowerChangeCoverageFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_RuijieRrmAPTxPowerChangeCoverageFlag_Type.__name__ = "Integer32"
_RuijieRrmAPTxPowerChangeCoverageFlag_Object = MibScalar
ruijieRrmAPTxPowerChangeCoverageFlag = _RuijieRrmAPTxPowerChangeCoverageFlag_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 2, 2, 17),
    _RuijieRrmAPTxPowerChangeCoverageFlag_Type()
)
ruijieRrmAPTxPowerChangeCoverageFlag.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieRrmAPTxPowerChangeCoverageFlag.setStatus("current")
_RuijieRrmDFSFreeCount_Type = Integer32
_RuijieRrmDFSFreeCount_Object = MibScalar
ruijieRrmDFSFreeCount = _RuijieRrmDFSFreeCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 2, 2, 18),
    _RuijieRrmDFSFreeCount_Type()
)
ruijieRrmDFSFreeCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieRrmDFSFreeCount.setStatus("current")
_RuijieRrmAPChannelChangeCount_Type = Integer32
_RuijieRrmAPChannelChangeCount_Object = MibScalar
ruijieRrmAPChannelChangeCount = _RuijieRrmAPChannelChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 2, 2, 19),
    _RuijieRrmAPChannelChangeCount_Type()
)
ruijieRrmAPChannelChangeCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieRrmAPChannelChangeCount.setStatus("current")
_RuijieRrmTraps_ObjectIdentity = ObjectIdentity
ruijieRrmTraps = _RuijieRrmTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 2, 3)
)
_RuijieRrmMIBConformance_ObjectIdentity = ObjectIdentity
ruijieRrmMIBConformance = _RuijieRrmMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 3)
)
_RuijieRrmMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieRrmMIBCompliances = _RuijieRrmMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 3, 1)
)
_RuijieRrmMIBGroups_ObjectIdentity = ObjectIdentity
ruijieRrmMIBGroups = _RuijieRrmMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 3, 2)
)

# Managed Objects groups

ruijieRrmMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 3, 2, 1)
)
ruijieRrmMIBGroup.setObjects(
      *(("RUIJIE-RRM-MIB", "ruijieRrmRFNetworkName"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPName"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPIfThresholdRadioType"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPIfForeignInterferenceThreshold"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPIfForeignNoiseThreshold"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPIfRFUtilizationThreshold"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPIfThroughputThreshold"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPIfMobilesThreshold"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPIfThresholdMacAddr"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPIfThresholdRadioType"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPIfThresholdName"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPIfLoadRxUtilization"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPIfLoadTxUtilization"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPIfLoadChannelUtilization"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPIfLoadNumOfClients"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPIfPoorSNRClients"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPIfLoadName"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPIfLoadMacAddr"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPIfLoadSlotId"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPIfThroughput"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPIfInterferenceChannelNo"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPIfInterferencePower"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPIfInterferenceUtilization"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPIfInterferenceName"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPIfInterferenceMacAddr"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPIfInterferenceSlotId"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPIfNoiseChannelNo"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPIfDBNoisePower"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPIfNoiseName"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPIfNoiseMacAddr"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPIfNoiseSlotId"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPIfLoadProfileState"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPIfInterferenceProfileState"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPIfNoiseProfileState"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPIfCoverageProfileState"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPIfPerformanceProfileState"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPIfProfileName"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPIfProfileMacAddr"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPIfProfileSlotId"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPIfRxNeighborMacAddress"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPIfRxNeighborSlot"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPIfRxNeighborIpAddress"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPIfRxNeighborRSSI"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPIfRxNeighborSNR"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPIfRxNeighborChannel"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPIfRxNeighborChannelWidth"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPIfRxNeighborName"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPIfRxNeighborMacAddr"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPIfRxNeighborSlotId"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPIfStationRSSICoverageIndex"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPIfRSSILevel"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPIfStationCountOnRSSI"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPIfStationRSSIName"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPIfStationRSSIMacAddr"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPIfStationRSSISlotId"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPIfStationSNRCoverageIndex"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPIfSNRLevel"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPIfStationCountOnSNR"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPIfStationSNRName"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPIfStationSNRMacAddr"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPIfStationSNRSlotId"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPIfRecommendedChannelNumber"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPIfRecommendedTxPowerLevel"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPIfRecommendedRTSThreshold"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPIfRecommendedFragmentationThreshold"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPIfRecommendedName"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPIfRecommendedMacAddr"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPIfRecommendedSlotId"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPRadioID"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPRadioType"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPRealName"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPMacAddr"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPIfThroughputMacAddr"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPIfThroughputSlotId"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPIfThroughputAPName"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPIfThroughputRx"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPIfThroughputTx"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPIfThroughputTotal"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPSnrBSSIDMacAddr"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPSnrBSSIDSlotId"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPSnrBSSIDAPName"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPSnrBSSIDAverageSignalStrength"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPSnrBSSIDSignalPkts"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPSnrBSSIDHighestRxSignalStrength"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPSnrBSSIDLowestRxSignalStrength"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPSnrBSSIDSampleTime"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11bDynamicChannelAssignment"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11bAnchorTime"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11bChannalWidth11n"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11bDynamicChannelUpdateInterval"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11bDCASensitivity"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11bForeignInterfereFactorEnable"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11bLoadFactorEnable"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11bNoiseFactorEnable"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11bChannelUpdateCmdInvoke"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11bDCAChannelIndex"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11bDCAChannelOperation"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11aDynamicChannelAssignment"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11aAnchorTime"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11aChannalWidth11n"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11aDynamicChannelUpdateInterval"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11aDCASensitivity"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11aForeignInterfereFactorEnable"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11aLoadFactorEnable"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11aNoiseFactorEnable"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11aChannelUpdateCmdInvoke"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11aDCAChannelIndex"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11aDCAChannelOperation"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11bDTPCSupport"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11bDynamicTransmitPowerControl"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11bDynamicTxPowerControlInterval"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11bCurrentTxPowerLevel"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11bPowerUpdateCmdInvoke"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11bTXPowerThreshold"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11bTPCNeighborNumber"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11aDTPCSupport"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11aDynamicTransmitPowerControl"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11aDynamicTxPowerControlInterval"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11aCurrentTxPowerLevel"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11aPowerUpdateCmdInvoke"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11aTXPowerThreshold"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11aTPCNeighborNumber"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11bCoverageEnable"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11bCoverageExceptionGlobal"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11bCoverageLevelGlobal"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11bCoverageDataRSSIThreshold"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11bCoverageVoiceRSSIThreshold"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11bCoverageDataPacketCount"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11bCoverageVoicePacketCount"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11bCoverageDataFailRate"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11bCoverageVoiceFailRate"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11aCoverageEnable"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11aCoverageExceptionGlobal"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11aCoverageLevelGlobal"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11aCoverageDataRSSIThreshold"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11aCoverageVoiceRSSIThreshold"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11aCoverageDataPacketCount"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11aCoverageVoicePacketCount"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11aCoverageDataFailRate"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11aCoverageVoiceFailRate"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11bGlobalAutomaticGrouping"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11bGroupLeaderMacAddr"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11bGroupLeader"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11bGroupLastUpdateTime"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11bGroupInterval"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11bPeerMacAddress"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11bPeerIpAddress"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11bAPname"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11bAPRadioID"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11bAPChannel"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11bAPTxPower"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11bAPChannelRrmChangeFlag"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11bAPTxPowerRrmChangeFlag"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11bSummaryMacAddress"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11aGlobalAutomaticGrouping"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11aGroupLeader"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11aGroupLastUpdateTime"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11aGroupInterval"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11aPeerMacAddress"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11aPeerIpAddress"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11aAPname"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11aAPRadioID"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11aAPChannel"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11aAPTxPower"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11aAPChannelRrmChangeFlag"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11aAPTxPowerRrmChangeFlag"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11aSummaryMacAddress"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11bForeignInterferenceThreshold"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11bForeignNoiseThreshold"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11bRFUtilizationThreshold"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11bThroughputThreshold"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11bMobilesThreshold"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11aForeignInterferenceThreshold"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11aForeignNoiseThreshold"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11aRFUtilizationThreshold"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11aThroughputThreshold"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11aMobilesThreshold"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11bMonitorEnable"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11bChannelMonitorList"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11bMonitorInterval"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11bCoverageMeasurementInterval"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11bLoadMeasurementInterval"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11bNoiseMeasurementInterval"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11bSignalMeasurementInterval"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11bNeighborMessageInterval"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11aMonitorEnable"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11aChannelMonitorList"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11aMonitorInterval"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11aCoverageMeasurementInterval"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11aLoadMeasurementInterval"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11aNoiseMeasurementInterval"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11aSignalMeasurementInterval"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11aNeighborMessageInterval"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11bSetFactoryDefault"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11aSetFactoryDefault"))
)
if mibBuilder.loadTexts:
    ruijieRrmMIBGroup.setStatus("current")

ruijieRrmTrapsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 3, 2, 2)
)
ruijieRrmTrapsGroup.setObjects(
      *(("RUIJIE-RRM-MIB", "ruijieRrmAPDot11bProfileTrapControlMask"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPDot11aProfileTrapControlMask"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPDot11bParamUpdateTrapControlMask"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPDot11aParamUpdateTrapControlMask"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPMacAddrTrapVariable"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPRadioIDTrapVariable"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPRadioTypeTrapVariable"),
        ("RUIJIE-RRM-MIB", "ruijieRrmClientNumberTrapVariable"),
        ("RUIJIE-RRM-MIB", "ruijieRrmForeignInterfereTrapVariable"),
        ("RUIJIE-RRM-MIB", "ruijieRrmNoiseTrapVariable"),
        ("RUIJIE-RRM-MIB", "ruijieRrmThroughputTrapVariable"),
        ("RUIJIE-RRM-MIB", "ruijieRrmUtilizationTrapVariable"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPTxPowerBeforeChange"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPTxPowerAfterChange"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPTxPowerChangeCoverageFlag"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPChannelNumberBeforeChannge"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPChannelNumberAfterChannge"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPChannelChangeReason"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPChannelChangeReasonValue"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPChannelChangeCount"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDFSFreeCount"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11bGroupLeaderMacAddrTrapVariable"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11aGroupLeaderMacAddrTrapVariable"))
)
if mibBuilder.loadTexts:
    ruijieRrmTrapsGroup.setStatus("current")


# Notification objects

ruijieRrmAPClientNumProfileFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 2, 3, 1)
)
ruijieRrmAPClientNumProfileFailed.setObjects(
      *(("RUIJIE-RRM-MIB", "ruijieRrmAPMacAddrTrapVariable"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPRadioIDTrapVariable"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPRadioTypeTrapVariable"),
        ("RUIJIE-RRM-MIB", "ruijieRrmClientNumberTrapVariable"))
)
if mibBuilder.loadTexts:
    ruijieRrmAPClientNumProfileFailed.setStatus(
        "current"
    )

ruijieRrmAPLoadProfileFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 2, 3, 2)
)
ruijieRrmAPLoadProfileFailed.setObjects(
      *(("RUIJIE-RRM-MIB", "ruijieRrmAPMacAddrTrapVariable"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPRadioIDTrapVariable"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPRadioTypeTrapVariable"),
        ("RUIJIE-RRM-MIB", "ruijieRrmUtilizationTrapVariable"))
)
if mibBuilder.loadTexts:
    ruijieRrmAPLoadProfileFailed.setStatus(
        "current"
    )

ruijieRrmAPNoiseProfileFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 2, 3, 3)
)
ruijieRrmAPNoiseProfileFailed.setObjects(
      *(("RUIJIE-RRM-MIB", "ruijieRrmAPMacAddrTrapVariable"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPRadioIDTrapVariable"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPRadioTypeTrapVariable"),
        ("RUIJIE-RRM-MIB", "ruijieRrmNoiseTrapVariable"))
)
if mibBuilder.loadTexts:
    ruijieRrmAPNoiseProfileFailed.setStatus(
        "current"
    )

ruijieRrmAPInterferenceProfileFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 2, 3, 4)
)
ruijieRrmAPInterferenceProfileFailed.setObjects(
      *(("RUIJIE-RRM-MIB", "ruijieRrmAPMacAddrTrapVariable"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPRadioIDTrapVariable"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPRadioTypeTrapVariable"),
        ("RUIJIE-RRM-MIB", "ruijieRrmForeignInterfereTrapVariable"))
)
if mibBuilder.loadTexts:
    ruijieRrmAPInterferenceProfileFailed.setStatus(
        "current"
    )

ruijieRrmAPPerformanceProfileFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 2, 3, 5)
)
ruijieRrmAPPerformanceProfileFailed.setObjects(
      *(("RUIJIE-RRM-MIB", "ruijieRrmAPMacAddrTrapVariable"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPRadioIDTrapVariable"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPRadioTypeTrapVariable"),
        ("RUIJIE-RRM-MIB", "ruijieRrmThroughputTrapVariable"))
)
if mibBuilder.loadTexts:
    ruijieRrmAPPerformanceProfileFailed.setStatus(
        "current"
    )

ruijieRrmAPClientNumProfileUpdatedToPass = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 2, 3, 6)
)
ruijieRrmAPClientNumProfileUpdatedToPass.setObjects(
      *(("RUIJIE-RRM-MIB", "ruijieRrmAPMacAddrTrapVariable"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPRadioIDTrapVariable"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPRadioTypeTrapVariable"),
        ("RUIJIE-RRM-MIB", "ruijieRrmClientNumberTrapVariable"))
)
if mibBuilder.loadTexts:
    ruijieRrmAPClientNumProfileUpdatedToPass.setStatus(
        "current"
    )

ruijieRrmAPLoadProfileUpdatedToPass = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 2, 3, 7)
)
ruijieRrmAPLoadProfileUpdatedToPass.setObjects(
      *(("RUIJIE-RRM-MIB", "ruijieRrmAPMacAddrTrapVariable"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPRadioIDTrapVariable"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPRadioTypeTrapVariable"),
        ("RUIJIE-RRM-MIB", "ruijieRrmUtilizationTrapVariable"))
)
if mibBuilder.loadTexts:
    ruijieRrmAPLoadProfileUpdatedToPass.setStatus(
        "current"
    )

ruijieRrmAPNoiseProfileUpdatedToPass = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 2, 3, 8)
)
ruijieRrmAPNoiseProfileUpdatedToPass.setObjects(
      *(("RUIJIE-RRM-MIB", "ruijieRrmAPMacAddrTrapVariable"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPRadioIDTrapVariable"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPRadioTypeTrapVariable"),
        ("RUIJIE-RRM-MIB", "ruijieRrmNoiseTrapVariable"))
)
if mibBuilder.loadTexts:
    ruijieRrmAPNoiseProfileUpdatedToPass.setStatus(
        "current"
    )

ruijieRrmAPInterferenceProfileUpdatedToPass = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 2, 3, 9)
)
ruijieRrmAPInterferenceProfileUpdatedToPass.setObjects(
      *(("RUIJIE-RRM-MIB", "ruijieRrmAPMacAddrTrapVariable"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPRadioIDTrapVariable"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPRadioTypeTrapVariable"),
        ("RUIJIE-RRM-MIB", "ruijieRrmForeignInterfereTrapVariable"))
)
if mibBuilder.loadTexts:
    ruijieRrmAPInterferenceProfileUpdatedToPass.setStatus(
        "current"
    )

ruijieRrmAPPerformanceProfileUpdatedToPass = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 2, 3, 10)
)
ruijieRrmAPPerformanceProfileUpdatedToPass.setObjects(
      *(("RUIJIE-RRM-MIB", "ruijieRrmAPMacAddrTrapVariable"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPRadioIDTrapVariable"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPRadioTypeTrapVariable"),
        ("RUIJIE-RRM-MIB", "ruijieRrmThroughputTrapVariable"))
)
if mibBuilder.loadTexts:
    ruijieRrmAPPerformanceProfileUpdatedToPass.setStatus(
        "current"
    )

ruijieRrmAPCurrentTxPowerChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 2, 3, 11)
)
ruijieRrmAPCurrentTxPowerChanged.setObjects(
      *(("RUIJIE-RRM-MIB", "ruijieRrmAPMacAddrTrapVariable"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPRadioIDTrapVariable"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPRadioTypeTrapVariable"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPTxPowerBeforeChange"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPTxPowerAfterChange"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPTxPowerChangeCoverageFlag"))
)
if mibBuilder.loadTexts:
    ruijieRrmAPCurrentTxPowerChanged.setStatus(
        "current"
    )

ruijieRrmAPCurrentChannelChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 2, 3, 12)
)
ruijieRrmAPCurrentChannelChanged.setObjects(
      *(("RUIJIE-RRM-MIB", "ruijieRrmAPMacAddrTrapVariable"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPRadioIDTrapVariable"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPRadioTypeTrapVariable"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPChannelNumberBeforeChannge"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPChannelNumberAfterChannge"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPChannelChangeReason"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPChannelChangeReasonValue"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPChannelChangeCount"))
)
if mibBuilder.loadTexts:
    ruijieRrmAPCurrentChannelChanged.setStatus(
        "current"
    )

ruijieRrmDot11bGroupingDone = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 2, 3, 13)
)
ruijieRrmDot11bGroupingDone.setObjects(
    ("RUIJIE-RRM-MIB", "ruijieRrmDot11bGroupLeaderMacAddrTrapVariable")
)
if mibBuilder.loadTexts:
    ruijieRrmDot11bGroupingDone.setStatus(
        "current"
    )

ruijieRrmDot11aGroupingDone = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 2, 3, 14)
)
ruijieRrmDot11aGroupingDone.setObjects(
    ("RUIJIE-RRM-MIB", "ruijieRrmDot11aGroupLeaderMacAddrTrapVariable")
)
if mibBuilder.loadTexts:
    ruijieRrmDot11aGroupingDone.setStatus(
        "current"
    )

ruijieRrmDot11bDFSFreeCountBelowThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 2, 3, 15)
)
ruijieRrmDot11bDFSFreeCountBelowThreshold.setObjects(
    ("RUIJIE-RRM-MIB", "ruijieRrmDFSFreeCount")
)
if mibBuilder.loadTexts:
    ruijieRrmDot11bDFSFreeCountBelowThreshold.setStatus(
        "current"
    )

ruijieRrmDot11aDFSFreeCountBelowThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 2, 3, 16)
)
ruijieRrmDot11aDFSFreeCountBelowThreshold.setObjects(
    ("RUIJIE-RRM-MIB", "ruijieRrmDFSFreeCount")
)
if mibBuilder.loadTexts:
    ruijieRrmDot11aDFSFreeCountBelowThreshold.setStatus(
        "current"
    )

ruijieRrmNeighborAPInterference = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 2, 3, 17)
)
ruijieRrmNeighborAPInterference.setObjects(
    ("RUIJIE-RRM-MIB", "ruijieRrmAPMacAddrTrapVariable")
)
if mibBuilder.loadTexts:
    ruijieRrmNeighborAPInterference.setStatus(
        "current"
    )

ruijieRrmStationInterference = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 2, 3, 18)
)
ruijieRrmStationInterference.setObjects(
    ("RUIJIE-RRM-MIB", "ruijieRrmAPMacAddrTrapVariable")
)
if mibBuilder.loadTexts:
    ruijieRrmStationInterference.setStatus(
        "current"
    )

ruijieRrmOtherDiveceInterference = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 2, 3, 19)
)
ruijieRrmOtherDiveceInterference.setObjects(
    ("RUIJIE-RRM-MIB", "ruijieRrmAPMacAddrTrapVariable")
)
if mibBuilder.loadTexts:
    ruijieRrmOtherDiveceInterference.setStatus(
        "current"
    )


# Notifications groups

ruijieRrmTrap = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 3, 2, 3)
)
ruijieRrmTrap.setObjects(
      *(("RUIJIE-RRM-MIB", "ruijieRrmAPClientNumProfileFailed"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPLoadProfileFailed"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPNoiseProfileFailed"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPInterferenceProfileFailed"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPPerformanceProfileFailed"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPClientNumProfileUpdatedToPass"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPLoadProfileUpdatedToPass"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPNoiseProfileUpdatedToPass"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPInterferenceProfileUpdatedToPass"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPPerformanceProfileUpdatedToPass"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPCurrentTxPowerChanged"),
        ("RUIJIE-RRM-MIB", "ruijieRrmAPCurrentChannelChanged"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11bGroupingDone"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11aGroupingDone"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11bDFSFreeCountBelowThreshold"),
        ("RUIJIE-RRM-MIB", "ruijieRrmDot11aDFSFreeCountBelowThreshold"),
        ("RUIJIE-RRM-MIB", "ruijieRrmNeighborAPInterference"),
        ("RUIJIE-RRM-MIB", "ruijieRrmStationInterference"),
        ("RUIJIE-RRM-MIB", "ruijieRrmOtherDiveceInterference"))
)
if mibBuilder.loadTexts:
    ruijieRrmTrap.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ruijieRrmMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 63, 3, 1, 1)
)
ruijieRrmMIBCompliance.setObjects(
      *(("RUIJIE-RRM-MIB", "ruijieRrmMIBGroup"),
        ("RUIJIE-RRM-MIB", "ruijieRrmTrapsGroup"))
)
if mibBuilder.loadTexts:
    ruijieRrmMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-RRM-MIB",
    **{"ProfileState": ProfileState,
       "ruijieRrmMIB": ruijieRrmMIB,
       "ruijieRrmMIBObjects": ruijieRrmMIBObjects,
       "ruijieRrmObjectsGroup": ruijieRrmObjectsGroup,
       "ruijieRrmRFNetworkName": ruijieRrmRFNetworkName,
       "ruijieRrmObjectsDot11a": ruijieRrmObjectsDot11a,
       "ruijieRrmDCADot11a": ruijieRrmDCADot11a,
       "ruijieRrmDot11aDynamicChannelAssignment": ruijieRrmDot11aDynamicChannelAssignment,
       "ruijieRrmDot11aAnchorTime": ruijieRrmDot11aAnchorTime,
       "ruijieRrmDot11aChannalWidth11n": ruijieRrmDot11aChannalWidth11n,
       "ruijieRrmDot11aDynamicChannelUpdateInterval": ruijieRrmDot11aDynamicChannelUpdateInterval,
       "ruijieRrmDot11aDCASensitivity": ruijieRrmDot11aDCASensitivity,
       "ruijieRrmDot11aForeignInterfereFactorEnable": ruijieRrmDot11aForeignInterfereFactorEnable,
       "ruijieRrmDot11aLoadFactorEnable": ruijieRrmDot11aLoadFactorEnable,
       "ruijieRrmDot11aNoiseFactorEnable": ruijieRrmDot11aNoiseFactorEnable,
       "ruijieRrmDot11aChannelUpdateCmdInvoke": ruijieRrmDot11aChannelUpdateCmdInvoke,
       "ruijieRrmDot11aDCAChannelTable": ruijieRrmDot11aDCAChannelTable,
       "ruijieRrmDot11aDCAChannelEntry": ruijieRrmDot11aDCAChannelEntry,
       "ruijieRrmDot11aDCAChannelIndex": ruijieRrmDot11aDCAChannelIndex,
       "ruijieRrmDot11aDCAChannelOperation": ruijieRrmDot11aDCAChannelOperation,
       "ruijieRrmTPCDot11a": ruijieRrmTPCDot11a,
       "ruijieRrmDot11aDTPCSupport": ruijieRrmDot11aDTPCSupport,
       "ruijieRrmDot11aDynamicTransmitPowerControl": ruijieRrmDot11aDynamicTransmitPowerControl,
       "ruijieRrmDot11aDynamicTxPowerControlInterval": ruijieRrmDot11aDynamicTxPowerControlInterval,
       "ruijieRrmDot11aCurrentTxPowerLevel": ruijieRrmDot11aCurrentTxPowerLevel,
       "ruijieRrmDot11aPowerUpdateCmdInvoke": ruijieRrmDot11aPowerUpdateCmdInvoke,
       "ruijieRrmDot11aTXPowerThreshold": ruijieRrmDot11aTXPowerThreshold,
       "ruijieRrmDot11aTPCNeighborNumber": ruijieRrmDot11aTPCNeighborNumber,
       "ruijieRrmCHDDot11a": ruijieRrmCHDDot11a,
       "ruijieRrmDot11aCoverageEnable": ruijieRrmDot11aCoverageEnable,
       "ruijieRrmDot11aCoverageExceptionGlobal": ruijieRrmDot11aCoverageExceptionGlobal,
       "ruijieRrmDot11aCoverageLevelGlobal": ruijieRrmDot11aCoverageLevelGlobal,
       "ruijieRrmDot11aCoverageDataRSSIThreshold": ruijieRrmDot11aCoverageDataRSSIThreshold,
       "ruijieRrmDot11aCoverageVoiceRSSIThreshold": ruijieRrmDot11aCoverageVoiceRSSIThreshold,
       "ruijieRrmDot11aCoverageDataPacketCount": ruijieRrmDot11aCoverageDataPacketCount,
       "ruijieRrmDot11aCoverageVoicePacketCount": ruijieRrmDot11aCoverageVoicePacketCount,
       "ruijieRrmDot11aCoverageDataFailRate": ruijieRrmDot11aCoverageDataFailRate,
       "ruijieRrmDot11aCoverageVoiceFailRate": ruijieRrmDot11aCoverageVoiceFailRate,
       "ruijieRrmGroupDot11a": ruijieRrmGroupDot11a,
       "ruijieRrmDot11aGlobalAutomaticGrouping": ruijieRrmDot11aGlobalAutomaticGrouping,
       "ruijieRrmDot11aGroupLeaderMacAddr": ruijieRrmDot11aGroupLeaderMacAddr,
       "ruijieRrmDot11aGroupLeader": ruijieRrmDot11aGroupLeader,
       "ruijieRrmDot11aGroupLastUpdateTime": ruijieRrmDot11aGroupLastUpdateTime,
       "ruijieRrmDot11aGroupInterval": ruijieRrmDot11aGroupInterval,
       "ruijieRrmDot11aGroupTable": ruijieRrmDot11aGroupTable,
       "ruijieRrmDot11aGroupEntry": ruijieRrmDot11aGroupEntry,
       "ruijieRrmDot11aPeerMacAddress": ruijieRrmDot11aPeerMacAddress,
       "ruijieRrmDot11aPeerIpAddress": ruijieRrmDot11aPeerIpAddress,
       "ruijieRrmDot11aSummaryTable": ruijieRrmDot11aSummaryTable,
       "ruijieRrmDot11aSummaryEntry": ruijieRrmDot11aSummaryEntry,
       "ruijieRrmDot11aAPname": ruijieRrmDot11aAPname,
       "ruijieRrmDot11aAPRadioID": ruijieRrmDot11aAPRadioID,
       "ruijieRrmDot11aAPChannel": ruijieRrmDot11aAPChannel,
       "ruijieRrmDot11aAPTxPower": ruijieRrmDot11aAPTxPower,
       "ruijieRrmDot11aAPChannelRrmChangeFlag": ruijieRrmDot11aAPChannelRrmChangeFlag,
       "ruijieRrmDot11aAPTxPowerRrmChangeFlag": ruijieRrmDot11aAPTxPowerRrmChangeFlag,
       "ruijieRrmDot11aSummaryMacAddress": ruijieRrmDot11aSummaryMacAddress,
       "ruijieRrmProfileDot11a": ruijieRrmProfileDot11a,
       "ruijieRrmDot11aForeignInterferenceThreshold": ruijieRrmDot11aForeignInterferenceThreshold,
       "ruijieRrmDot11aForeignNoiseThreshold": ruijieRrmDot11aForeignNoiseThreshold,
       "ruijieRrmDot11aRFUtilizationThreshold": ruijieRrmDot11aRFUtilizationThreshold,
       "ruijieRrmDot11aThroughputThreshold": ruijieRrmDot11aThroughputThreshold,
       "ruijieRrmDot11aMobilesThreshold": ruijieRrmDot11aMobilesThreshold,
       "ruijieRrmMonitorDot11a": ruijieRrmMonitorDot11a,
       "ruijieRrmDot11aMonitorEnable": ruijieRrmDot11aMonitorEnable,
       "ruijieRrmDot11aChannelMonitorList": ruijieRrmDot11aChannelMonitorList,
       "ruijieRrmDot11aMonitorInterval": ruijieRrmDot11aMonitorInterval,
       "ruijieRrmDot11aCoverageMeasurementInterval": ruijieRrmDot11aCoverageMeasurementInterval,
       "ruijieRrmDot11aLoadMeasurementInterval": ruijieRrmDot11aLoadMeasurementInterval,
       "ruijieRrmDot11aNoiseMeasurementInterval": ruijieRrmDot11aNoiseMeasurementInterval,
       "ruijieRrmDot11aSignalMeasurementInterval": ruijieRrmDot11aSignalMeasurementInterval,
       "ruijieRrmDot11aNeighborMessageInterval": ruijieRrmDot11aNeighborMessageInterval,
       "ruijieRrmFactoryDot11a": ruijieRrmFactoryDot11a,
       "ruijieRrmDot11aSetFactoryDefault": ruijieRrmDot11aSetFactoryDefault,
       "ruijieRrmObjectsDot11b": ruijieRrmObjectsDot11b,
       "ruijieRrmDCADot11b": ruijieRrmDCADot11b,
       "ruijieRrmDot11bDynamicChannelAssignment": ruijieRrmDot11bDynamicChannelAssignment,
       "ruijieRrmDot11bAnchorTime": ruijieRrmDot11bAnchorTime,
       "ruijieRrmDot11bChannalWidth11n": ruijieRrmDot11bChannalWidth11n,
       "ruijieRrmDot11bDynamicChannelUpdateInterval": ruijieRrmDot11bDynamicChannelUpdateInterval,
       "ruijieRrmDot11bDCASensitivity": ruijieRrmDot11bDCASensitivity,
       "ruijieRrmDot11bForeignInterfereFactorEnable": ruijieRrmDot11bForeignInterfereFactorEnable,
       "ruijieRrmDot11bLoadFactorEnable": ruijieRrmDot11bLoadFactorEnable,
       "ruijieRrmDot11bNoiseFactorEnable": ruijieRrmDot11bNoiseFactorEnable,
       "ruijieRrmDot11bChannelUpdateCmdInvoke": ruijieRrmDot11bChannelUpdateCmdInvoke,
       "ruijieRrmDot11bDCAChannelTable": ruijieRrmDot11bDCAChannelTable,
       "ruijieRrmDot11bDCAChannelEntry": ruijieRrmDot11bDCAChannelEntry,
       "ruijieRrmDot11bDCAChannelIndex": ruijieRrmDot11bDCAChannelIndex,
       "ruijieRrmDot11bDCAChannelOperation": ruijieRrmDot11bDCAChannelOperation,
       "ruijieRrmTPCDot11b": ruijieRrmTPCDot11b,
       "ruijieRrmDot11bDTPCSupport": ruijieRrmDot11bDTPCSupport,
       "ruijieRrmDot11bDynamicTransmitPowerControl": ruijieRrmDot11bDynamicTransmitPowerControl,
       "ruijieRrmDot11bDynamicTxPowerControlInterval": ruijieRrmDot11bDynamicTxPowerControlInterval,
       "ruijieRrmDot11bCurrentTxPowerLevel": ruijieRrmDot11bCurrentTxPowerLevel,
       "ruijieRrmDot11bPowerUpdateCmdInvoke": ruijieRrmDot11bPowerUpdateCmdInvoke,
       "ruijieRrmDot11bTXPowerThreshold": ruijieRrmDot11bTXPowerThreshold,
       "ruijieRrmDot11bTPCNeighborNumber": ruijieRrmDot11bTPCNeighborNumber,
       "ruijieRrmCHDDot11b": ruijieRrmCHDDot11b,
       "ruijieRrmDot11bCoverageEnable": ruijieRrmDot11bCoverageEnable,
       "ruijieRrmDot11bCoverageExceptionGlobal": ruijieRrmDot11bCoverageExceptionGlobal,
       "ruijieRrmDot11bCoverageLevelGlobal": ruijieRrmDot11bCoverageLevelGlobal,
       "ruijieRrmDot11bCoverageDataRSSIThreshold": ruijieRrmDot11bCoverageDataRSSIThreshold,
       "ruijieRrmDot11bCoverageVoiceRSSIThreshold": ruijieRrmDot11bCoverageVoiceRSSIThreshold,
       "ruijieRrmDot11bCoverageDataPacketCount": ruijieRrmDot11bCoverageDataPacketCount,
       "ruijieRrmDot11bCoverageVoicePacketCount": ruijieRrmDot11bCoverageVoicePacketCount,
       "ruijieRrmDot11bCoverageDataFailRate": ruijieRrmDot11bCoverageDataFailRate,
       "ruijieRrmDot11bCoverageVoiceFailRate": ruijieRrmDot11bCoverageVoiceFailRate,
       "ruijieRrmGroupDot11b": ruijieRrmGroupDot11b,
       "ruijieRrmDot11bGlobalAutomaticGrouping": ruijieRrmDot11bGlobalAutomaticGrouping,
       "ruijieRrmDot11bGroupLeaderMacAddr": ruijieRrmDot11bGroupLeaderMacAddr,
       "ruijieRrmDot11bGroupLeader": ruijieRrmDot11bGroupLeader,
       "ruijieRrmDot11bGroupLastUpdateTime": ruijieRrmDot11bGroupLastUpdateTime,
       "ruijieRrmDot11bGroupInterval": ruijieRrmDot11bGroupInterval,
       "ruijieRrmDot11bGroupTable": ruijieRrmDot11bGroupTable,
       "ruijieRrmDot11bGroupEntry": ruijieRrmDot11bGroupEntry,
       "ruijieRrmDot11bPeerMacAddress": ruijieRrmDot11bPeerMacAddress,
       "ruijieRrmDot11bPeerIpAddress": ruijieRrmDot11bPeerIpAddress,
       "ruijieRrmDot11bSummaryTable": ruijieRrmDot11bSummaryTable,
       "ruijieRrmDot11bSummaryEntry": ruijieRrmDot11bSummaryEntry,
       "ruijieRrmDot11bAPname": ruijieRrmDot11bAPname,
       "ruijieRrmDot11bAPRadioID": ruijieRrmDot11bAPRadioID,
       "ruijieRrmDot11bAPChannel": ruijieRrmDot11bAPChannel,
       "ruijieRrmDot11bAPTxPower": ruijieRrmDot11bAPTxPower,
       "ruijieRrmDot11bAPChannelRrmChangeFlag": ruijieRrmDot11bAPChannelRrmChangeFlag,
       "ruijieRrmDot11bAPTxPowerRrmChangeFlag": ruijieRrmDot11bAPTxPowerRrmChangeFlag,
       "ruijieRrmDot11bSummaryMacAddress": ruijieRrmDot11bSummaryMacAddress,
       "ruijieRrmProfileDot11b": ruijieRrmProfileDot11b,
       "ruijieRrmDot11bForeignInterferenceThreshold": ruijieRrmDot11bForeignInterferenceThreshold,
       "ruijieRrmDot11bForeignNoiseThreshold": ruijieRrmDot11bForeignNoiseThreshold,
       "ruijieRrmDot11bRFUtilizationThreshold": ruijieRrmDot11bRFUtilizationThreshold,
       "ruijieRrmDot11bThroughputThreshold": ruijieRrmDot11bThroughputThreshold,
       "ruijieRrmDot11bMobilesThreshold": ruijieRrmDot11bMobilesThreshold,
       "ruijieRrmMonitorDot11b": ruijieRrmMonitorDot11b,
       "ruijieRrmDot11bMonitorEnable": ruijieRrmDot11bMonitorEnable,
       "ruijieRrmDot11bChannelMonitorList": ruijieRrmDot11bChannelMonitorList,
       "ruijieRrmDot11bMonitorInterval": ruijieRrmDot11bMonitorInterval,
       "ruijieRrmDot11bCoverageMeasurementInterval": ruijieRrmDot11bCoverageMeasurementInterval,
       "ruijieRrmDot11bLoadMeasurementInterval": ruijieRrmDot11bLoadMeasurementInterval,
       "ruijieRrmDot11bNoiseMeasurementInterval": ruijieRrmDot11bNoiseMeasurementInterval,
       "ruijieRrmDot11bSignalMeasurementInterval": ruijieRrmDot11bSignalMeasurementInterval,
       "ruijieRrmDot11bNeighborMessageInterval": ruijieRrmDot11bNeighborMessageInterval,
       "ruijieRrmFactoryDot11b": ruijieRrmFactoryDot11b,
       "ruijieRrmDot11bSetFactoryDefault": ruijieRrmDot11bSetFactoryDefault,
       "ruijieRrmObjectsAP": ruijieRrmObjectsAP,
       "ruijieRrmAPIfSlotId": ruijieRrmAPIfSlotId,
       "ruijieRrmAPName": ruijieRrmAPName,
       "ruijieRrmAPIfProfileThresholdConfigTable": ruijieRrmAPIfProfileThresholdConfigTable,
       "ruijieRrmAPIfProfileThresholdConfigEntry": ruijieRrmAPIfProfileThresholdConfigEntry,
       "ruijieRrmAPIfThresholdRadioType": ruijieRrmAPIfThresholdRadioType,
       "ruijieRrmAPIfForeignInterferenceThreshold": ruijieRrmAPIfForeignInterferenceThreshold,
       "ruijieRrmAPIfForeignNoiseThreshold": ruijieRrmAPIfForeignNoiseThreshold,
       "ruijieRrmAPIfRFUtilizationThreshold": ruijieRrmAPIfRFUtilizationThreshold,
       "ruijieRrmAPIfThroughputThreshold": ruijieRrmAPIfThroughputThreshold,
       "ruijieRrmAPIfMobilesThreshold": ruijieRrmAPIfMobilesThreshold,
       "ruijieRrmAPIfThresholdName": ruijieRrmAPIfThresholdName,
       "ruijieRrmAPIfThresholdMacAddr": ruijieRrmAPIfThresholdMacAddr,
       "ruijieRrmAPIfForeignGlobalConfig": ruijieRrmAPIfForeignGlobalConfig,
       "ruijieRrmAPIfNoiseGlobalConfig": ruijieRrmAPIfNoiseGlobalConfig,
       "ruijieRrmAPIfRFUtilizationGlobalConfig": ruijieRrmAPIfRFUtilizationGlobalConfig,
       "ruijieRrmAPIfThroughputGlobalConfig": ruijieRrmAPIfThroughputGlobalConfig,
       "ruijieRrmAPIfMobilesGlobalConfig": ruijieRrmAPIfMobilesGlobalConfig,
       "ruijieRrmAPIfLoadParametersTable": ruijieRrmAPIfLoadParametersTable,
       "ruijieRrmAPIfLoadParametersEntry": ruijieRrmAPIfLoadParametersEntry,
       "ruijieRrmAPIfLoadRxUtilization": ruijieRrmAPIfLoadRxUtilization,
       "ruijieRrmAPIfLoadTxUtilization": ruijieRrmAPIfLoadTxUtilization,
       "ruijieRrmAPIfLoadChannelUtilization": ruijieRrmAPIfLoadChannelUtilization,
       "ruijieRrmAPIfLoadNumOfClients": ruijieRrmAPIfLoadNumOfClients,
       "ruijieRrmAPIfPoorSNRClients": ruijieRrmAPIfPoorSNRClients,
       "ruijieRrmAPIfLoadName": ruijieRrmAPIfLoadName,
       "ruijieRrmAPIfLoadMacAddr": ruijieRrmAPIfLoadMacAddr,
       "ruijieRrmAPIfLoadSlotId": ruijieRrmAPIfLoadSlotId,
       "ruijieRrmAPIfThroughput": ruijieRrmAPIfThroughput,
       "ruijieRrmAPIfChannelInterferenceInfoTable": ruijieRrmAPIfChannelInterferenceInfoTable,
       "ruijieRrmAPIfChannelInterferenceInfoEntry": ruijieRrmAPIfChannelInterferenceInfoEntry,
       "ruijieRrmAPIfInterferenceChannelNo": ruijieRrmAPIfInterferenceChannelNo,
       "ruijieRrmAPIfInterferencePower": ruijieRrmAPIfInterferencePower,
       "ruijieRrmAPIfInterferenceUtilization": ruijieRrmAPIfInterferenceUtilization,
       "ruijieRrmAPIfInterferenceName": ruijieRrmAPIfInterferenceName,
       "ruijieRrmAPIfInterferenceMacAddr": ruijieRrmAPIfInterferenceMacAddr,
       "ruijieRrmAPIfInterferenceSlotId": ruijieRrmAPIfInterferenceSlotId,
       "ruijieRrmAPIfChannelNoiseInfoTable": ruijieRrmAPIfChannelNoiseInfoTable,
       "ruijieRrmAPIfChannelNoiseInfoEntry": ruijieRrmAPIfChannelNoiseInfoEntry,
       "ruijieRrmAPIfNoiseChannelNo": ruijieRrmAPIfNoiseChannelNo,
       "ruijieRrmAPIfDBNoisePower": ruijieRrmAPIfDBNoisePower,
       "ruijieRrmAPIfNoiseName": ruijieRrmAPIfNoiseName,
       "ruijieRrmAPIfNoiseMacAddr": ruijieRrmAPIfNoiseMacAddr,
       "ruijieRrmAPIfNoiseSlotId": ruijieRrmAPIfNoiseSlotId,
       "ruijieRrmAPIfProfileStateTable": ruijieRrmAPIfProfileStateTable,
       "ruijieRrmAPIfProfileStateEntry": ruijieRrmAPIfProfileStateEntry,
       "ruijieRrmAPIfLoadProfileState": ruijieRrmAPIfLoadProfileState,
       "ruijieRrmAPIfInterferenceProfileState": ruijieRrmAPIfInterferenceProfileState,
       "ruijieRrmAPIfNoiseProfileState": ruijieRrmAPIfNoiseProfileState,
       "ruijieRrmAPIfCoverageProfileState": ruijieRrmAPIfCoverageProfileState,
       "ruijieRrmAPIfPerformanceProfileState": ruijieRrmAPIfPerformanceProfileState,
       "ruijieRrmAPIfProfileName": ruijieRrmAPIfProfileName,
       "ruijieRrmAPIfProfileMacAddr": ruijieRrmAPIfProfileMacAddr,
       "ruijieRrmAPIfProfileSlotId": ruijieRrmAPIfProfileSlotId,
       "ruijieRrmAPIfRxNeighborsTable": ruijieRrmAPIfRxNeighborsTable,
       "ruijieRrmAPIfRxNeighborsEntry": ruijieRrmAPIfRxNeighborsEntry,
       "ruijieRrmAPIfRxNeighborMacAddress": ruijieRrmAPIfRxNeighborMacAddress,
       "ruijieRrmAPIfRxNeighborSlot": ruijieRrmAPIfRxNeighborSlot,
       "ruijieRrmAPIfRxNeighborIpAddress": ruijieRrmAPIfRxNeighborIpAddress,
       "ruijieRrmAPIfRxNeighborRSSI": ruijieRrmAPIfRxNeighborRSSI,
       "ruijieRrmAPIfRxNeighborSNR": ruijieRrmAPIfRxNeighborSNR,
       "ruijieRrmAPIfRxNeighborChannel": ruijieRrmAPIfRxNeighborChannel,
       "ruijieRrmAPIfRxNeighborChannelWidth": ruijieRrmAPIfRxNeighborChannelWidth,
       "ruijieRrmAPIfRxNeighborName": ruijieRrmAPIfRxNeighborName,
       "ruijieRrmAPIfRxNeighborMacAddr": ruijieRrmAPIfRxNeighborMacAddr,
       "ruijieRrmAPIfRxNeighborSlotId": ruijieRrmAPIfRxNeighborSlotId,
       "ruijieRrmAPIfStationRSSICoverageInfoTable": ruijieRrmAPIfStationRSSICoverageInfoTable,
       "ruijieRrmAPIfStationRSSICoverageInfoEntry": ruijieRrmAPIfStationRSSICoverageInfoEntry,
       "ruijieRrmAPIfStationRSSICoverageIndex": ruijieRrmAPIfStationRSSICoverageIndex,
       "ruijieRrmAPIfRSSILevel": ruijieRrmAPIfRSSILevel,
       "ruijieRrmAPIfStationCountOnRSSI": ruijieRrmAPIfStationCountOnRSSI,
       "ruijieRrmAPIfStationRSSIName": ruijieRrmAPIfStationRSSIName,
       "ruijieRrmAPIfStationRSSIMacAddr": ruijieRrmAPIfStationRSSIMacAddr,
       "ruijieRrmAPIfStationRSSISlotId": ruijieRrmAPIfStationRSSISlotId,
       "ruijieRrmAPIfStationSNRCoverageInfoTable": ruijieRrmAPIfStationSNRCoverageInfoTable,
       "ruijieRrmAPIfStationSNRCoverageInfoEntry": ruijieRrmAPIfStationSNRCoverageInfoEntry,
       "ruijieRrmAPIfStationSNRCoverageIndex": ruijieRrmAPIfStationSNRCoverageIndex,
       "ruijieRrmAPIfSNRLevel": ruijieRrmAPIfSNRLevel,
       "ruijieRrmAPIfStationCountOnSNR": ruijieRrmAPIfStationCountOnSNR,
       "ruijieRrmAPIfStationSNRName": ruijieRrmAPIfStationSNRName,
       "ruijieRrmAPIfStationSNRMacAddr": ruijieRrmAPIfStationSNRMacAddr,
       "ruijieRrmAPIfStationSNRSlotId": ruijieRrmAPIfStationSNRSlotId,
       "ruijieRrmAPIfRecommendedRFParametersTable": ruijieRrmAPIfRecommendedRFParametersTable,
       "ruijieRrmAPIfRecommendedRFParametersEntry": ruijieRrmAPIfRecommendedRFParametersEntry,
       "ruijieRrmAPIfRecommendedChannelNumber": ruijieRrmAPIfRecommendedChannelNumber,
       "ruijieRrmAPIfRecommendedTxPowerLevel": ruijieRrmAPIfRecommendedTxPowerLevel,
       "ruijieRrmAPIfRecommendedRTSThreshold": ruijieRrmAPIfRecommendedRTSThreshold,
       "ruijieRrmAPIfRecommendedFragmentationThreshold": ruijieRrmAPIfRecommendedFragmentationThreshold,
       "ruijieRrmAPIfRecommendedName": ruijieRrmAPIfRecommendedName,
       "ruijieRrmAPIfRecommendedMacAddr": ruijieRrmAPIfRecommendedMacAddr,
       "ruijieRrmAPIfRecommendedSlotId": ruijieRrmAPIfRecommendedSlotId,
       "ruijieRrmAPRadioTable": ruijieRrmAPRadioTable,
       "ruijieRrmAPRadioEntry": ruijieRrmAPRadioEntry,
       "ruijieRrmAPRadioID": ruijieRrmAPRadioID,
       "ruijieRrmAPRadioType": ruijieRrmAPRadioType,
       "ruijieRrmAPRealName": ruijieRrmAPRealName,
       "ruijieRrmAPMacAddr": ruijieRrmAPMacAddr,
       "ruijieRrmAPIfThroughputParametersTable": ruijieRrmAPIfThroughputParametersTable,
       "ruijieRrmAPIfThroughputParametersEntry": ruijieRrmAPIfThroughputParametersEntry,
       "ruijieRrmAPIfThroughputMacAddr": ruijieRrmAPIfThroughputMacAddr,
       "ruijieRrmAPIfThroughputSlotId": ruijieRrmAPIfThroughputSlotId,
       "ruijieRrmAPIfThroughputAPName": ruijieRrmAPIfThroughputAPName,
       "ruijieRrmAPIfThroughputRx": ruijieRrmAPIfThroughputRx,
       "ruijieRrmAPIfThroughputTx": ruijieRrmAPIfThroughputTx,
       "ruijieRrmAPIfThroughputTotal": ruijieRrmAPIfThroughputTotal,
       "ruijieRrmAPSnrBSSIDTable": ruijieRrmAPSnrBSSIDTable,
       "ruijieRrmAPSnrBSSIDEntry": ruijieRrmAPSnrBSSIDEntry,
       "ruijieRrmAPSnrBSSIDMacAddr": ruijieRrmAPSnrBSSIDMacAddr,
       "ruijieRrmAPSnrBSSIDSlotId": ruijieRrmAPSnrBSSIDSlotId,
       "ruijieRrmAPSnrBSSIDAPName": ruijieRrmAPSnrBSSIDAPName,
       "ruijieRrmAPSnrBSSIDAverageSignalStrength": ruijieRrmAPSnrBSSIDAverageSignalStrength,
       "ruijieRrmAPSnrBSSIDSignalPkts": ruijieRrmAPSnrBSSIDSignalPkts,
       "ruijieRrmAPSnrBSSIDHighestRxSignalStrength": ruijieRrmAPSnrBSSIDHighestRxSignalStrength,
       "ruijieRrmAPSnrBSSIDLowestRxSignalStrength": ruijieRrmAPSnrBSSIDLowestRxSignalStrength,
       "ruijieRrmAPSnrBSSIDSampleTime": ruijieRrmAPSnrBSSIDSampleTime,
       "ruijieRrmMIBTraps": ruijieRrmMIBTraps,
       "ruijieRrmTrapControl": ruijieRrmTrapControl,
       "ruijieRrmAPDot11bProfileTrapControlMask": ruijieRrmAPDot11bProfileTrapControlMask,
       "ruijieRrmAPDot11aProfileTrapControlMask": ruijieRrmAPDot11aProfileTrapControlMask,
       "ruijieRrmAPDot11bParamUpdateTrapControlMask": ruijieRrmAPDot11bParamUpdateTrapControlMask,
       "ruijieRrmAPDot11aParamUpdateTrapControlMask": ruijieRrmAPDot11aParamUpdateTrapControlMask,
       "ruijieRrmTrapVariable": ruijieRrmTrapVariable,
       "ruijieRrmAPMacAddrTrapVariable": ruijieRrmAPMacAddrTrapVariable,
       "ruijieRrmAPRadioIDTrapVariable": ruijieRrmAPRadioIDTrapVariable,
       "ruijieRrmAPRadioTypeTrapVariable": ruijieRrmAPRadioTypeTrapVariable,
       "ruijieRrmClientNumberTrapVariable": ruijieRrmClientNumberTrapVariable,
       "ruijieRrmForeignInterfereTrapVariable": ruijieRrmForeignInterfereTrapVariable,
       "ruijieRrmNoiseTrapVariable": ruijieRrmNoiseTrapVariable,
       "ruijieRrmThroughputTrapVariable": ruijieRrmThroughputTrapVariable,
       "ruijieRrmUtilizationTrapVariable": ruijieRrmUtilizationTrapVariable,
       "ruijieRrmAPTxPowerBeforeChange": ruijieRrmAPTxPowerBeforeChange,
       "ruijieRrmAPTxPowerAfterChange": ruijieRrmAPTxPowerAfterChange,
       "ruijieRrmAPChannelNumberBeforeChannge": ruijieRrmAPChannelNumberBeforeChannge,
       "ruijieRrmAPChannelNumberAfterChannge": ruijieRrmAPChannelNumberAfterChannge,
       "ruijieRrmDot11bGroupLeaderMacAddrTrapVariable": ruijieRrmDot11bGroupLeaderMacAddrTrapVariable,
       "ruijieRrmDot11aGroupLeaderMacAddrTrapVariable": ruijieRrmDot11aGroupLeaderMacAddrTrapVariable,
       "ruijieRrmAPChannelChangeReason": ruijieRrmAPChannelChangeReason,
       "ruijieRrmAPChannelChangeReasonValue": ruijieRrmAPChannelChangeReasonValue,
       "ruijieRrmAPTxPowerChangeCoverageFlag": ruijieRrmAPTxPowerChangeCoverageFlag,
       "ruijieRrmDFSFreeCount": ruijieRrmDFSFreeCount,
       "ruijieRrmAPChannelChangeCount": ruijieRrmAPChannelChangeCount,
       "ruijieRrmTraps": ruijieRrmTraps,
       "ruijieRrmAPClientNumProfileFailed": ruijieRrmAPClientNumProfileFailed,
       "ruijieRrmAPLoadProfileFailed": ruijieRrmAPLoadProfileFailed,
       "ruijieRrmAPNoiseProfileFailed": ruijieRrmAPNoiseProfileFailed,
       "ruijieRrmAPInterferenceProfileFailed": ruijieRrmAPInterferenceProfileFailed,
       "ruijieRrmAPPerformanceProfileFailed": ruijieRrmAPPerformanceProfileFailed,
       "ruijieRrmAPClientNumProfileUpdatedToPass": ruijieRrmAPClientNumProfileUpdatedToPass,
       "ruijieRrmAPLoadProfileUpdatedToPass": ruijieRrmAPLoadProfileUpdatedToPass,
       "ruijieRrmAPNoiseProfileUpdatedToPass": ruijieRrmAPNoiseProfileUpdatedToPass,
       "ruijieRrmAPInterferenceProfileUpdatedToPass": ruijieRrmAPInterferenceProfileUpdatedToPass,
       "ruijieRrmAPPerformanceProfileUpdatedToPass": ruijieRrmAPPerformanceProfileUpdatedToPass,
       "ruijieRrmAPCurrentTxPowerChanged": ruijieRrmAPCurrentTxPowerChanged,
       "ruijieRrmAPCurrentChannelChanged": ruijieRrmAPCurrentChannelChanged,
       "ruijieRrmDot11bGroupingDone": ruijieRrmDot11bGroupingDone,
       "ruijieRrmDot11aGroupingDone": ruijieRrmDot11aGroupingDone,
       "ruijieRrmDot11bDFSFreeCountBelowThreshold": ruijieRrmDot11bDFSFreeCountBelowThreshold,
       "ruijieRrmDot11aDFSFreeCountBelowThreshold": ruijieRrmDot11aDFSFreeCountBelowThreshold,
       "ruijieRrmNeighborAPInterference": ruijieRrmNeighborAPInterference,
       "ruijieRrmStationInterference": ruijieRrmStationInterference,
       "ruijieRrmOtherDiveceInterference": ruijieRrmOtherDiveceInterference,
       "ruijieRrmMIBConformance": ruijieRrmMIBConformance,
       "ruijieRrmMIBCompliances": ruijieRrmMIBCompliances,
       "ruijieRrmMIBCompliance": ruijieRrmMIBCompliance,
       "ruijieRrmMIBGroups": ruijieRrmMIBGroups,
       "ruijieRrmMIBGroup": ruijieRrmMIBGroup,
       "ruijieRrmTrapsGroup": ruijieRrmTrapsGroup,
       "ruijieRrmTrap": ruijieRrmTrap}
)
