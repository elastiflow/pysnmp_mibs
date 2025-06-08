# SNMP MIB module (TROPIC-OSPF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_7483/TROPIC-OSPF-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 18:04:12 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(AreaID,) = mibBuilder.importSymbols(
    "OSPF-MIB",
    "AreaID")

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

(tnOspfMIB,
 tnProtocolModules) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnOspfMIB",
    "tnProtocolModules")


# MODULE-IDENTITY

tnOspfMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 4, 3)
)
if mibBuilder.loadTexts:
    tnOspfMibModule.setRevisions(
        ("2008-03-06 12:00",
         "2008-03-28 12:00",
         "2008-06-09 12:00",
         "2008-07-24 12:00",
         "2008-12-18 12:00",
         "2009-01-09 12:00",
         "2011-04-15 12:00",
         "2011-08-31 12:00",
         "2011-09-28 12:00",
         "2012-06-13 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TnTopologyId(TextualConvention, Unsigned32):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_TnOspfConf_ObjectIdentity = ObjectIdentity
tnOspfConf = _TnOspfConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 5, 1, 1)
)
_TnOspfGroups_ObjectIdentity = ObjectIdentity
tnOspfGroups = _TnOspfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 5, 1, 1, 1)
)
_TnOspfCompliances_ObjectIdentity = ObjectIdentity
tnOspfCompliances = _TnOspfCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 5, 1, 1, 2)
)
_TnOspfObjs_ObjectIdentity = ObjectIdentity
tnOspfObjs = _TnOspfObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 5, 1, 2)
)
_TnOspfAreaTable_Object = MibTable
tnOspfAreaTable = _TnOspfAreaTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 5, 1, 2, 2)
)
if mibBuilder.loadTexts:
    tnOspfAreaTable.setStatus("current")
_TnOspfAreaEntry_Object = MibTableRow
tnOspfAreaEntry = _TnOspfAreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 5, 1, 2, 2, 1)
)
tnOspfAreaEntry.setIndexNames(
    (0, "TROPIC-OSPF-MIB", "tnOspfAreaTopologyId"),
    (0, "TROPIC-OSPF-MIB", "tnOspfAreaId"),
)
if mibBuilder.loadTexts:
    tnOspfAreaEntry.setStatus("current")
_TnOspfAreaTopologyId_Type = TnTopologyId
_TnOspfAreaTopologyId_Object = MibTableColumn
tnOspfAreaTopologyId = _TnOspfAreaTopologyId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 5, 1, 2, 2, 1, 1),
    _TnOspfAreaTopologyId_Type()
)
tnOspfAreaTopologyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnOspfAreaTopologyId.setStatus("current")
_TnOspfAreaId_Type = AreaID
_TnOspfAreaId_Object = MibTableColumn
tnOspfAreaId = _TnOspfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 5, 1, 2, 2, 1, 2),
    _TnOspfAreaId_Type()
)
tnOspfAreaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnOspfAreaId.setStatus("current")
_TnOspfPortTable_Object = MibTable
tnOspfPortTable = _TnOspfPortTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 5, 1, 2, 21)
)
if mibBuilder.loadTexts:
    tnOspfPortTable.setStatus("current")
_TnOspfPortEntry_Object = MibTableRow
tnOspfPortEntry = _TnOspfPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 5, 1, 2, 21, 1)
)
tnOspfPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnOspfPortEntry.setStatus("current")
_TnOspfPortTopologyId_Type = TnTopologyId
_TnOspfPortTopologyId_Object = MibTableColumn
tnOspfPortTopologyId = _TnOspfPortTopologyId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 5, 1, 2, 21, 1, 1),
    _TnOspfPortTopologyId_Type()
)
tnOspfPortTopologyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOspfPortTopologyId.setStatus("current")
_TnOspfMultiAreaConfigTable_Object = MibTable
tnOspfMultiAreaConfigTable = _TnOspfMultiAreaConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 5, 1, 2, 22)
)
if mibBuilder.loadTexts:
    tnOspfMultiAreaConfigTable.setStatus("current")
_TnOspfMultiAreaConfigEntry_Object = MibTableRow
tnOspfMultiAreaConfigEntry = _TnOspfMultiAreaConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 5, 1, 2, 22, 1)
)
tnOspfMultiAreaConfigEntry.setIndexNames(
    (0, "TROPIC-OSPF-MIB", "tnOspfAreaTopologyId"),
)
if mibBuilder.loadTexts:
    tnOspfMultiAreaConfigEntry.setStatus("current")
_TnOspfMultiAreaId_Type = AreaID
_TnOspfMultiAreaId_Object = MibTableColumn
tnOspfMultiAreaId = _TnOspfMultiAreaId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 5, 1, 2, 22, 1, 1),
    _TnOspfMultiAreaId_Type()
)
tnOspfMultiAreaId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOspfMultiAreaId.setStatus("current")


class _TnOspfMultiAreaConfigType_Type(Integer32):
    """Custom type tnOspfMultiAreaConfigType based on Integer32"""
    defaultValue = 1

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
        *(("normal", 1),
          ("stub", 2),
          ("totallyStub", 3),
          ("nssa", 4),
          ("nssaTotallyStub", 5))
    )


_TnOspfMultiAreaConfigType_Type.__name__ = "Integer32"
_TnOspfMultiAreaConfigType_Object = MibTableColumn
tnOspfMultiAreaConfigType = _TnOspfMultiAreaConfigType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 5, 1, 2, 22, 1, 2),
    _TnOspfMultiAreaConfigType_Type()
)
tnOspfMultiAreaConfigType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOspfMultiAreaConfigType.setStatus("current")


class _TnOspfMultiAreaConfigDnsOpaqueLsa_Type(Integer32):
    """Custom type tnOspfMultiAreaConfigDnsOpaqueLsa based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_TnOspfMultiAreaConfigDnsOpaqueLsa_Type.__name__ = "Integer32"
_TnOspfMultiAreaConfigDnsOpaqueLsa_Object = MibTableColumn
tnOspfMultiAreaConfigDnsOpaqueLsa = _TnOspfMultiAreaConfigDnsOpaqueLsa_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 5, 1, 2, 22, 1, 3),
    _TnOspfMultiAreaConfigDnsOpaqueLsa_Type()
)
tnOspfMultiAreaConfigDnsOpaqueLsa.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOspfMultiAreaConfigDnsOpaqueLsa.setStatus("current")


class _TnOspfMultiAreaConfigWavekeyOpaqueLsa_Type(Integer32):
    """Custom type tnOspfMultiAreaConfigWavekeyOpaqueLsa based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_TnOspfMultiAreaConfigWavekeyOpaqueLsa_Type.__name__ = "Integer32"
_TnOspfMultiAreaConfigWavekeyOpaqueLsa_Object = MibTableColumn
tnOspfMultiAreaConfigWavekeyOpaqueLsa = _TnOspfMultiAreaConfigWavekeyOpaqueLsa_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 5, 1, 2, 22, 1, 4),
    _TnOspfMultiAreaConfigWavekeyOpaqueLsa_Type()
)
tnOspfMultiAreaConfigWavekeyOpaqueLsa.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOspfMultiAreaConfigWavekeyOpaqueLsa.setStatus("current")


class _TnOspfMultiAreaConfigNssaTranslate_Type(Integer32):
    """Custom type tnOspfMultiAreaConfigNssaTranslate based on Integer32"""
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
        *(("candidate", 1),
          ("always", 2),
          ("never", 3),
          ("notApplicable", 4))
    )


_TnOspfMultiAreaConfigNssaTranslate_Type.__name__ = "Integer32"
_TnOspfMultiAreaConfigNssaTranslate_Object = MibTableColumn
tnOspfMultiAreaConfigNssaTranslate = _TnOspfMultiAreaConfigNssaTranslate_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 5, 1, 2, 22, 1, 5),
    _TnOspfMultiAreaConfigNssaTranslate_Type()
)
tnOspfMultiAreaConfigNssaTranslate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOspfMultiAreaConfigNssaTranslate.setStatus("current")


class _TnOspfMultiAreaConfigDefaultCost_Type(Integer32):
    """Custom type tnOspfMultiAreaConfigDefaultCost based on Integer32"""
    defaultValue = 10


_TnOspfMultiAreaConfigDefaultCost_Type.__name__ = "Integer32"
_TnOspfMultiAreaConfigDefaultCost_Object = MibTableColumn
tnOspfMultiAreaConfigDefaultCost = _TnOspfMultiAreaConfigDefaultCost_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 5, 1, 2, 22, 1, 6),
    _TnOspfMultiAreaConfigDefaultCost_Type()
)
tnOspfMultiAreaConfigDefaultCost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOspfMultiAreaConfigDefaultCost.setStatus("current")
_TnOspfMultiAreaConfigVirtualLinkIp_Type = IpAddress
_TnOspfMultiAreaConfigVirtualLinkIp_Object = MibTableColumn
tnOspfMultiAreaConfigVirtualLinkIp = _TnOspfMultiAreaConfigVirtualLinkIp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 5, 1, 2, 22, 1, 7),
    _TnOspfMultiAreaConfigVirtualLinkIp_Type()
)
tnOspfMultiAreaConfigVirtualLinkIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOspfMultiAreaConfigVirtualLinkIp.setStatus("current")


class _TnOspfMultiAreaConfigRowStatus_Type(RowStatus):
    """Custom type tnOspfMultiAreaConfigRowStatus based on RowStatus"""
    defaultValue = 6


_TnOspfMultiAreaConfigRowStatus_Type.__name__ = "RowStatus"
_TnOspfMultiAreaConfigRowStatus_Object = MibTableColumn
tnOspfMultiAreaConfigRowStatus = _TnOspfMultiAreaConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 5, 1, 2, 22, 1, 8),
    _TnOspfMultiAreaConfigRowStatus_Type()
)
tnOspfMultiAreaConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOspfMultiAreaConfigRowStatus.setStatus("current")

# Managed Objects groups

tnOspfAreaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 5, 1, 1, 1, 2)
)
tnOspfAreaGroup.setObjects(
      *(("TROPIC-OSPF-MIB", "tnOspfAreaTopologyId"),
        ("TROPIC-OSPF-MIB", "tnOspfAreaId"))
)
if mibBuilder.loadTexts:
    tnOspfAreaGroup.setStatus("current")

tnOspfPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 5, 1, 1, 1, 21)
)
tnOspfPortGroup.setObjects(
    ("TROPIC-OSPF-MIB", "tnOspfPortTopologyId")
)
if mibBuilder.loadTexts:
    tnOspfPortGroup.setStatus("current")

tnOspfMultiAreaConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 5, 1, 1, 1, 22)
)
tnOspfMultiAreaConfigGroup.setObjects(
      *(("TROPIC-OSPF-MIB", "tnOspfMultiAreaId"),
        ("TROPIC-OSPF-MIB", "tnOspfMultiAreaConfigType"),
        ("TROPIC-OSPF-MIB", "tnOspfMultiAreaConfigDnsOpaqueLsa"),
        ("TROPIC-OSPF-MIB", "tnOspfMultiAreaConfigWavekeyOpaqueLsa"),
        ("TROPIC-OSPF-MIB", "tnOspfMultiAreaConfigNssaTranslate"),
        ("TROPIC-OSPF-MIB", "tnOspfMultiAreaConfigDefaultCost"),
        ("TROPIC-OSPF-MIB", "tnOspfMultiAreaConfigVirtualLinkIp"),
        ("TROPIC-OSPF-MIB", "tnOspfMultiAreaConfigRowStatus"))
)
if mibBuilder.loadTexts:
    tnOspfMultiAreaConfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tnOspfCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 5, 1, 1, 2, 1)
)
tnOspfCompliance.setObjects(
      *(("TROPIC-OSPF-MIB", "tnOspfAreaGroup"),
        ("TROPIC-OSPF-MIB", "tnOspfPortGroup"),
        ("TROPIC-OSPF-MIB", "tnOspfMultiAreaConfigGroup"))
)
if mibBuilder.loadTexts:
    tnOspfCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TROPIC-OSPF-MIB",
    **{"TnTopologyId": TnTopologyId,
       "tnOspfMibModule": tnOspfMibModule,
       "tnOspfConf": tnOspfConf,
       "tnOspfGroups": tnOspfGroups,
       "tnOspfAreaGroup": tnOspfAreaGroup,
       "tnOspfPortGroup": tnOspfPortGroup,
       "tnOspfMultiAreaConfigGroup": tnOspfMultiAreaConfigGroup,
       "tnOspfCompliances": tnOspfCompliances,
       "tnOspfCompliance": tnOspfCompliance,
       "tnOspfObjs": tnOspfObjs,
       "tnOspfAreaTable": tnOspfAreaTable,
       "tnOspfAreaEntry": tnOspfAreaEntry,
       "tnOspfAreaTopologyId": tnOspfAreaTopologyId,
       "tnOspfAreaId": tnOspfAreaId,
       "tnOspfPortTable": tnOspfPortTable,
       "tnOspfPortEntry": tnOspfPortEntry,
       "tnOspfPortTopologyId": tnOspfPortTopologyId,
       "tnOspfMultiAreaConfigTable": tnOspfMultiAreaConfigTable,
       "tnOspfMultiAreaConfigEntry": tnOspfMultiAreaConfigEntry,
       "tnOspfMultiAreaId": tnOspfMultiAreaId,
       "tnOspfMultiAreaConfigType": tnOspfMultiAreaConfigType,
       "tnOspfMultiAreaConfigDnsOpaqueLsa": tnOspfMultiAreaConfigDnsOpaqueLsa,
       "tnOspfMultiAreaConfigWavekeyOpaqueLsa": tnOspfMultiAreaConfigWavekeyOpaqueLsa,
       "tnOspfMultiAreaConfigNssaTranslate": tnOspfMultiAreaConfigNssaTranslate,
       "tnOspfMultiAreaConfigDefaultCost": tnOspfMultiAreaConfigDefaultCost,
       "tnOspfMultiAreaConfigVirtualLinkIp": tnOspfMultiAreaConfigVirtualLinkIp,
       "tnOspfMultiAreaConfigRowStatus": tnOspfMultiAreaConfigRowStatus}
)
