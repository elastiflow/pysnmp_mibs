# SNMP MIB module (RUIJIE-RIP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-RIP-MIB.mib
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

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

(IfIndex,) = mibBuilder.importSymbols(
    "RUIJIE-TC",
    "IfIndex")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ruijieRIPMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13)
)
if mibBuilder.loadTexts:
    ruijieRIPMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieRIPMIBObjects_ObjectIdentity = ObjectIdentity
ruijieRIPMIBObjects = _RuijieRIPMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1)
)


class _RuijieRipEnable_Type(EnabledStatus):
    """Custom type ruijieRipEnable based on EnabledStatus"""
    defaultValue = 2


_RuijieRipEnable_Type.__name__ = "EnabledStatus"
_RuijieRipEnable_Object = MibScalar
ruijieRipEnable = _RuijieRipEnable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 1),
    _RuijieRipEnable_Type()
)
ruijieRipEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRipEnable.setStatus("current")


class _RuijieRipUpdateTime_Type(Integer32):
    """Custom type ruijieRipUpdateTime based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RuijieRipUpdateTime_Type.__name__ = "Integer32"
_RuijieRipUpdateTime_Object = MibScalar
ruijieRipUpdateTime = _RuijieRipUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 2),
    _RuijieRipUpdateTime_Type()
)
ruijieRipUpdateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRipUpdateTime.setStatus("current")


class _RuijieRipInvalidTime_Type(Integer32):
    """Custom type ruijieRipInvalidTime based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RuijieRipInvalidTime_Type.__name__ = "Integer32"
_RuijieRipInvalidTime_Object = MibScalar
ruijieRipInvalidTime = _RuijieRipInvalidTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 3),
    _RuijieRipInvalidTime_Type()
)
ruijieRipInvalidTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRipInvalidTime.setStatus("current")


class _RuijieRipHolddownTime_Type(Integer32):
    """Custom type ruijieRipHolddownTime based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RuijieRipHolddownTime_Type.__name__ = "Integer32"
_RuijieRipHolddownTime_Object = MibScalar
ruijieRipHolddownTime = _RuijieRipHolddownTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 4),
    _RuijieRipHolddownTime_Type()
)
ruijieRipHolddownTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRipHolddownTime.setStatus("current")


class _RuijieRipRecommendSetting_Type(Integer32):
    """Custom type ruijieRipRecommendSetting based on Integer32"""
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
        *(("ripv1", 1),
          ("ripv2", 2),
          ("compatible", 3))
    )


_RuijieRipRecommendSetting_Type.__name__ = "Integer32"
_RuijieRipRecommendSetting_Object = MibScalar
ruijieRipRecommendSetting = _RuijieRipRecommendSetting_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 5),
    _RuijieRipRecommendSetting_Type()
)
ruijieRipRecommendSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRipRecommendSetting.setStatus("current")
_RuijieRipIfStatTable_Object = MibTable
ruijieRipIfStatTable = _RuijieRipIfStatTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 6)
)
if mibBuilder.loadTexts:
    ruijieRipIfStatTable.setStatus("current")
_RuijieRipIfStatEntry_Object = MibTableRow
ruijieRipIfStatEntry = _RuijieRipIfStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 6, 1)
)
ruijieRipIfStatEntry.setIndexNames(
    (0, "RUIJIE-RIP-MIB", "ruijieRipIfStatIfIndex"),
)
if mibBuilder.loadTexts:
    ruijieRipIfStatEntry.setStatus("current")
_RuijieRipIfStatIfIndex_Type = IfIndex
_RuijieRipIfStatIfIndex_Object = MibTableColumn
ruijieRipIfStatIfIndex = _RuijieRipIfStatIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 6, 1, 1),
    _RuijieRipIfStatIfIndex_Type()
)
ruijieRipIfStatIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRipIfStatIfIndex.setStatus("current")
_RuijieRipIfStatRcvBadPackets_Type = Counter32
_RuijieRipIfStatRcvBadPackets_Object = MibTableColumn
ruijieRipIfStatRcvBadPackets = _RuijieRipIfStatRcvBadPackets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 6, 1, 2),
    _RuijieRipIfStatRcvBadPackets_Type()
)
ruijieRipIfStatRcvBadPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRipIfStatRcvBadPackets.setStatus("current")
_RuijieRipIfStatRcvBadRoutes_Type = Counter32
_RuijieRipIfStatRcvBadRoutes_Object = MibTableColumn
ruijieRipIfStatRcvBadRoutes = _RuijieRipIfStatRcvBadRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 6, 1, 3),
    _RuijieRipIfStatRcvBadRoutes_Type()
)
ruijieRipIfStatRcvBadRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRipIfStatRcvBadRoutes.setStatus("current")
_RuijieRipIfStatSentUpdates_Type = Counter32
_RuijieRipIfStatSentUpdates_Object = MibTableColumn
ruijieRipIfStatSentUpdates = _RuijieRipIfStatSentUpdates_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 6, 1, 4),
    _RuijieRipIfStatSentUpdates_Type()
)
ruijieRipIfStatSentUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRipIfStatSentUpdates.setStatus("current")
_RuijieRipIfConfTable_Object = MibTable
ruijieRipIfConfTable = _RuijieRipIfConfTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 7)
)
if mibBuilder.loadTexts:
    ruijieRipIfConfTable.setStatus("current")
_RuijieRipIfConfEntry_Object = MibTableRow
ruijieRipIfConfEntry = _RuijieRipIfConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 7, 1)
)
ruijieRipIfConfEntry.setIndexNames(
    (0, "RUIJIE-RIP-MIB", "ruijieRipIfConfIfIndex"),
)
if mibBuilder.loadTexts:
    ruijieRipIfConfEntry.setStatus("current")
_RuijieRipIfConfIfIndex_Type = IfIndex
_RuijieRipIfConfIfIndex_Object = MibTableColumn
ruijieRipIfConfIfIndex = _RuijieRipIfConfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 7, 1, 1),
    _RuijieRipIfConfIfIndex_Type()
)
ruijieRipIfConfIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRipIfConfIfIndex.setStatus("current")


class _RuijieRipIfConfAuthType_Type(Integer32):
    """Custom type ruijieRipIfConfAuthType based on Integer32"""
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
        *(("noAuthentication", 1),
          ("simplePassword", 2),
          ("md5", 3))
    )


_RuijieRipIfConfAuthType_Type.__name__ = "Integer32"
_RuijieRipIfConfAuthType_Object = MibTableColumn
ruijieRipIfConfAuthType = _RuijieRipIfConfAuthType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 7, 1, 2),
    _RuijieRipIfConfAuthType_Type()
)
ruijieRipIfConfAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRipIfConfAuthType.setStatus("current")


class _RuijieRipIfConfAuthKeyChain_Type(DisplayString):
    """Custom type ruijieRipIfConfAuthKeyChain based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijieRipIfConfAuthKeyChain_Type.__name__ = "DisplayString"
_RuijieRipIfConfAuthKeyChain_Object = MibTableColumn
ruijieRipIfConfAuthKeyChain = _RuijieRipIfConfAuthKeyChain_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 7, 1, 3),
    _RuijieRipIfConfAuthKeyChain_Type()
)
ruijieRipIfConfAuthKeyChain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRipIfConfAuthKeyChain.setStatus("current")


class _RuijieRipIfConfSend_Type(Integer32):
    """Custom type ruijieRipIfConfSend based on Integer32"""
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
        *(("ripVersion1", 1),
          ("rip1Compatible", 2),
          ("ripVersion2", 3))
    )


_RuijieRipIfConfSend_Type.__name__ = "Integer32"
_RuijieRipIfConfSend_Object = MibTableColumn
ruijieRipIfConfSend = _RuijieRipIfConfSend_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 7, 1, 4),
    _RuijieRipIfConfSend_Type()
)
ruijieRipIfConfSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRipIfConfSend.setStatus("current")


class _RuijieRipIfConfReceive_Type(Integer32):
    """Custom type ruijieRipIfConfReceive based on Integer32"""
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
        *(("rip1", 1),
          ("rip2", 2),
          ("rip1OrRip2", 3))
    )


_RuijieRipIfConfReceive_Type.__name__ = "Integer32"
_RuijieRipIfConfReceive_Object = MibTableColumn
ruijieRipIfConfReceive = _RuijieRipIfConfReceive_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 7, 1, 5),
    _RuijieRipIfConfReceive_Type()
)
ruijieRipIfConfReceive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRipIfConfReceive.setStatus("current")


class _RuijieRipIfPassiveStatus_Type(EnabledStatus):
    """Custom type ruijieRipIfPassiveStatus based on EnabledStatus"""
    defaultValue = 2


_RuijieRipIfPassiveStatus_Type.__name__ = "EnabledStatus"
_RuijieRipIfPassiveStatus_Object = MibTableColumn
ruijieRipIfPassiveStatus = _RuijieRipIfPassiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 7, 1, 6),
    _RuijieRipIfPassiveStatus_Type()
)
ruijieRipIfPassiveStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRipIfPassiveStatus.setStatus("current")


class _RuijieRipIfBroadcastEnable_Type(EnabledStatus):
    """Custom type ruijieRipIfBroadcastEnable based on EnabledStatus"""
    defaultValue = 2


_RuijieRipIfBroadcastEnable_Type.__name__ = "EnabledStatus"
_RuijieRipIfBroadcastEnable_Object = MibTableColumn
ruijieRipIfBroadcastEnable = _RuijieRipIfBroadcastEnable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 7, 1, 7),
    _RuijieRipIfBroadcastEnable_Type()
)
ruijieRipIfBroadcastEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRipIfBroadcastEnable.setStatus("current")
_RuijieRipIfAdminStat_Type = EnabledStatus
_RuijieRipIfAdminStat_Object = MibTableColumn
ruijieRipIfAdminStat = _RuijieRipIfAdminStat_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 7, 1, 8),
    _RuijieRipIfAdminStat_Type()
)
ruijieRipIfAdminStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRipIfAdminStat.setStatus("current")


class _RuijieRipOffsetMetric_Type(Integer32):
    """Custom type ruijieRipOffsetMetric based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_RuijieRipOffsetMetric_Type.__name__ = "Integer32"
_RuijieRipOffsetMetric_Object = MibScalar
ruijieRipOffsetMetric = _RuijieRipOffsetMetric_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 8),
    _RuijieRipOffsetMetric_Type()
)
ruijieRipOffsetMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRipOffsetMetric.setStatus("current")


class _RuijieRipAdministrativeDistance_Type(Integer32):
    """Custom type ruijieRipAdministrativeDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RuijieRipAdministrativeDistance_Type.__name__ = "Integer32"
_RuijieRipAdministrativeDistance_Object = MibScalar
ruijieRipAdministrativeDistance = _RuijieRipAdministrativeDistance_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 9),
    _RuijieRipAdministrativeDistance_Type()
)
ruijieRipAdministrativeDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRipAdministrativeDistance.setStatus("current")


class _RuijieRipValidateUpdateSrcEnable_Type(EnabledStatus):
    """Custom type ruijieRipValidateUpdateSrcEnable based on EnabledStatus"""
    defaultValue = 1


_RuijieRipValidateUpdateSrcEnable_Type.__name__ = "EnabledStatus"
_RuijieRipValidateUpdateSrcEnable_Object = MibScalar
ruijieRipValidateUpdateSrcEnable = _RuijieRipValidateUpdateSrcEnable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 10),
    _RuijieRipValidateUpdateSrcEnable_Type()
)
ruijieRipValidateUpdateSrcEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRipValidateUpdateSrcEnable.setStatus("current")


class _RuijieRipPassiveStatus_Type(EnabledStatus):
    """Custom type ruijieRipPassiveStatus based on EnabledStatus"""
    defaultValue = 2


_RuijieRipPassiveStatus_Type.__name__ = "EnabledStatus"
_RuijieRipPassiveStatus_Object = MibScalar
ruijieRipPassiveStatus = _RuijieRipPassiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 11),
    _RuijieRipPassiveStatus_Type()
)
ruijieRipPassiveStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieRipPassiveStatus.setStatus("current")
_RuijieRipNextDueIn_Type = TimeTicks
_RuijieRipNextDueIn_Object = MibScalar
ruijieRipNextDueIn = _RuijieRipNextDueIn_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 12),
    _RuijieRipNextDueIn_Type()
)
ruijieRipNextDueIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRipNextDueIn.setStatus("current")
_RuijieRipIfOffsetTable_Object = MibTable
ruijieRipIfOffsetTable = _RuijieRipIfOffsetTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 13)
)
if mibBuilder.loadTexts:
    ruijieRipIfOffsetTable.setStatus("current")
_RuijieRipIfOffsetEntry_Object = MibTableRow
ruijieRipIfOffsetEntry = _RuijieRipIfOffsetEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 13, 1)
)
ruijieRipIfOffsetEntry.setIndexNames(
    (0, "RUIJIE-RIP-MIB", "ruijieRipIfOffsetIfIndex"),
    (0, "RUIJIE-RIP-MIB", "ruijieRipIfOffsetMethod"),
)
if mibBuilder.loadTexts:
    ruijieRipIfOffsetEntry.setStatus("current")


class _RuijieRipIfOffsetIfIndex_Type(Integer32):
    """Custom type ruijieRipIfOffsetIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RuijieRipIfOffsetIfIndex_Type.__name__ = "Integer32"
_RuijieRipIfOffsetIfIndex_Object = MibTableColumn
ruijieRipIfOffsetIfIndex = _RuijieRipIfOffsetIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 13, 1, 1),
    _RuijieRipIfOffsetIfIndex_Type()
)
ruijieRipIfOffsetIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRipIfOffsetIfIndex.setStatus("current")


class _RuijieRipIfOffsetMethod_Type(Integer32):
    """Custom type ruijieRipIfOffsetMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("out", 1),
          ("in", 2))
    )


_RuijieRipIfOffsetMethod_Type.__name__ = "Integer32"
_RuijieRipIfOffsetMethod_Object = MibTableColumn
ruijieRipIfOffsetMethod = _RuijieRipIfOffsetMethod_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 13, 1, 2),
    _RuijieRipIfOffsetMethod_Type()
)
ruijieRipIfOffsetMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRipIfOffsetMethod.setStatus("current")


class _RuijieRipIfOffsetAclName_Type(DisplayString):
    """Custom type ruijieRipIfOffsetAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijieRipIfOffsetAclName_Type.__name__ = "DisplayString"
_RuijieRipIfOffsetAclName_Object = MibTableColumn
ruijieRipIfOffsetAclName = _RuijieRipIfOffsetAclName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 13, 1, 3),
    _RuijieRipIfOffsetAclName_Type()
)
ruijieRipIfOffsetAclName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieRipIfOffsetAclName.setStatus("current")


class _RuijieRipIfOffsetMetric_Type(Unsigned32):
    """Custom type ruijieRipIfOffsetMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_RuijieRipIfOffsetMetric_Type.__name__ = "Unsigned32"
_RuijieRipIfOffsetMetric_Object = MibTableColumn
ruijieRipIfOffsetMetric = _RuijieRipIfOffsetMetric_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 13, 1, 4),
    _RuijieRipIfOffsetMetric_Type()
)
ruijieRipIfOffsetMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieRipIfOffsetMetric.setStatus("current")
_RuijieRipIfOffsetStatus_Type = RowStatus
_RuijieRipIfOffsetStatus_Object = MibTableColumn
ruijieRipIfOffsetStatus = _RuijieRipIfOffsetStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 13, 1, 5),
    _RuijieRipIfOffsetStatus_Type()
)
ruijieRipIfOffsetStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieRipIfOffsetStatus.setStatus("current")
_RuijieRipNetworkTable_Object = MibTable
ruijieRipNetworkTable = _RuijieRipNetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 14)
)
if mibBuilder.loadTexts:
    ruijieRipNetworkTable.setStatus("current")
_RuijieRipNetworkEntry_Object = MibTableRow
ruijieRipNetworkEntry = _RuijieRipNetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 14, 1)
)
ruijieRipNetworkEntry.setIndexNames(
    (0, "RUIJIE-RIP-MIB", "ruijieRipNetworkAddr"),
)
if mibBuilder.loadTexts:
    ruijieRipNetworkEntry.setStatus("current")
_RuijieRipNetworkAddr_Type = IpAddress
_RuijieRipNetworkAddr_Object = MibTableColumn
ruijieRipNetworkAddr = _RuijieRipNetworkAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 14, 1, 1),
    _RuijieRipNetworkAddr_Type()
)
ruijieRipNetworkAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRipNetworkAddr.setStatus("current")
_RuijieRipNetworkMask_Type = IpAddress
_RuijieRipNetworkMask_Object = MibTableColumn
ruijieRipNetworkMask = _RuijieRipNetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 14, 1, 2),
    _RuijieRipNetworkMask_Type()
)
ruijieRipNetworkMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRipNetworkMask.setStatus("current")
_RuijieRipNetworkStatus_Type = RowStatus
_RuijieRipNetworkStatus_Object = MibTableColumn
ruijieRipNetworkStatus = _RuijieRipNetworkStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 14, 1, 3),
    _RuijieRipNetworkStatus_Type()
)
ruijieRipNetworkStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieRipNetworkStatus.setStatus("current")
_RuijieRipNeighborTable_Object = MibTable
ruijieRipNeighborTable = _RuijieRipNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 15)
)
if mibBuilder.loadTexts:
    ruijieRipNeighborTable.setStatus("current")
_RuijieRipNeighborEntry_Object = MibTableRow
ruijieRipNeighborEntry = _RuijieRipNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 15, 1)
)
ruijieRipNeighborEntry.setIndexNames(
    (0, "RUIJIE-RIP-MIB", "ruijieRipNeighborIndex"),
)
if mibBuilder.loadTexts:
    ruijieRipNeighborEntry.setStatus("current")
_RuijieRipNeighborIndex_Type = IpAddress
_RuijieRipNeighborIndex_Object = MibTableColumn
ruijieRipNeighborIndex = _RuijieRipNeighborIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 15, 1, 1),
    _RuijieRipNeighborIndex_Type()
)
ruijieRipNeighborIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieRipNeighborIndex.setStatus("current")
_RuijieRipNeighborStatus_Type = RowStatus
_RuijieRipNeighborStatus_Object = MibTableColumn
ruijieRipNeighborStatus = _RuijieRipNeighborStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 15, 1, 2),
    _RuijieRipNeighborStatus_Type()
)
ruijieRipNeighborStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieRipNeighborStatus.setStatus("current")
_RuijieRIPMIBConformance_ObjectIdentity = ObjectIdentity
ruijieRIPMIBConformance = _RuijieRIPMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 2)
)
_RuijieRIPMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieRIPMIBCompliances = _RuijieRIPMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 2, 1)
)
_RuijieRIPMIBGroups_ObjectIdentity = ObjectIdentity
ruijieRIPMIBGroups = _RuijieRIPMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 2, 2)
)

# Managed Objects groups

ruijieRipMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 2, 2, 1)
)
ruijieRipMIBGroup.setObjects(
      *(("RUIJIE-RIP-MIB", "ruijieRipEnable"),
        ("RUIJIE-RIP-MIB", "ruijieRipUpdateTime"),
        ("RUIJIE-RIP-MIB", "ruijieRipInvalidTime"),
        ("RUIJIE-RIP-MIB", "ruijieRipHolddownTime"),
        ("RUIJIE-RIP-MIB", "ruijieRipRecommendSetting"),
        ("RUIJIE-RIP-MIB", "ruijieRipIfStatIfIndex"),
        ("RUIJIE-RIP-MIB", "ruijieRipIfStatRcvBadPackets"),
        ("RUIJIE-RIP-MIB", "ruijieRipIfStatRcvBadRoutes"),
        ("RUIJIE-RIP-MIB", "ruijieRipIfStatSentUpdates"),
        ("RUIJIE-RIP-MIB", "ruijieRipIfConfIfIndex"),
        ("RUIJIE-RIP-MIB", "ruijieRipIfConfAuthType"),
        ("RUIJIE-RIP-MIB", "ruijieRipIfConfAuthKeyChain"),
        ("RUIJIE-RIP-MIB", "ruijieRipIfConfSend"),
        ("RUIJIE-RIP-MIB", "ruijieRipIfConfReceive"),
        ("RUIJIE-RIP-MIB", "ruijieRipIfPassiveStatus"),
        ("RUIJIE-RIP-MIB", "ruijieRipIfBroadcastEnable"),
        ("RUIJIE-RIP-MIB", "ruijieRipIfAdminStat"),
        ("RUIJIE-RIP-MIB", "ruijieRipOffsetMetric"),
        ("RUIJIE-RIP-MIB", "ruijieRipAdministrativeDistance"),
        ("RUIJIE-RIP-MIB", "ruijieRipValidateUpdateSrcEnable"))
)
if mibBuilder.loadTexts:
    ruijieRipMIBGroup.setStatus("current")

ruijieRIPExtendMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 2, 2, 2)
)
ruijieRIPExtendMIBGroup.setObjects(
      *(("RUIJIE-RIP-MIB", "ruijieRipNextDueIn"),
        ("RUIJIE-RIP-MIB", "ruijieRipIfOffsetIfIndex"),
        ("RUIJIE-RIP-MIB", "ruijieRipIfOffsetMethod"),
        ("RUIJIE-RIP-MIB", "ruijieRipIfOffsetAclName"),
        ("RUIJIE-RIP-MIB", "ruijieRipIfOffsetMetric"),
        ("RUIJIE-RIP-MIB", "ruijieRipIfOffsetStatus"),
        ("RUIJIE-RIP-MIB", "ruijieRipNetworkAddr"),
        ("RUIJIE-RIP-MIB", "ruijieRipNetworkMask"),
        ("RUIJIE-RIP-MIB", "ruijieRipNetworkStatus"),
        ("RUIJIE-RIP-MIB", "ruijieRipNeighborIndex"),
        ("RUIJIE-RIP-MIB", "ruijieRipNeighborStatus"))
)
if mibBuilder.loadTexts:
    ruijieRIPExtendMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ruijieRIPMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 2, 1, 1)
)
ruijieRIPMIBCompliance.setObjects(
      *(("RUIJIE-RIP-MIB", "ruijieRipMIBGroup"),
        ("RUIJIE-RIP-MIB", "ruijieRIPExtendMIBGroup"))
)
if mibBuilder.loadTexts:
    ruijieRIPMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-RIP-MIB",
    **{"ruijieRIPMIB": ruijieRIPMIB,
       "ruijieRIPMIBObjects": ruijieRIPMIBObjects,
       "ruijieRipEnable": ruijieRipEnable,
       "ruijieRipUpdateTime": ruijieRipUpdateTime,
       "ruijieRipInvalidTime": ruijieRipInvalidTime,
       "ruijieRipHolddownTime": ruijieRipHolddownTime,
       "ruijieRipRecommendSetting": ruijieRipRecommendSetting,
       "ruijieRipIfStatTable": ruijieRipIfStatTable,
       "ruijieRipIfStatEntry": ruijieRipIfStatEntry,
       "ruijieRipIfStatIfIndex": ruijieRipIfStatIfIndex,
       "ruijieRipIfStatRcvBadPackets": ruijieRipIfStatRcvBadPackets,
       "ruijieRipIfStatRcvBadRoutes": ruijieRipIfStatRcvBadRoutes,
       "ruijieRipIfStatSentUpdates": ruijieRipIfStatSentUpdates,
       "ruijieRipIfConfTable": ruijieRipIfConfTable,
       "ruijieRipIfConfEntry": ruijieRipIfConfEntry,
       "ruijieRipIfConfIfIndex": ruijieRipIfConfIfIndex,
       "ruijieRipIfConfAuthType": ruijieRipIfConfAuthType,
       "ruijieRipIfConfAuthKeyChain": ruijieRipIfConfAuthKeyChain,
       "ruijieRipIfConfSend": ruijieRipIfConfSend,
       "ruijieRipIfConfReceive": ruijieRipIfConfReceive,
       "ruijieRipIfPassiveStatus": ruijieRipIfPassiveStatus,
       "ruijieRipIfBroadcastEnable": ruijieRipIfBroadcastEnable,
       "ruijieRipIfAdminStat": ruijieRipIfAdminStat,
       "ruijieRipOffsetMetric": ruijieRipOffsetMetric,
       "ruijieRipAdministrativeDistance": ruijieRipAdministrativeDistance,
       "ruijieRipValidateUpdateSrcEnable": ruijieRipValidateUpdateSrcEnable,
       "ruijieRipPassiveStatus": ruijieRipPassiveStatus,
       "ruijieRipNextDueIn": ruijieRipNextDueIn,
       "ruijieRipIfOffsetTable": ruijieRipIfOffsetTable,
       "ruijieRipIfOffsetEntry": ruijieRipIfOffsetEntry,
       "ruijieRipIfOffsetIfIndex": ruijieRipIfOffsetIfIndex,
       "ruijieRipIfOffsetMethod": ruijieRipIfOffsetMethod,
       "ruijieRipIfOffsetAclName": ruijieRipIfOffsetAclName,
       "ruijieRipIfOffsetMetric": ruijieRipIfOffsetMetric,
       "ruijieRipIfOffsetStatus": ruijieRipIfOffsetStatus,
       "ruijieRipNetworkTable": ruijieRipNetworkTable,
       "ruijieRipNetworkEntry": ruijieRipNetworkEntry,
       "ruijieRipNetworkAddr": ruijieRipNetworkAddr,
       "ruijieRipNetworkMask": ruijieRipNetworkMask,
       "ruijieRipNetworkStatus": ruijieRipNetworkStatus,
       "ruijieRipNeighborTable": ruijieRipNeighborTable,
       "ruijieRipNeighborEntry": ruijieRipNeighborEntry,
       "ruijieRipNeighborIndex": ruijieRipNeighborIndex,
       "ruijieRipNeighborStatus": ruijieRipNeighborStatus,
       "ruijieRIPMIBConformance": ruijieRIPMIBConformance,
       "ruijieRIPMIBCompliances": ruijieRIPMIBCompliances,
       "ruijieRIPMIBCompliance": ruijieRIPMIBCompliance,
       "ruijieRIPMIBGroups": ruijieRIPMIBGroups,
       "ruijieRipMIBGroup": ruijieRipMIBGroup,
       "ruijieRIPExtendMIBGroup": ruijieRIPExtendMIBGroup}
)
