# SNMP MIB module (RUIJIE-IGMP-SNOOPING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-IGMPSNOOPING-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:04:17 2025
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

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

(IfIndex,
 MemberMap) = mibBuilder.importSymbols(
    "RUIJIE-TC",
    "IfIndex",
    "MemberMap")

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


# MODULE-IDENTITY

ruijieIgmpSnoopingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8)
)
if mibBuilder.loadTexts:
    ruijieIgmpSnoopingMIB.setRevisions(
        ("2009-10-22 00:00",
         "2002-03-20 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieIgmpSnoopingMIBObjects_ObjectIdentity = ObjectIdentity
ruijieIgmpSnoopingMIBObjects = _RuijieIgmpSnoopingMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 1)
)


class _RuijieSNIgmpWorkingMode_Type(Integer32):
    """Custom type ruijieSNIgmpWorkingMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("svgl", 2),
          ("ivgl", 3),
          ("ivgl-svgl", 4))
    )


_RuijieSNIgmpWorkingMode_Type.__name__ = "Integer32"
_RuijieSNIgmpWorkingMode_Object = MibScalar
ruijieSNIgmpWorkingMode = _RuijieSNIgmpWorkingMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 1, 1),
    _RuijieSNIgmpWorkingMode_Type()
)
ruijieSNIgmpWorkingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieSNIgmpWorkingMode.setStatus("deprecated")


class _RuijieSNIgmpSourcePortCheck_Type(EnabledStatus):
    """Custom type ruijieSNIgmpSourcePortCheck based on EnabledStatus"""
    defaultValue = 2


_RuijieSNIgmpSourcePortCheck_Type.__name__ = "EnabledStatus"
_RuijieSNIgmpSourcePortCheck_Object = MibScalar
ruijieSNIgmpSourcePortCheck = _RuijieSNIgmpSourcePortCheck_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 1, 2),
    _RuijieSNIgmpSourcePortCheck_Type()
)
ruijieSNIgmpSourcePortCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieSNIgmpSourcePortCheck.setStatus("deprecated")


class _RuijieSNIgmpSourceIpCheck_Type(EnabledStatus):
    """Custom type ruijieSNIgmpSourceIpCheck based on EnabledStatus"""
    defaultValue = 2


_RuijieSNIgmpSourceIpCheck_Type.__name__ = "EnabledStatus"
_RuijieSNIgmpSourceIpCheck_Object = MibScalar
ruijieSNIgmpSourceIpCheck = _RuijieSNIgmpSourceIpCheck_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 1, 3),
    _RuijieSNIgmpSourceIpCheck_Type()
)
ruijieSNIgmpSourceIpCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieSNIgmpSourceIpCheck.setStatus("deprecated")
_RuijieSNIgmpSourceIpCheckDefIp_Type = IpAddress
_RuijieSNIgmpSourceIpCheckDefIp_Object = MibScalar
ruijieSNIgmpSourceIpCheckDefIp = _RuijieSNIgmpSourceIpCheckDefIp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 1, 4),
    _RuijieSNIgmpSourceIpCheckDefIp_Type()
)
ruijieSNIgmpSourceIpCheckDefIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieSNIgmpSourceIpCheckDefIp.setStatus("deprecated")
_RuijieSNIgmpSrcIpCheckTable_Object = MibTable
ruijieSNIgmpSrcIpCheckTable = _RuijieSNIgmpSrcIpCheckTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 1, 5)
)
if mibBuilder.loadTexts:
    ruijieSNIgmpSrcIpCheckTable.setStatus("deprecated")
_RuijieSNIgmpSrcIpCheckEntry_Object = MibTableRow
ruijieSNIgmpSrcIpCheckEntry = _RuijieSNIgmpSrcIpCheckEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 1, 5, 1)
)
ruijieSNIgmpSrcIpCheckEntry.setIndexNames(
    (0, "RUIJIE-IGMP-SNOOPING-MIB", "ruijieSNIgmpSrcIpCheckVID"),
    (0, "RUIJIE-IGMP-SNOOPING-MIB", "ruijieSNIgmpSrcIpCheckMultiIpAddr"),
)
if mibBuilder.loadTexts:
    ruijieSNIgmpSrcIpCheckEntry.setStatus("deprecated")
_RuijieSNIgmpSrcIpCheckVID_Type = VlanId
_RuijieSNIgmpSrcIpCheckVID_Object = MibTableColumn
ruijieSNIgmpSrcIpCheckVID = _RuijieSNIgmpSrcIpCheckVID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 1, 5, 1, 1),
    _RuijieSNIgmpSrcIpCheckVID_Type()
)
ruijieSNIgmpSrcIpCheckVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSNIgmpSrcIpCheckVID.setStatus("deprecated")
_RuijieSNIgmpSrcIpCheckMultiIpAddr_Type = IpAddress
_RuijieSNIgmpSrcIpCheckMultiIpAddr_Object = MibTableColumn
ruijieSNIgmpSrcIpCheckMultiIpAddr = _RuijieSNIgmpSrcIpCheckMultiIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 1, 5, 1, 2),
    _RuijieSNIgmpSrcIpCheckMultiIpAddr_Type()
)
ruijieSNIgmpSrcIpCheckMultiIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSNIgmpSrcIpCheckMultiIpAddr.setStatus("deprecated")
_RuijieSNIgmpSrcIpCheckSrcIpAddr_Type = IpAddress
_RuijieSNIgmpSrcIpCheckSrcIpAddr_Object = MibTableColumn
ruijieSNIgmpSrcIpCheckSrcIpAddr = _RuijieSNIgmpSrcIpCheckSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 1, 5, 1, 3),
    _RuijieSNIgmpSrcIpCheckSrcIpAddr_Type()
)
ruijieSNIgmpSrcIpCheckSrcIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieSNIgmpSrcIpCheckSrcIpAddr.setStatus("deprecated")


class _RuijieSNIgmpSrcIpCheckEntryStatus_Type(Integer32):
    """Custom type ruijieSNIgmpSrcIpCheckEntryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("delete", 2))
    )


_RuijieSNIgmpSrcIpCheckEntryStatus_Type.__name__ = "Integer32"
_RuijieSNIgmpSrcIpCheckEntryStatus_Object = MibTableColumn
ruijieSNIgmpSrcIpCheckEntryStatus = _RuijieSNIgmpSrcIpCheckEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 1, 5, 1, 4),
    _RuijieSNIgmpSrcIpCheckEntryStatus_Type()
)
ruijieSNIgmpSrcIpCheckEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieSNIgmpSrcIpCheckEntryStatus.setStatus("deprecated")
_RuijieSNIgmpPortTable_Object = MibTable
ruijieSNIgmpPortTable = _RuijieSNIgmpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 1, 6)
)
if mibBuilder.loadTexts:
    ruijieSNIgmpPortTable.setStatus("deprecated")
_RuijieSNIgmpPortEntry_Object = MibTableRow
ruijieSNIgmpPortEntry = _RuijieSNIgmpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 1, 6, 1)
)
ruijieSNIgmpPortEntry.setIndexNames(
    (0, "RUIJIE-IGMP-SNOOPING-MIB", "ruijieSNIgmpPortRouterVID"),
    (0, "RUIJIE-IGMP-SNOOPING-MIB", "ruijieSNIgmpPortIndex"),
)
if mibBuilder.loadTexts:
    ruijieSNIgmpPortEntry.setStatus("deprecated")
_RuijieSNIgmpPortRouterVID_Type = VlanId
_RuijieSNIgmpPortRouterVID_Object = MibTableColumn
ruijieSNIgmpPortRouterVID = _RuijieSNIgmpPortRouterVID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 1, 6, 1, 1),
    _RuijieSNIgmpPortRouterVID_Type()
)
ruijieSNIgmpPortRouterVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieSNIgmpPortRouterVID.setStatus("deprecated")
_RuijieSNIgmpPortIndex_Type = IfIndex
_RuijieSNIgmpPortIndex_Object = MibTableColumn
ruijieSNIgmpPortIndex = _RuijieSNIgmpPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 1, 6, 1, 2),
    _RuijieSNIgmpPortIndex_Type()
)
ruijieSNIgmpPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSNIgmpPortIndex.setStatus("deprecated")


class _RuijieSNIgmpPortRouterState_Type(Integer32):
    """Custom type ruijieSNIgmpPortRouterState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mrnone", 1),
          ("mrstatic", 2),
          ("mrdynamic", 3))
    )


_RuijieSNIgmpPortRouterState_Type.__name__ = "Integer32"
_RuijieSNIgmpPortRouterState_Object = MibTableColumn
ruijieSNIgmpPortRouterState = _RuijieSNIgmpPortRouterState_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 1, 6, 1, 3),
    _RuijieSNIgmpPortRouterState_Type()
)
ruijieSNIgmpPortRouterState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieSNIgmpPortRouterState.setStatus("deprecated")
_RuijieSNIgmpPortRouterProfile_Type = Unsigned32
_RuijieSNIgmpPortRouterProfile_Object = MibTableColumn
ruijieSNIgmpPortRouterProfile = _RuijieSNIgmpPortRouterProfile_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 1, 6, 1, 4),
    _RuijieSNIgmpPortRouterProfile_Type()
)
ruijieSNIgmpPortRouterProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieSNIgmpPortRouterProfile.setStatus("deprecated")
_RuijieSNIgmpGDANumber_Type = Unsigned32
_RuijieSNIgmpGDANumber_Object = MibScalar
ruijieSNIgmpGDANumber = _RuijieSNIgmpGDANumber_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 1, 7),
    _RuijieSNIgmpGDANumber_Type()
)
ruijieSNIgmpGDANumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSNIgmpGDANumber.setStatus("deprecated")
_RuijieSNIgmpGDATable_Object = MibTable
ruijieSNIgmpGDATable = _RuijieSNIgmpGDATable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 1, 8)
)
if mibBuilder.loadTexts:
    ruijieSNIgmpGDATable.setStatus("deprecated")
_RuijieSNIgmpGDAEntry_Object = MibTableRow
ruijieSNIgmpGDAEntry = _RuijieSNIgmpGDAEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 1, 8, 1)
)
ruijieSNIgmpGDAEntry.setIndexNames(
    (0, "RUIJIE-IGMP-SNOOPING-MIB", "ruijieSNIgmpGDAVID"),
    (0, "RUIJIE-IGMP-SNOOPING-MIB", "ruijieSNIgmpGDAAddr"),
)
if mibBuilder.loadTexts:
    ruijieSNIgmpGDAEntry.setStatus("deprecated")
_RuijieSNIgmpGDAVID_Type = VlanId
_RuijieSNIgmpGDAVID_Object = MibTableColumn
ruijieSNIgmpGDAVID = _RuijieSNIgmpGDAVID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 1, 8, 1, 1),
    _RuijieSNIgmpGDAVID_Type()
)
ruijieSNIgmpGDAVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSNIgmpGDAVID.setStatus("deprecated")
_RuijieSNIgmpGDAAddr_Type = IpAddress
_RuijieSNIgmpGDAAddr_Object = MibTableColumn
ruijieSNIgmpGDAAddr = _RuijieSNIgmpGDAAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 1, 8, 1, 2),
    _RuijieSNIgmpGDAAddr_Type()
)
ruijieSNIgmpGDAAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSNIgmpGDAAddr.setStatus("deprecated")
_RuijieSNIgmpGDAPortMemberAction_Type = MemberMap
_RuijieSNIgmpGDAPortMemberAction_Object = MibTableColumn
ruijieSNIgmpGDAPortMemberAction = _RuijieSNIgmpGDAPortMemberAction_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 1, 8, 1, 3),
    _RuijieSNIgmpGDAPortMemberAction_Type()
)
ruijieSNIgmpGDAPortMemberAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieSNIgmpGDAPortMemberAction.setStatus("deprecated")
_RuijieSNIgmpGDATrunkMemberAction_Type = MemberMap
_RuijieSNIgmpGDATrunkMemberAction_Object = MibTableColumn
ruijieSNIgmpGDATrunkMemberAction = _RuijieSNIgmpGDATrunkMemberAction_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 1, 8, 1, 4),
    _RuijieSNIgmpGDATrunkMemberAction_Type()
)
ruijieSNIgmpGDATrunkMemberAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieSNIgmpGDATrunkMemberAction.setStatus("deprecated")
_RuijieSNIgmpSvglVID_Type = Integer32
_RuijieSNIgmpSvglVID_Object = MibScalar
ruijieSNIgmpSvglVID = _RuijieSNIgmpSvglVID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 1, 9),
    _RuijieSNIgmpSvglVID_Type()
)
ruijieSNIgmpSvglVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieSNIgmpSvglVID.setStatus("deprecated")
_RuijieSNIgmpSvglProfile_Type = Unsigned32
_RuijieSNIgmpSvglProfile_Object = MibScalar
ruijieSNIgmpSvglProfile = _RuijieSNIgmpSvglProfile_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 1, 10),
    _RuijieSNIgmpSvglProfile_Type()
)
ruijieSNIgmpSvglProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieSNIgmpSvglProfile.setStatus("deprecated")
_RuijieSNIgmpMrLearnTable_Object = MibTable
ruijieSNIgmpMrLearnTable = _RuijieSNIgmpMrLearnTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 1, 11)
)
if mibBuilder.loadTexts:
    ruijieSNIgmpMrLearnTable.setStatus("deprecated")
_RuijieSNIgmpMrLearnEntry_Object = MibTableRow
ruijieSNIgmpMrLearnEntry = _RuijieSNIgmpMrLearnEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 1, 11, 1)
)
ruijieSNIgmpMrLearnEntry.setIndexNames(
    (0, "RUIJIE-IGMP-SNOOPING-MIB", "ruijieSNIgmpMrLearnVID"),
)
if mibBuilder.loadTexts:
    ruijieSNIgmpMrLearnEntry.setStatus("deprecated")
_RuijieSNIgmpMrLearnVID_Type = VlanId
_RuijieSNIgmpMrLearnVID_Object = MibTableColumn
ruijieSNIgmpMrLearnVID = _RuijieSNIgmpMrLearnVID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 1, 11, 1, 1),
    _RuijieSNIgmpMrLearnVID_Type()
)
ruijieSNIgmpMrLearnVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieSNIgmpMrLearnVID.setStatus("deprecated")


class _RuijieSNIgmpMrLearnStatus_Type(Integer32):
    """Custom type ruijieSNIgmpMrLearnStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("pim-dvmrp", 2))
    )


_RuijieSNIgmpMrLearnStatus_Type.__name__ = "Integer32"
_RuijieSNIgmpMrLearnStatus_Object = MibTableColumn
ruijieSNIgmpMrLearnStatus = _RuijieSNIgmpMrLearnStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 1, 11, 1, 2),
    _RuijieSNIgmpMrLearnStatus_Type()
)
ruijieSNIgmpMrLearnStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieSNIgmpMrLearnStatus.setStatus("deprecated")
_RuijieSNIgmpPortFilteringTable_Object = MibTable
ruijieSNIgmpPortFilteringTable = _RuijieSNIgmpPortFilteringTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 1, 12)
)
if mibBuilder.loadTexts:
    ruijieSNIgmpPortFilteringTable.setStatus("deprecated")
_RuijieSNIgmpPortFilteringEntry_Object = MibTableRow
ruijieSNIgmpPortFilteringEntry = _RuijieSNIgmpPortFilteringEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 1, 12, 1)
)
ruijieSNIgmpPortFilteringEntry.setIndexNames(
    (0, "RUIJIE-IGMP-SNOOPING-MIB", "ruijieSNPortIndex"),
)
if mibBuilder.loadTexts:
    ruijieSNIgmpPortFilteringEntry.setStatus("deprecated")
_RuijieSNPortIndex_Type = IfIndex
_RuijieSNPortIndex_Object = MibTableColumn
ruijieSNPortIndex = _RuijieSNPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 1, 12, 1, 1),
    _RuijieSNPortIndex_Type()
)
ruijieSNPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSNPortIndex.setStatus("deprecated")
_RuijieSNIgmpFilteringProfile_Type = Unsigned32
_RuijieSNIgmpFilteringProfile_Object = MibTableColumn
ruijieSNIgmpFilteringProfile = _RuijieSNIgmpFilteringProfile_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 1, 12, 1, 2),
    _RuijieSNIgmpFilteringProfile_Type()
)
ruijieSNIgmpFilteringProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieSNIgmpFilteringProfile.setStatus("deprecated")
_RuijieSNIgmpFilteringMaxGroups_Type = Unsigned32
_RuijieSNIgmpFilteringMaxGroups_Object = MibTableColumn
ruijieSNIgmpFilteringMaxGroups = _RuijieSNIgmpFilteringMaxGroups_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 1, 12, 1, 3),
    _RuijieSNIgmpFilteringMaxGroups_Type()
)
ruijieSNIgmpFilteringMaxGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieSNIgmpFilteringMaxGroups.setStatus("deprecated")
_RuijieSNIgmpGDAConfigTable_Object = MibTable
ruijieSNIgmpGDAConfigTable = _RuijieSNIgmpGDAConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 1, 13)
)
if mibBuilder.loadTexts:
    ruijieSNIgmpGDAConfigTable.setStatus("deprecated")
_RuijieSNIgmpGDAConfigEntry_Object = MibTableRow
ruijieSNIgmpGDAConfigEntry = _RuijieSNIgmpGDAConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 1, 13, 1)
)
ruijieSNIgmpGDAConfigEntry.setIndexNames(
    (0, "RUIJIE-IGMP-SNOOPING-MIB", "ruijieSNIgmpGDAConfigVID"),
    (0, "RUIJIE-IGMP-SNOOPING-MIB", "ruijieSNIgmpGDAConfigAddr"),
)
if mibBuilder.loadTexts:
    ruijieSNIgmpGDAConfigEntry.setStatus("deprecated")
_RuijieSNIgmpGDAConfigVID_Type = VlanId
_RuijieSNIgmpGDAConfigVID_Object = MibTableColumn
ruijieSNIgmpGDAConfigVID = _RuijieSNIgmpGDAConfigVID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 1, 13, 1, 1),
    _RuijieSNIgmpGDAConfigVID_Type()
)
ruijieSNIgmpGDAConfigVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSNIgmpGDAConfigVID.setStatus("deprecated")
_RuijieSNIgmpGDAConfigAddr_Type = IpAddress
_RuijieSNIgmpGDAConfigAddr_Object = MibTableColumn
ruijieSNIgmpGDAConfigAddr = _RuijieSNIgmpGDAConfigAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 1, 13, 1, 2),
    _RuijieSNIgmpGDAConfigAddr_Type()
)
ruijieSNIgmpGDAConfigAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSNIgmpGDAConfigAddr.setStatus("deprecated")
_RuijieSNIgmpGDAConfigIfIndex_Type = IfIndex
_RuijieSNIgmpGDAConfigIfIndex_Object = MibTableColumn
ruijieSNIgmpGDAConfigIfIndex = _RuijieSNIgmpGDAConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 1, 13, 1, 3),
    _RuijieSNIgmpGDAConfigIfIndex_Type()
)
ruijieSNIgmpGDAConfigIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSNIgmpGDAConfigIfIndex.setStatus("deprecated")


class _RuijieSNIgmpGDAConfigType_Type(Integer32):
    """Custom type ruijieSNIgmpGDAConfigType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("null", 1),
          ("static", 2),
          ("dynamic", 3),
          ("mrouter", 4))
    )


_RuijieSNIgmpGDAConfigType_Type.__name__ = "Integer32"
_RuijieSNIgmpGDAConfigType_Object = MibTableColumn
ruijieSNIgmpGDAConfigType = _RuijieSNIgmpGDAConfigType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 1, 13, 1, 4),
    _RuijieSNIgmpGDAConfigType_Type()
)
ruijieSNIgmpGDAConfigType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSNIgmpGDAConfigType.setStatus("deprecated")


class _RuijieSNIgmpGDAConfigStatus_Type(Integer32):
    """Custom type ruijieSNIgmpGDAConfigStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("invalid", 2))
    )


_RuijieSNIgmpGDAConfigStatus_Type.__name__ = "Integer32"
_RuijieSNIgmpGDAConfigStatus_Object = MibTableColumn
ruijieSNIgmpGDAConfigStatus = _RuijieSNIgmpGDAConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 1, 13, 1, 5),
    _RuijieSNIgmpGDAConfigStatus_Type()
)
ruijieSNIgmpGDAConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSNIgmpGDAConfigStatus.setStatus("deprecated")
_RuijieSNIgmpQueryResponeTime_Type = Unsigned32
_RuijieSNIgmpQueryResponeTime_Object = MibScalar
ruijieSNIgmpQueryResponeTime = _RuijieSNIgmpQueryResponeTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 1, 14),
    _RuijieSNIgmpQueryResponeTime_Type()
)
ruijieSNIgmpQueryResponeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieSNIgmpQueryResponeTime.setStatus("deprecated")


class _RuijieIgmpSnoopingWorkingMode_Type(Integer32):
    """Custom type ruijieIgmpSnoopingWorkingMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("svgl", 2),
          ("ivgl", 3),
          ("ivgl-svgl", 4))
    )


_RuijieIgmpSnoopingWorkingMode_Type.__name__ = "Integer32"
_RuijieIgmpSnoopingWorkingMode_Object = MibScalar
ruijieIgmpSnoopingWorkingMode = _RuijieIgmpSnoopingWorkingMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 1, 15),
    _RuijieIgmpSnoopingWorkingMode_Type()
)
ruijieIgmpSnoopingWorkingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieIgmpSnoopingWorkingMode.setStatus("current")
_RuijieIgmpSnoopingGDANumber_Type = Unsigned32
_RuijieIgmpSnoopingGDANumber_Object = MibScalar
ruijieIgmpSnoopingGDANumber = _RuijieIgmpSnoopingGDANumber_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 1, 16),
    _RuijieIgmpSnoopingGDANumber_Type()
)
ruijieIgmpSnoopingGDANumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIgmpSnoopingGDANumber.setStatus("current")
_RuijieIgmpSnoopingGDATable_Object = MibTable
ruijieIgmpSnoopingGDATable = _RuijieIgmpSnoopingGDATable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 1, 17)
)
if mibBuilder.loadTexts:
    ruijieIgmpSnoopingGDATable.setStatus("current")
_RuijieIgmpSnoopingGDAEntry_Object = MibTableRow
ruijieIgmpSnoopingGDAEntry = _RuijieIgmpSnoopingGDAEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 1, 17, 1)
)
ruijieIgmpSnoopingGDAEntry.setIndexNames(
    (0, "RUIJIE-IGMP-SNOOPING-MIB", "ruijieIgmpSnoopingGDAVID"),
    (0, "RUIJIE-IGMP-SNOOPING-MIB", "ruijieIgmpSnoopingGDAAddr"),
)
if mibBuilder.loadTexts:
    ruijieIgmpSnoopingGDAEntry.setStatus("current")
_RuijieIgmpSnoopingGDAVID_Type = VlanId
_RuijieIgmpSnoopingGDAVID_Object = MibTableColumn
ruijieIgmpSnoopingGDAVID = _RuijieIgmpSnoopingGDAVID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 1, 17, 1, 1),
    _RuijieIgmpSnoopingGDAVID_Type()
)
ruijieIgmpSnoopingGDAVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIgmpSnoopingGDAVID.setStatus("current")
_RuijieIgmpSnoopingGDAAddr_Type = IpAddress
_RuijieIgmpSnoopingGDAAddr_Object = MibTableColumn
ruijieIgmpSnoopingGDAAddr = _RuijieIgmpSnoopingGDAAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 1, 17, 1, 2),
    _RuijieIgmpSnoopingGDAAddr_Type()
)
ruijieIgmpSnoopingGDAAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIgmpSnoopingGDAAddr.setStatus("current")
_RuijieIgmpSnoopingGDAPortMemberAction_Type = MemberMap
_RuijieIgmpSnoopingGDAPortMemberAction_Object = MibTableColumn
ruijieIgmpSnoopingGDAPortMemberAction = _RuijieIgmpSnoopingGDAPortMemberAction_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 1, 17, 1, 3),
    _RuijieIgmpSnoopingGDAPortMemberAction_Type()
)
ruijieIgmpSnoopingGDAPortMemberAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieIgmpSnoopingGDAPortMemberAction.setStatus("current")
_RuijieIgmpSnoopingVlanStatusTable_Object = MibTable
ruijieIgmpSnoopingVlanStatusTable = _RuijieIgmpSnoopingVlanStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 1, 18)
)
if mibBuilder.loadTexts:
    ruijieIgmpSnoopingVlanStatusTable.setStatus("current")
_RuijieIgmpSnoopingVlanStatusEntry_Object = MibTableRow
ruijieIgmpSnoopingVlanStatusEntry = _RuijieIgmpSnoopingVlanStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 1, 18, 1)
)
ruijieIgmpSnoopingVlanStatusEntry.setIndexNames(
    (0, "RUIJIE-IGMP-SNOOPING-MIB", "ruijieIgmpSnoopingVlanStatusVID"),
)
if mibBuilder.loadTexts:
    ruijieIgmpSnoopingVlanStatusEntry.setStatus("current")
_RuijieIgmpSnoopingVlanStatusVID_Type = VlanId
_RuijieIgmpSnoopingVlanStatusVID_Object = MibTableColumn
ruijieIgmpSnoopingVlanStatusVID = _RuijieIgmpSnoopingVlanStatusVID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 1, 18, 1, 1),
    _RuijieIgmpSnoopingVlanStatusVID_Type()
)
ruijieIgmpSnoopingVlanStatusVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieIgmpSnoopingVlanStatusVID.setStatus("current")
_RuijieIgmpSnoopingVlanStatusStatus_Type = EnabledStatus
_RuijieIgmpSnoopingVlanStatusStatus_Object = MibTableColumn
ruijieIgmpSnoopingVlanStatusStatus = _RuijieIgmpSnoopingVlanStatusStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 1, 18, 1, 2),
    _RuijieIgmpSnoopingVlanStatusStatus_Type()
)
ruijieIgmpSnoopingVlanStatusStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieIgmpSnoopingVlanStatusStatus.setStatus("current")
_RuijieIgmpSnoopingSvglVID_Type = Integer32
_RuijieIgmpSnoopingSvglVID_Object = MibScalar
ruijieIgmpSnoopingSvglVID = _RuijieIgmpSnoopingSvglVID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 1, 19),
    _RuijieIgmpSnoopingSvglVID_Type()
)
ruijieIgmpSnoopingSvglVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieIgmpSnoopingSvglVID.setStatus("current")
_RuijieIgmpSnoopingSvglProfile_Type = Unsigned32
_RuijieIgmpSnoopingSvglProfile_Object = MibScalar
ruijieIgmpSnoopingSvglProfile = _RuijieIgmpSnoopingSvglProfile_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 1, 20),
    _RuijieIgmpSnoopingSvglProfile_Type()
)
ruijieIgmpSnoopingSvglProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieIgmpSnoopingSvglProfile.setStatus("current")
_RuijieIgmpSnoopingMrLearnTable_Object = MibTable
ruijieIgmpSnoopingMrLearnTable = _RuijieIgmpSnoopingMrLearnTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 1, 21)
)
if mibBuilder.loadTexts:
    ruijieIgmpSnoopingMrLearnTable.setStatus("current")
_RuijieIgmpSnoopingMrLearnEntry_Object = MibTableRow
ruijieIgmpSnoopingMrLearnEntry = _RuijieIgmpSnoopingMrLearnEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 1, 21, 1)
)
ruijieIgmpSnoopingMrLearnEntry.setIndexNames(
    (0, "RUIJIE-IGMP-SNOOPING-MIB", "ruijieIgmpSnoopingMrLearnVID"),
)
if mibBuilder.loadTexts:
    ruijieIgmpSnoopingMrLearnEntry.setStatus("current")
_RuijieIgmpSnoopingMrLearnVID_Type = VlanId
_RuijieIgmpSnoopingMrLearnVID_Object = MibTableColumn
ruijieIgmpSnoopingMrLearnVID = _RuijieIgmpSnoopingMrLearnVID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 1, 21, 1, 1),
    _RuijieIgmpSnoopingMrLearnVID_Type()
)
ruijieIgmpSnoopingMrLearnVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieIgmpSnoopingMrLearnVID.setStatus("current")


class _RuijieIgmpSnoopingMrLearnStatus_Type(Integer32):
    """Custom type ruijieIgmpSnoopingMrLearnStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("pim-dvmrp", 2))
    )


_RuijieIgmpSnoopingMrLearnStatus_Type.__name__ = "Integer32"
_RuijieIgmpSnoopingMrLearnStatus_Object = MibTableColumn
ruijieIgmpSnoopingMrLearnStatus = _RuijieIgmpSnoopingMrLearnStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 1, 21, 1, 2),
    _RuijieIgmpSnoopingMrLearnStatus_Type()
)
ruijieIgmpSnoopingMrLearnStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieIgmpSnoopingMrLearnStatus.setStatus("current")
_RuijieIgmpSnoopingPortFilteringTable_Object = MibTable
ruijieIgmpSnoopingPortFilteringTable = _RuijieIgmpSnoopingPortFilteringTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 1, 22)
)
if mibBuilder.loadTexts:
    ruijieIgmpSnoopingPortFilteringTable.setStatus("current")
_RuijieIgmpSnoopingPortFilteringEntry_Object = MibTableRow
ruijieIgmpSnoopingPortFilteringEntry = _RuijieIgmpSnoopingPortFilteringEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 1, 22, 1)
)
ruijieIgmpSnoopingPortFilteringEntry.setIndexNames(
    (0, "RUIJIE-IGMP-SNOOPING-MIB", "ruijieIgmpSnoopingportIndex"),
)
if mibBuilder.loadTexts:
    ruijieIgmpSnoopingPortFilteringEntry.setStatus("current")
_RuijieIgmpSnoopingportIndex_Type = IfIndex
_RuijieIgmpSnoopingportIndex_Object = MibTableColumn
ruijieIgmpSnoopingportIndex = _RuijieIgmpSnoopingportIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 1, 22, 1, 1),
    _RuijieIgmpSnoopingportIndex_Type()
)
ruijieIgmpSnoopingportIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIgmpSnoopingportIndex.setStatus("current")
_RuijieIgmpSnoopingFilteringProfile_Type = Unsigned32
_RuijieIgmpSnoopingFilteringProfile_Object = MibTableColumn
ruijieIgmpSnoopingFilteringProfile = _RuijieIgmpSnoopingFilteringProfile_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 1, 22, 1, 2),
    _RuijieIgmpSnoopingFilteringProfile_Type()
)
ruijieIgmpSnoopingFilteringProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieIgmpSnoopingFilteringProfile.setStatus("current")
_RuijieIgmpSnoopingFilteringMaxGroups_Type = Unsigned32
_RuijieIgmpSnoopingFilteringMaxGroups_Object = MibTableColumn
ruijieIgmpSnoopingFilteringMaxGroups = _RuijieIgmpSnoopingFilteringMaxGroups_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 1, 22, 1, 3),
    _RuijieIgmpSnoopingFilteringMaxGroups_Type()
)
ruijieIgmpSnoopingFilteringMaxGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieIgmpSnoopingFilteringMaxGroups.setStatus("current")
_RuijieIgmpSnoopingGDAConfigTable_Object = MibTable
ruijieIgmpSnoopingGDAConfigTable = _RuijieIgmpSnoopingGDAConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 1, 23)
)
if mibBuilder.loadTexts:
    ruijieIgmpSnoopingGDAConfigTable.setStatus("current")
_RuijieIgmpSnoopingGDAConfigEntry_Object = MibTableRow
ruijieIgmpSnoopingGDAConfigEntry = _RuijieIgmpSnoopingGDAConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 1, 23, 1)
)
ruijieIgmpSnoopingGDAConfigEntry.setIndexNames(
    (0, "RUIJIE-IGMP-SNOOPING-MIB", "ruijieIgmpSnoopingGDAConfigVID"),
    (0, "RUIJIE-IGMP-SNOOPING-MIB", "ruijieIgmpSnoopingGDAConfigAddr"),
    (0, "RUIJIE-IGMP-SNOOPING-MIB", "ruijieIgmpSnoopingGDAConfigIfIndex"),
)
if mibBuilder.loadTexts:
    ruijieIgmpSnoopingGDAConfigEntry.setStatus("current")
_RuijieIgmpSnoopingGDAConfigVID_Type = VlanId
_RuijieIgmpSnoopingGDAConfigVID_Object = MibTableColumn
ruijieIgmpSnoopingGDAConfigVID = _RuijieIgmpSnoopingGDAConfigVID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 1, 23, 1, 1),
    _RuijieIgmpSnoopingGDAConfigVID_Type()
)
ruijieIgmpSnoopingGDAConfigVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIgmpSnoopingGDAConfigVID.setStatus("current")
_RuijieIgmpSnoopingGDAConfigAddr_Type = IpAddress
_RuijieIgmpSnoopingGDAConfigAddr_Object = MibTableColumn
ruijieIgmpSnoopingGDAConfigAddr = _RuijieIgmpSnoopingGDAConfigAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 1, 23, 1, 2),
    _RuijieIgmpSnoopingGDAConfigAddr_Type()
)
ruijieIgmpSnoopingGDAConfigAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIgmpSnoopingGDAConfigAddr.setStatus("current")
_RuijieIgmpSnoopingGDAConfigIfIndex_Type = IfIndex
_RuijieIgmpSnoopingGDAConfigIfIndex_Object = MibTableColumn
ruijieIgmpSnoopingGDAConfigIfIndex = _RuijieIgmpSnoopingGDAConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 1, 23, 1, 3),
    _RuijieIgmpSnoopingGDAConfigIfIndex_Type()
)
ruijieIgmpSnoopingGDAConfigIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIgmpSnoopingGDAConfigIfIndex.setStatus("current")
_RuijieIgmpSnoopingQueryResponeTime_Type = Unsigned32
_RuijieIgmpSnoopingQueryResponeTime_Object = MibScalar
ruijieIgmpSnoopingQueryResponeTime = _RuijieIgmpSnoopingQueryResponeTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 1, 24),
    _RuijieIgmpSnoopingQueryResponeTime_Type()
)
ruijieIgmpSnoopingQueryResponeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieIgmpSnoopingQueryResponeTime.setStatus("current")
_RuijieIgmpSnoopingReportSuppress_Type = TruthValue
_RuijieIgmpSnoopingReportSuppress_Object = MibScalar
ruijieIgmpSnoopingReportSuppress = _RuijieIgmpSnoopingReportSuppress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 1, 25),
    _RuijieIgmpSnoopingReportSuppress_Type()
)
ruijieIgmpSnoopingReportSuppress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieIgmpSnoopingReportSuppress.setStatus("current")
_RuijieIgmpSnoopingFastleave_Type = TruthValue
_RuijieIgmpSnoopingFastleave_Object = MibScalar
ruijieIgmpSnoopingFastleave = _RuijieIgmpSnoopingFastleave_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 1, 26),
    _RuijieIgmpSnoopingFastleave_Type()
)
ruijieIgmpSnoopingFastleave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieIgmpSnoopingFastleave.setStatus("current")
_RuijieIgmpSnoopingGDANewTable_Object = MibTable
ruijieIgmpSnoopingGDANewTable = _RuijieIgmpSnoopingGDANewTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 1, 27)
)
if mibBuilder.loadTexts:
    ruijieIgmpSnoopingGDANewTable.setStatus("current")
_RuijieIgmpSnoopingGDANewEntry_Object = MibTableRow
ruijieIgmpSnoopingGDANewEntry = _RuijieIgmpSnoopingGDANewEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 1, 27, 1)
)
ruijieIgmpSnoopingGDANewEntry.setIndexNames(
    (0, "RUIJIE-IGMP-SNOOPING-MIB", "ruijieIgmpSnoopingGDANewInVID"),
    (0, "RUIJIE-IGMP-SNOOPING-MIB", "ruijieIgmpSnoopingGDANewOutVID"),
    (0, "RUIJIE-IGMP-SNOOPING-MIB", "ruijieIgsmpSnoopingGDASrc"),
    (0, "RUIJIE-IGMP-SNOOPING-MIB", "ruijieIgmpSnoopingGDAGrp"),
    (0, "RUIJIE-IGMP-SNOOPING-MIB", "ruijieIgmpSnoopingGDAIfx"),
)
if mibBuilder.loadTexts:
    ruijieIgmpSnoopingGDANewEntry.setStatus("current")
_RuijieIgmpSnoopingGDANewInVID_Type = VlanId
_RuijieIgmpSnoopingGDANewInVID_Object = MibTableColumn
ruijieIgmpSnoopingGDANewInVID = _RuijieIgmpSnoopingGDANewInVID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 1, 27, 1, 1),
    _RuijieIgmpSnoopingGDANewInVID_Type()
)
ruijieIgmpSnoopingGDANewInVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIgmpSnoopingGDANewInVID.setStatus("current")
_RuijieIgmpSnoopingGDANewOutVID_Type = VlanId
_RuijieIgmpSnoopingGDANewOutVID_Object = MibTableColumn
ruijieIgmpSnoopingGDANewOutVID = _RuijieIgmpSnoopingGDANewOutVID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 1, 27, 1, 2),
    _RuijieIgmpSnoopingGDANewOutVID_Type()
)
ruijieIgmpSnoopingGDANewOutVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIgmpSnoopingGDANewOutVID.setStatus("current")
_RuijieIgsmpSnoopingGDASrc_Type = IpAddress
_RuijieIgsmpSnoopingGDASrc_Object = MibTableColumn
ruijieIgsmpSnoopingGDASrc = _RuijieIgsmpSnoopingGDASrc_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 1, 27, 1, 3),
    _RuijieIgsmpSnoopingGDASrc_Type()
)
ruijieIgsmpSnoopingGDASrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIgsmpSnoopingGDASrc.setStatus("current")
_RuijieIgmpSnoopingGDAGrp_Type = IpAddress
_RuijieIgmpSnoopingGDAGrp_Object = MibTableColumn
ruijieIgmpSnoopingGDAGrp = _RuijieIgmpSnoopingGDAGrp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 1, 27, 1, 4),
    _RuijieIgmpSnoopingGDAGrp_Type()
)
ruijieIgmpSnoopingGDAGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIgmpSnoopingGDAGrp.setStatus("current")
_RuijieIgmpSnoopingGDAIfx_Type = IfIndex
_RuijieIgmpSnoopingGDAIfx_Object = MibTableColumn
ruijieIgmpSnoopingGDAIfx = _RuijieIgmpSnoopingGDAIfx_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 1, 27, 1, 5),
    _RuijieIgmpSnoopingGDAIfx_Type()
)
ruijieIgmpSnoopingGDAIfx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIgmpSnoopingGDAIfx.setStatus("current")
_RuijieIgmpSnoopingGDAIfxAction_Type = Integer32
_RuijieIgmpSnoopingGDAIfxAction_Object = MibTableColumn
ruijieIgmpSnoopingGDAIfxAction = _RuijieIgmpSnoopingGDAIfxAction_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 1, 27, 1, 6),
    _RuijieIgmpSnoopingGDAIfxAction_Type()
)
ruijieIgmpSnoopingGDAIfxAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieIgmpSnoopingGDAIfxAction.setStatus("current")


class _RuijieIgmpSnoopingMulticastWlan_Type(Integer32):
    """Custom type ruijieIgmpSnoopingMulticastWlan based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enable", 1))
    )


_RuijieIgmpSnoopingMulticastWlan_Type.__name__ = "Integer32"
_RuijieIgmpSnoopingMulticastWlan_Object = MibScalar
ruijieIgmpSnoopingMulticastWlan = _RuijieIgmpSnoopingMulticastWlan_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 1, 28),
    _RuijieIgmpSnoopingMulticastWlan_Type()
)
ruijieIgmpSnoopingMulticastWlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieIgmpSnoopingMulticastWlan.setStatus("current")
_RuijieIgmpSnoopingMIBConformance_ObjectIdentity = ObjectIdentity
ruijieIgmpSnoopingMIBConformance = _RuijieIgmpSnoopingMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 2)
)
_RuijieIgmpSnoopingMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieIgmpSnoopingMIBCompliances = _RuijieIgmpSnoopingMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 2, 1)
)
_RuijieIgmpSnoopingMIBGroups_ObjectIdentity = ObjectIdentity
ruijieIgmpSnoopingMIBGroups = _RuijieIgmpSnoopingMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 2, 2)
)

# Managed Objects groups

ruijieIgmpSnoopingMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 2, 2, 1)
)
ruijieIgmpSnoopingMIBGroup.setObjects(
      *(("RUIJIE-IGMP-SNOOPING-MIB", "ruijieSNIgmpWorkingMode"),
        ("RUIJIE-IGMP-SNOOPING-MIB", "ruijieSNIgmpSourcePortCheck"),
        ("RUIJIE-IGMP-SNOOPING-MIB", "ruijieSNIgmpSourceIpCheck"),
        ("RUIJIE-IGMP-SNOOPING-MIB", "ruijieSNIgmpSourceIpCheckDefIp"),
        ("RUIJIE-IGMP-SNOOPING-MIB", "ruijieSNIgmpSrcIpCheckVID"),
        ("RUIJIE-IGMP-SNOOPING-MIB", "ruijieSNIgmpSrcIpCheckMultiIpAddr"),
        ("RUIJIE-IGMP-SNOOPING-MIB", "ruijieSNIgmpSrcIpCheckSrcIpAddr"),
        ("RUIJIE-IGMP-SNOOPING-MIB", "ruijieSNIgmpSrcIpCheckEntryStatus"),
        ("RUIJIE-IGMP-SNOOPING-MIB", "ruijieSNIgmpPortRouterVID"),
        ("RUIJIE-IGMP-SNOOPING-MIB", "ruijieSNIgmpPortIndex"),
        ("RUIJIE-IGMP-SNOOPING-MIB", "ruijieSNIgmpPortRouterState"),
        ("RUIJIE-IGMP-SNOOPING-MIB", "ruijieSNIgmpPortRouterProfile"),
        ("RUIJIE-IGMP-SNOOPING-MIB", "ruijieSNIgmpGDANumber"),
        ("RUIJIE-IGMP-SNOOPING-MIB", "ruijieSNIgmpGDAVID"),
        ("RUIJIE-IGMP-SNOOPING-MIB", "ruijieSNIgmpGDAAddr"),
        ("RUIJIE-IGMP-SNOOPING-MIB", "ruijieSNIgmpGDAPortMemberAction"),
        ("RUIJIE-IGMP-SNOOPING-MIB", "ruijieSNIgmpGDATrunkMemberAction"),
        ("RUIJIE-IGMP-SNOOPING-MIB", "ruijieSNIgmpSvglVID"),
        ("RUIJIE-IGMP-SNOOPING-MIB", "ruijieSNIgmpSvglProfile"),
        ("RUIJIE-IGMP-SNOOPING-MIB", "ruijieSNIgmpMrLearnVID"),
        ("RUIJIE-IGMP-SNOOPING-MIB", "ruijieSNIgmpMrLearnStatus"),
        ("RUIJIE-IGMP-SNOOPING-MIB", "ruijieSNPortIndex"),
        ("RUIJIE-IGMP-SNOOPING-MIB", "ruijieSNIgmpFilteringProfile"),
        ("RUIJIE-IGMP-SNOOPING-MIB", "ruijieSNIgmpFilteringMaxGroups"),
        ("RUIJIE-IGMP-SNOOPING-MIB", "ruijieSNIgmpGDAConfigVID"),
        ("RUIJIE-IGMP-SNOOPING-MIB", "ruijieSNIgmpGDAConfigAddr"),
        ("RUIJIE-IGMP-SNOOPING-MIB", "ruijieSNIgmpGDAConfigIfIndex"),
        ("RUIJIE-IGMP-SNOOPING-MIB", "ruijieSNIgmpGDAConfigType"),
        ("RUIJIE-IGMP-SNOOPING-MIB", "ruijieSNIgmpGDAConfigStatus"),
        ("RUIJIE-IGMP-SNOOPING-MIB", "ruijieSNIgmpQueryResponeTime"))
)
if mibBuilder.loadTexts:
    ruijieIgmpSnoopingMIBGroup.setStatus("deprecated")

ruijieIgmpSnoopingMIBGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 2, 2, 2)
)
ruijieIgmpSnoopingMIBGroup2.setObjects(
      *(("RUIJIE-IGMP-SNOOPING-MIB", "ruijieIgmpSnoopingWorkingMode"),
        ("RUIJIE-IGMP-SNOOPING-MIB", "ruijieIgmpSnoopingGDANumber"),
        ("RUIJIE-IGMP-SNOOPING-MIB", "ruijieIgmpSnoopingGDAVID"),
        ("RUIJIE-IGMP-SNOOPING-MIB", "ruijieIgmpSnoopingGDAAddr"),
        ("RUIJIE-IGMP-SNOOPING-MIB", "ruijieIgmpSnoopingGDAPortMemberAction"),
        ("RUIJIE-IGMP-SNOOPING-MIB", "ruijieIgmpSnoopingVlanStatusVID"),
        ("RUIJIE-IGMP-SNOOPING-MIB", "ruijieIgmpSnoopingVlanStatusStatus"),
        ("RUIJIE-IGMP-SNOOPING-MIB", "ruijieIgmpSnoopingSvglVID"),
        ("RUIJIE-IGMP-SNOOPING-MIB", "ruijieIgmpSnoopingSvglProfile"),
        ("RUIJIE-IGMP-SNOOPING-MIB", "ruijieIgmpSnoopingMrLearnVID"),
        ("RUIJIE-IGMP-SNOOPING-MIB", "ruijieIgmpSnoopingMrLearnStatus"),
        ("RUIJIE-IGMP-SNOOPING-MIB", "ruijieIgmpSnoopingportIndex"),
        ("RUIJIE-IGMP-SNOOPING-MIB", "ruijieIgmpSnoopingFilteringProfile"),
        ("RUIJIE-IGMP-SNOOPING-MIB", "ruijieIgmpSnoopingFilteringMaxGroups"),
        ("RUIJIE-IGMP-SNOOPING-MIB", "ruijieIgmpSnoopingGDAConfigVID"),
        ("RUIJIE-IGMP-SNOOPING-MIB", "ruijieIgmpSnoopingGDAConfigAddr"),
        ("RUIJIE-IGMP-SNOOPING-MIB", "ruijieIgmpSnoopingGDAConfigIfIndex"),
        ("RUIJIE-IGMP-SNOOPING-MIB", "ruijieIgmpSnoopingQueryResponeTime"),
        ("RUIJIE-IGMP-SNOOPING-MIB", "ruijieIgmpSnoopingReportSuppress"),
        ("RUIJIE-IGMP-SNOOPING-MIB", "ruijieIgmpSnoopingFastleave"),
        ("RUIJIE-IGMP-SNOOPING-MIB", "ruijieIgmpSnoopingGDANewInVID"),
        ("RUIJIE-IGMP-SNOOPING-MIB", "ruijieIgmpSnoopingGDANewOutVID"),
        ("RUIJIE-IGMP-SNOOPING-MIB", "ruijieIgsmpSnoopingGDASrc"),
        ("RUIJIE-IGMP-SNOOPING-MIB", "ruijieIgmpSnoopingGDAGrp"),
        ("RUIJIE-IGMP-SNOOPING-MIB", "ruijieIgmpSnoopingGDAIfx"),
        ("RUIJIE-IGMP-SNOOPING-MIB", "ruijieIgmpSnoopingGDAIfxAction"),
        ("RUIJIE-IGMP-SNOOPING-MIB", "ruijieIgmpSnoopingMulticastWlan"))
)
if mibBuilder.loadTexts:
    ruijieIgmpSnoopingMIBGroup2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ruijieIgmpSnoopingMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 2, 1, 1)
)
ruijieIgmpSnoopingMIBCompliance.setObjects(
    ("RUIJIE-IGMP-SNOOPING-MIB", "ruijieIgmpSnoopingMIBGroup")
)
if mibBuilder.loadTexts:
    ruijieIgmpSnoopingMIBCompliance.setStatus(
        "deprecated"
    )

ruijieIgmpSnoopingMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 8, 2, 1, 2)
)
ruijieIgmpSnoopingMIBCompliance2.setObjects(
    ("RUIJIE-IGMP-SNOOPING-MIB", "ruijieIgmpSnoopingMIBGroup2")
)
if mibBuilder.loadTexts:
    ruijieIgmpSnoopingMIBCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-IGMP-SNOOPING-MIB",
    **{"ruijieIgmpSnoopingMIB": ruijieIgmpSnoopingMIB,
       "ruijieIgmpSnoopingMIBObjects": ruijieIgmpSnoopingMIBObjects,
       "ruijieSNIgmpWorkingMode": ruijieSNIgmpWorkingMode,
       "ruijieSNIgmpSourcePortCheck": ruijieSNIgmpSourcePortCheck,
       "ruijieSNIgmpSourceIpCheck": ruijieSNIgmpSourceIpCheck,
       "ruijieSNIgmpSourceIpCheckDefIp": ruijieSNIgmpSourceIpCheckDefIp,
       "ruijieSNIgmpSrcIpCheckTable": ruijieSNIgmpSrcIpCheckTable,
       "ruijieSNIgmpSrcIpCheckEntry": ruijieSNIgmpSrcIpCheckEntry,
       "ruijieSNIgmpSrcIpCheckVID": ruijieSNIgmpSrcIpCheckVID,
       "ruijieSNIgmpSrcIpCheckMultiIpAddr": ruijieSNIgmpSrcIpCheckMultiIpAddr,
       "ruijieSNIgmpSrcIpCheckSrcIpAddr": ruijieSNIgmpSrcIpCheckSrcIpAddr,
       "ruijieSNIgmpSrcIpCheckEntryStatus": ruijieSNIgmpSrcIpCheckEntryStatus,
       "ruijieSNIgmpPortTable": ruijieSNIgmpPortTable,
       "ruijieSNIgmpPortEntry": ruijieSNIgmpPortEntry,
       "ruijieSNIgmpPortRouterVID": ruijieSNIgmpPortRouterVID,
       "ruijieSNIgmpPortIndex": ruijieSNIgmpPortIndex,
       "ruijieSNIgmpPortRouterState": ruijieSNIgmpPortRouterState,
       "ruijieSNIgmpPortRouterProfile": ruijieSNIgmpPortRouterProfile,
       "ruijieSNIgmpGDANumber": ruijieSNIgmpGDANumber,
       "ruijieSNIgmpGDATable": ruijieSNIgmpGDATable,
       "ruijieSNIgmpGDAEntry": ruijieSNIgmpGDAEntry,
       "ruijieSNIgmpGDAVID": ruijieSNIgmpGDAVID,
       "ruijieSNIgmpGDAAddr": ruijieSNIgmpGDAAddr,
       "ruijieSNIgmpGDAPortMemberAction": ruijieSNIgmpGDAPortMemberAction,
       "ruijieSNIgmpGDATrunkMemberAction": ruijieSNIgmpGDATrunkMemberAction,
       "ruijieSNIgmpSvglVID": ruijieSNIgmpSvglVID,
       "ruijieSNIgmpSvglProfile": ruijieSNIgmpSvglProfile,
       "ruijieSNIgmpMrLearnTable": ruijieSNIgmpMrLearnTable,
       "ruijieSNIgmpMrLearnEntry": ruijieSNIgmpMrLearnEntry,
       "ruijieSNIgmpMrLearnVID": ruijieSNIgmpMrLearnVID,
       "ruijieSNIgmpMrLearnStatus": ruijieSNIgmpMrLearnStatus,
       "ruijieSNIgmpPortFilteringTable": ruijieSNIgmpPortFilteringTable,
       "ruijieSNIgmpPortFilteringEntry": ruijieSNIgmpPortFilteringEntry,
       "ruijieSNPortIndex": ruijieSNPortIndex,
       "ruijieSNIgmpFilteringProfile": ruijieSNIgmpFilteringProfile,
       "ruijieSNIgmpFilteringMaxGroups": ruijieSNIgmpFilteringMaxGroups,
       "ruijieSNIgmpGDAConfigTable": ruijieSNIgmpGDAConfigTable,
       "ruijieSNIgmpGDAConfigEntry": ruijieSNIgmpGDAConfigEntry,
       "ruijieSNIgmpGDAConfigVID": ruijieSNIgmpGDAConfigVID,
       "ruijieSNIgmpGDAConfigAddr": ruijieSNIgmpGDAConfigAddr,
       "ruijieSNIgmpGDAConfigIfIndex": ruijieSNIgmpGDAConfigIfIndex,
       "ruijieSNIgmpGDAConfigType": ruijieSNIgmpGDAConfigType,
       "ruijieSNIgmpGDAConfigStatus": ruijieSNIgmpGDAConfigStatus,
       "ruijieSNIgmpQueryResponeTime": ruijieSNIgmpQueryResponeTime,
       "ruijieIgmpSnoopingWorkingMode": ruijieIgmpSnoopingWorkingMode,
       "ruijieIgmpSnoopingGDANumber": ruijieIgmpSnoopingGDANumber,
       "ruijieIgmpSnoopingGDATable": ruijieIgmpSnoopingGDATable,
       "ruijieIgmpSnoopingGDAEntry": ruijieIgmpSnoopingGDAEntry,
       "ruijieIgmpSnoopingGDAVID": ruijieIgmpSnoopingGDAVID,
       "ruijieIgmpSnoopingGDAAddr": ruijieIgmpSnoopingGDAAddr,
       "ruijieIgmpSnoopingGDAPortMemberAction": ruijieIgmpSnoopingGDAPortMemberAction,
       "ruijieIgmpSnoopingVlanStatusTable": ruijieIgmpSnoopingVlanStatusTable,
       "ruijieIgmpSnoopingVlanStatusEntry": ruijieIgmpSnoopingVlanStatusEntry,
       "ruijieIgmpSnoopingVlanStatusVID": ruijieIgmpSnoopingVlanStatusVID,
       "ruijieIgmpSnoopingVlanStatusStatus": ruijieIgmpSnoopingVlanStatusStatus,
       "ruijieIgmpSnoopingSvglVID": ruijieIgmpSnoopingSvglVID,
       "ruijieIgmpSnoopingSvglProfile": ruijieIgmpSnoopingSvglProfile,
       "ruijieIgmpSnoopingMrLearnTable": ruijieIgmpSnoopingMrLearnTable,
       "ruijieIgmpSnoopingMrLearnEntry": ruijieIgmpSnoopingMrLearnEntry,
       "ruijieIgmpSnoopingMrLearnVID": ruijieIgmpSnoopingMrLearnVID,
       "ruijieIgmpSnoopingMrLearnStatus": ruijieIgmpSnoopingMrLearnStatus,
       "ruijieIgmpSnoopingPortFilteringTable": ruijieIgmpSnoopingPortFilteringTable,
       "ruijieIgmpSnoopingPortFilteringEntry": ruijieIgmpSnoopingPortFilteringEntry,
       "ruijieIgmpSnoopingportIndex": ruijieIgmpSnoopingportIndex,
       "ruijieIgmpSnoopingFilteringProfile": ruijieIgmpSnoopingFilteringProfile,
       "ruijieIgmpSnoopingFilteringMaxGroups": ruijieIgmpSnoopingFilteringMaxGroups,
       "ruijieIgmpSnoopingGDAConfigTable": ruijieIgmpSnoopingGDAConfigTable,
       "ruijieIgmpSnoopingGDAConfigEntry": ruijieIgmpSnoopingGDAConfigEntry,
       "ruijieIgmpSnoopingGDAConfigVID": ruijieIgmpSnoopingGDAConfigVID,
       "ruijieIgmpSnoopingGDAConfigAddr": ruijieIgmpSnoopingGDAConfigAddr,
       "ruijieIgmpSnoopingGDAConfigIfIndex": ruijieIgmpSnoopingGDAConfigIfIndex,
       "ruijieIgmpSnoopingQueryResponeTime": ruijieIgmpSnoopingQueryResponeTime,
       "ruijieIgmpSnoopingReportSuppress": ruijieIgmpSnoopingReportSuppress,
       "ruijieIgmpSnoopingFastleave": ruijieIgmpSnoopingFastleave,
       "ruijieIgmpSnoopingGDANewTable": ruijieIgmpSnoopingGDANewTable,
       "ruijieIgmpSnoopingGDANewEntry": ruijieIgmpSnoopingGDANewEntry,
       "ruijieIgmpSnoopingGDANewInVID": ruijieIgmpSnoopingGDANewInVID,
       "ruijieIgmpSnoopingGDANewOutVID": ruijieIgmpSnoopingGDANewOutVID,
       "ruijieIgsmpSnoopingGDASrc": ruijieIgsmpSnoopingGDASrc,
       "ruijieIgmpSnoopingGDAGrp": ruijieIgmpSnoopingGDAGrp,
       "ruijieIgmpSnoopingGDAIfx": ruijieIgmpSnoopingGDAIfx,
       "ruijieIgmpSnoopingGDAIfxAction": ruijieIgmpSnoopingGDAIfxAction,
       "ruijieIgmpSnoopingMulticastWlan": ruijieIgmpSnoopingMulticastWlan,
       "ruijieIgmpSnoopingMIBConformance": ruijieIgmpSnoopingMIBConformance,
       "ruijieIgmpSnoopingMIBCompliances": ruijieIgmpSnoopingMIBCompliances,
       "ruijieIgmpSnoopingMIBCompliance": ruijieIgmpSnoopingMIBCompliance,
       "ruijieIgmpSnoopingMIBCompliance2": ruijieIgmpSnoopingMIBCompliance2,
       "ruijieIgmpSnoopingMIBGroups": ruijieIgmpSnoopingMIBGroups,
       "ruijieIgmpSnoopingMIBGroup": ruijieIgmpSnoopingMIBGroup,
       "ruijieIgmpSnoopingMIBGroup2": ruijieIgmpSnoopingMIBGroup2}
)
